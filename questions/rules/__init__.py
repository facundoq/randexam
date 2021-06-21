
import abc
class Condition(abc.ABC):
    @abc.abstractmethod
    def matches(self,row):
        pass

    def count_matches(self,rows):
        return sum(map(self.matches,rows))

class AndConditions(Condition):
    def __init__(self,conditions:[Condition]):
        self.conditions=conditions

    def matches(self,row):
        return all([c.matches(row) for c in self.conditions])
    
    def __repr__(self):
        return " and ".join(map(str,self.conditions))

class AttributeValueNominal(Condition):
    def __init__(self,index:int,v:str,name:str=None):
        self.index=index
        self.v=v
        self.name=name

    def matches(self,row):
        return row[self.index]==self.v
    
    def __repr__(self):
        attribute_name= f"Column{self.index}" if self.name is None else self.name
        return f"{attribute_name} = {self.v}"

from enum import Enum
class Operator(Enum):
    lt="<"
    lte="<="
    gt=">"
    gte=">="
    eq="="
    neq="="


    def apply(self,v1,v2):
        if self==Operator.lt:
            return v1<v2
        elif self==Operator.lte:
            return v1<=v2
        elif self==Operator.gt:
            return v1>v2
        elif self==Operator.gte:
            return v1>=v2
        elif self==Operator.eq:
            return v1==v2
        elif self==Operator.neq:
            return v1!=v2
        raise ValueError(self)

class AttributeRange(Condition):
    def __init__(self,index:int,limit:float,o:Operator,name:str=None):
        self.index=index
        self.limit=limit
        self.o=o
        self.name=name

    def matches(self,row):
        return self.o.apply(row[self.index],self.limit)
    
    def __repr__(self):
        attribute_name= f"Column{self.index}" if self.name is None else self.name
        return f"{attribute_name} {self.o.value} {self.limit}"

class Rule(Condition):
    def __init__(self,antecedent:Condition,consecuent:Condition):
        self.antecedent=antecedent
        self.consequent=consecuent
    def matches(self,row):
        return self.antecedent.matches(row) and self.consequent.matches(row)
    
    # def matches_antecedent(self,row):
    #     return self.matches_rule_list(row,self.antecedents)
    # def matches_consequent(self,row):
    #     return self.matches_rule_list(row,self.consequents)

    def __repr__(self):
        return f"{self.antecedent} → {self.consequent}"

class DatasetMetric(abc.ABC):
    @abc.abstractmethod
    def eval(self,r:Rule,rows:[[]]):
        pass

    @classmethod
    def eval_all(cls,r:Rule,rows:[[]]):
        rules={"Soporte":Support,"Cobertura":Coverage,"Confianza":Confidence,"Interés":Lift}
        results={}
        for k,v in rules.items():
            results[k]=v().eval(r,rows)
        return results

class Support(DatasetMetric):
    def eval(self,r:Condition,rows:[[]]):
        return r.count_matches(rows)/len(rows)

class Coverage(DatasetMetric):
    def eval(self,r:Condition,rows:[[]]):
        
        return r.antecedent.count_matches(rows)/len(rows)

import numpy as np        
class Lift(DatasetMetric):
    def eval(self,r:Condition,rows:[[]]):
        s=Support()
        denominator=s.eval(r.antecedent,rows) * s.eval(r.consequent,rows)
        if denominator==0:
            return np.Inf
        else:
            r= s.eval(r,rows) /denominator
        return r

class Confidence(DatasetMetric):    
    def eval(self,r:Condition,rows:[[]]):
        count_a=r.antecedent.count_matches(rows)
        if count_a==0:
            return 1
        else:
            return r.count_matches(rows)/count_a



from typing import Dict,List
class OneR:
    def __init__(self,rules:[Rule],attribute_name:str=None,attribute_stats=None):
        super().__init__()
        self.rules=rules
        self.attribute_name=attribute_name
        self.attribute_stats=attribute_stats

    def predict(self,row):
        for r in self.rules:
            if r.antecedent.matches(row):
                return r.consequent.v
        raise ValueError(f"No condition available for sample {row}")
    
    def predict_all(self,rows):
        return [self.predict(r) for r in rows]

    def accuracy(self,rows,y):
        predictions=self.predict_all(rows)
        n=len(rows)
        tp=sum([p==t for p,t in zip(predictions,y)])
        return tp/n
    
    @classmethod
    def transpose(cls,rows):
        n,m=len(rows), len(rows[0])
        return [ [rows[i][j] for i in range(n)] for j in range(m)]
        
    @classmethod
    def fit(cls,rows,attributes:[str]):
        columns=cls.transpose(rows)
        # assume class is last column
        class_index=len(attributes)
        # separate features from class
        y=columns[class_index]
        columns=columns[:class_index]
        classes=list(set(y))
        attribute_models=[]
        confidence_metric=Confidence()
        for i,attribute in enumerate(attributes):
            values=columns[i]
            unique_values=list(set(values))
            rules=[]
            for v in unique_values:
                antecedent=AttributeValueNominal(i,v,name=attribute)
                def class_rule(c):
                    return Rule(antecedent,AttributeValueNominal(class_index,c,name="Clase"))            
                possible_rules=[class_rule(c) for c in classes]
                confidences=[confidence_metric.eval(r,rows) for r in possible_rules]
                best_rule_index=confidences.index(max(confidences))
                rules.append(possible_rules[best_rule_index])
            attribute_models.append(OneR(rules,attribute_name=attribute))
        
        accuracies = [model.accuracy(rows,y) for model in attribute_models]
        best_attribute_index=accuracies.index(max(accuracies))
        return attribute_models[best_attribute_index],attribute_models

