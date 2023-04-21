
import numpy as np

log_base = 10

def log(p:np.ndarray):
    return np.log2(p)/np.log2(log_base)

def score(classes):
    # frecuencia de c/valor del atributo
    unique_elements, counts_elements = np.unique(classes, return_counts=True)
    # N = cant.total de valores
    n = len(classes)
    
    # E = valor de entropia
    E = 0
    for i in counts_elements:
        p=i/n
        E = E - p*log(p)

    return E
    

def calculate_entropy(p:np.ndarray)->float:
    '''
    :param p: 1D vector of size C with class probabilities/relative frequencies
    :return: entropy of p
    '''
    E=0
    for i in range(len(p)):
        if p[i]>0:
            E += -p[i]*np.log2(p[i])
        else:
            E += 0
    #Alternative implementation
    #E=-np.sum(p*np.log2(p))
    return E


def entropy_nominal(values, y):
    if isinstance(values[0],str):
        #reencode as int
        unique_values=list(set(values))
        values=[unique_values.index(v) for v in values]
        values=np.array(values)
    # frecuencia de c/valor del atributo
    
    unique_values, counts = np.unique(values, return_counts=True)

    E = 0
    n = len(values)
    
    
    for v,c in zip(unique_values,counts):
        # analizando una rama
        value_y = y[values==v]
        value_entropy = score(value_y)
        p=c/n
        E = E + p * value_entropy
    return E
def pairwise(t):
    return zip(t, t[1:])

def binary_discretize(values:np.ndarray,discretization_point:float):
    values=values.copy()
    values[values<discretization_point]=0
    values[values>=discretization_point]=1
    return values

def entropy_numeric(values, y):
    indices=np.argsort(values)
    values=values[indices]
    y=y[indices]
    discretization_points=np.array([(a+b)/2 for a,b in pairwise(values) if a!=b])
    entropies=[]
    for p in discretization_points:
        discretized_values=binary_discretize(values,p)
        entropies.append(entropy_nominal(discretized_values,y))
    
    return np.array(entropies), discretization_points


def information_gain_nominal(values,y):
    E=score(y)
    values_E=entropy_nominal(values,y)
    return E-values_E

def information_gain_numeric(values,y):
    E=score(y)
    entropies,values=entropy_numeric(values,y)
    return E-entropies,values




def divide0(a:np.ndarray,b:np.ndarray)->np.ndarray:
    #make 0/0=0
    print(a.shape,b.shape)
    print(a,b)
    return np.divide(a, b, out=np.zeros_like(a), where=b!=0)
import pandas as pd

def value_counts_base(s:pd.Series,vals:list)->np.ndarray:
    result = np.zeros(len(vals))

    n = len(s)
    for i,v in enumerate(vals):
        result[i] = (s==v).sum() / n
    return result