from abc import ABC,abstractmethod
import numpy as np
from scipy.stats import norm
import pandas as pd

from pandas.api.types import is_string_dtype,is_numeric_dtype,is_bool_dtype
from pandas.api.types import is_numeric_dtype


class Variable(ABC):
    @abstractmethod
    def predict(x,debug=False):
        pass    
    
    @classmethod
    def fit_pandas_column(cls,col:pd.Series,kwargs):
        if is_numeric_dtype(col):
            return GaussianVariable.fit(col.to_numpy(),*kwargs)
        elif is_string_dtype(col):
            return CategoricalVariable.fit(col.to_list(),*kwargs)
        elif is_bool_dtype(col):
            return CategoricalVariable.fit(col.to_list(),*kwargs)
        else:
            raise ValueError(f"Unsupported dtype {col.dtype}")
    

class GaussianVariable(Variable):

    @classmethod
    def fit(cls,values:np.array,smoothing:float=0):
        mu= values.mean()
        std = values.std(ddof=1)
        return GaussianVariable(mu,std,smoothing=smoothing)
    
    def __init__(self,mu:float,std:float,smoothing:float=0) -> None:
        self.mu=mu
        self.std=std
        self.norm=norm(mu,std+smoothing)


    def predict(self,x:np.array):
        return self.norm.pdf(np.array(x))

    def __repr__(self) -> str:
        return f"N~({self.mu},{self.std})"

class CategoricalVariable(Variable):
    
    def __init__(self,probabilities:dict[str,float]) -> None:
        self.probabilities = probabilities
    
    @classmethod
    def fit(cls,values:list,value_set=None, smoothing:float = 0):
        if value_set is None:
            value_set = set(values)
        n = len(values)
        probabilities = { v:(values.count(v)/n)+smoothing for v in value_set }
        total = sum(probabilities.values())
        probabilities = {v:(p/total) for v,p in probabilities.items()}
        return CategoricalVariable(probabilities)

    def predict(self,x):
        return np.array(list(map(lambda v:self.probabilities[v],x)))
        
    def __repr__(self) -> str:
        return f"C~({self.probabilities})"

def split_by_class(df:pd.DataFrame,y:np.array,class_names:np.array):
    return [(df.loc[y==name,:],name) for name in class_names]

class NaiveBayesSingleClass:
    @classmethod
    def fit(cls,x:pd.DataFrame,variable_kwargs={}):
        variables = { name:Variable.fit_pandas_column(col,variable_kwargs.get(name,{})) for name,col in x.items()}
        return NaiveBayesSingleClass(variables)
    
    def __init__(self,variables:dict[str,Variable]):    
        self.variables=variables
        
    def predict(self,x:pd.DataFrame):
        p = 1
        for name,var in self.variables.items():
            value = x[name]
            pi = var.predict(value)
            p *= pi
        return p
        
    def __repr__(self) -> str:
        variables = '\n\n'.join([f"{k}: {v}" for k,v in self.variables.items()])
        return f"Distribuciones:\n\n {variables}"

class NaiveBayes:

    def __init__(self,class_names:list[str],class_models:list[NaiveBayesSingleClass],class_probabilities:CategoricalVariable):
        self.class_names = class_names
        self.class_models = class_models
        self.class_probabilities = class_probabilities
        
    @classmethod
    def fit(cls,x:pd.DataFrame,y:np.ndarray[str],variable_kwargs={},smoothing_classes=0):
        class_names = np.unique(y)
        class_models = [NaiveBayesSingleClass.fit(samples,variable_kwargs) for samples,name in split_by_class(x,y,class_names)]
        class_probabilities = CategoricalVariable.fit(list(y),smoothing=smoothing_classes)
        return NaiveBayes(class_names,class_models,class_probabilities)
    
    @property
    def n_classes(self):
        return len(self.class_names)
    
    def predict(self,x:pd.DataFrame,debug=False):
        if debug:
            details = []
        n = len(x)
        results = np.zeros( (n,self.n_classes))
        for c in range(self.n_classes): 
            p_x = self.class_models[c].predict(x)
            name = self.class_names[c]
            p_class = self.class_probabilities.predict([name])[0]
            results[:,c]= p_x*p_class
            if debug:
                name = self.class_names[c]
                details.append([f"Clase {name}","","","",""])
                for i in range(n):  
                    details.append([f"Ejemplo {i}", f"P(c={name})={p_class:.2f}", f"p(x \| c={name})={p_x[i]:.2e}",f"p(c={name} \| x)={results[i,c]:.2e}"])
        if debug:
            return results, details
        else:
            return results
    def predict_classes(self,x:pd.DataFrame,debug=False):
        prob = self.predict(x,debug=debug)
        classes = prob.argmax(axis=1)
        pred = np.array([self.class_names[i] for i in classes])
        return pred
    
    def __repr__(self) -> str:
        
        def class_description(i:int):
            name = self.class_names[i]
            p_c = self.class_probabilities.predict([name])[0]
            return f"Clase {name}: (P(c={name})={p_c}):\n\n {self.class_models[i]}"
        class_descriptions = [ class_description(i) for i in range(self.n_classes)]
        class_descriptions = '\n\n'.join(class_descriptions)
        return f"{NaiveBayes.__name__}\n\n {class_descriptions}" 
        
    def table(self) -> str:
        rows = []
        for c,cm in enumerate(self.class_models):
            name =self.class_names[c]
            rows.append([f"Clase {name}",f"P(c={name}) = {self.class_probabilities.predict([name])[0]}"])
            for k,v in cm.variables.items():
                rows.append([f"{k}",f"{v}"])
        
        return rows


