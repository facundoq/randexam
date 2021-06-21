
import numpy as np


def entropy(classes):
    # frecuencia de c/valor del atributo
    unique_elements, counts_elements = np.unique(classes, return_counts=True)
    # N = cant.total de valores
    n = len(classes)
    
    # E = valor de entropia
    E = 0
    for i in counts_elements:
        p=i/n
        E = E - p*np.log2(p)
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
        value_entropy = entropy(value_y)
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
    E=entropy(y)
    values_E=entropy_nominal(values,y)
    return E-values_E

def information_gain_numeric(values,y):
    E=entropy(y)
    entropies,values=entropy_numeric(values,y)
    return E-entropies,values
