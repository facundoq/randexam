from __future__ import annotations
import numpy as np
import pandas as pd

#from .tree_pandas import DecisionTreeNode,DecisionTreeLeafNode,DecisionTreeValueNode
from questions.trees.tree_pandas import DecisionTreeNode,DecisionTreeLeafNode,DecisionTreeNominalNode,ClassProbabilities,DecisionTree,DecisionTreeNumericNode
from questions.trees import utils

class DatasetInfo:
    def __init__(self, class_names:list[str], column_names:list[str]):
        self.column_names=column_names
        self.class_names=class_names
    @property
    def n_classes(self):
        return len(self.class_names)

# Training configuration for decision tree
class DecisionTreeConfig:
    def __init__(self, min_info_gain:float=1e-8, minimal_leaf_size:int=1, minimal_size_for_split=1, max_height:int=np.iinfo(int).max,verbose=False):
        if minimal_size_for_split<1:
            raise ValueError(f"minimal_size_for_split must be equal or greater than 1")
        if minimal_leaf_size<1:
            raise ValueError(f"minimal_leaf_size must be equal or greater than 1")
        if min_info_gain<=0:
            raise ValueError(f"min_info_gain must be greater than 0")
        
        self.minimal_size_for_split=minimal_size_for_split
        self.min_info_gain=min_info_gain
        self.minimal_leaf_size=minimal_leaf_size
        self.max_height=max_height
        self.verbose=verbose

    def log(self,m:str):
        if self.verbose:
            print(m)

def fit(x:pd.DataFrame, y:pd.Series,c=DecisionTreeConfig()):
    class_names = y.unique()
    assert len(x.columns)>=1
    class_probabilities = y.value_counts(normalize=True)
    # c.log(class_probabilities)
    root = create_tree(x,y,c,class_probabilities,class_names,height=0)
    return DecisionTree(root,class_names)

def create_tree(x:pd.DataFrame, y:pd.Series,c:DecisionTreeConfig,class_probabilities:np.ndarray,class_names:list,height:int)->DecisionTreeNode:
    rows,cols=x.shape
    assert rows>=c.minimal_leaf_size, f"Cannot build tree, the number of samples ({rows}) is less than the minimum number of samples per leaf ({c.minimal_leaf_size})"
    # c.log(height,x.shape,x.columns,"\n",x)
    # Base case: no more columns to split on
    c.log(" "*(height*2))
    if cols==0:
        if c.verbose:
            c.log("No more columns")
        return DecisionTreeLeafNode(class_probabilities)
    
    # Base case: max tree height reached
    if height==c.max_height:
        if c.verbose:
            c.log(f"Max height {c.max_height} reached")
        return DecisionTreeLeafNode(class_probabilities)
    
    # Base case: not enough samples to continue splitting
    if rows<c.minimal_size_for_split:
        if c.verbose:
            c.log(f"Minimal size of split ({c.minimal_size_for_split}) not achieved ({rows} rows); prepruning tree.")
        return DecisionTreeLeafNode(class_probabilities)

    # Find best column to split on
    splitting_column=calculate_best_split_column(x, y, class_names,c)
    # calculate info gain
    entropy=utils.calculate_entropy(class_probabilities)
    info_gain=entropy-splitting_column.entropy

    if c.verbose:
        c.log(f"Best column: {splitting_column.name}")

    # Base case: info gain less than minimum
    if info_gain <c.min_info_gain:
        return DecisionTreeLeafNode(class_probabilities)
    
    # no base case: do a recursive split
    # print(f"do recursive on {splitting_column.name}")
    if pd.api.types.is_numeric_dtype(x[splitting_column.name]):
        node = recursive_split_numeric(x,y,splitting_column,class_names,class_probabilities,height)
    else:
        node = recursive_split_nominal(x,y,splitting_column,class_names,class_probabilities,height)
    return node


def calculate_best_split_column(x:pd.DataFrame, y:pd.Series, classes:list,config:DecisionTreeConfig)->NominalColumnInfo:
    
    best_column=None
    for column in x.columns:
        
        xc = x[column]
        print(column,"\n",xc)
        if pd.api.types.is_numeric_dtype(xc):
            column = NumericColumnInfo.calculate_column_entropy(xc, y, classes,config)
        else:
            column = NominalColumnInfo.calculate_column_entropy(xc, y, classes,config)
        c.log(f"Column {column.name}, entropy {column.entropy}, class probabilities: {column.class_probabilities}")
        if best_column is None or column.entropy<best_column.entropy:
            best_column=column
    return best_column

def recursive_split_nominal(x,y,col:NominalColumnInfo,class_names:list,class_probabilities:np.ndarray,height:int):
    # Recursive case: split on the selected column
    children={}
    # remove this column from consideration
    column_values = x[col.name]
    x = x.drop(col.name,axis=1)
    c.log(f"data without column\n {x}")
    #x = x.drop(col.name,axis=1,inplace=False)
    for v,vp in col.class_probabilities.items():
        indices = column_values==v
        # Select samples for column value
        vx=x[indices]
        vy=y[indices]
        c.log(f"Branch {col.name}={v}:")
        c.log(vx)
        children[v]=create_tree(vx,vy,c,vp,class_names,height+1)
        c.log(f"Finished brach {col.name}={v}")
    return DecisionTreeNominalNode(class_probabilities,col.name,children)

def recursive_split_numeric(x,y,column:NumericColumnInfo,class_names:list,class_probabilities:np.ndarray,height:int):
    # Recursive case: split on the selected column
    
    # remove this column from consideration
    column_values = x[column.name]
    x_left = x[column_values<=column.split_value]
    y_left = y[column_values<=column.split_value]
    
    x_right = x[column_values>column.split_value]
    y_right = y[column_values>column.split_value]
    print(class_probabilities)
    child_left = create_tree(x_left,y_left,c,column.class_probabilities[0],class_names,height+1)
    child_right = create_tree(x_right,y_right,c,column.class_probabilities[1],class_names,height+1)

        # c.log(f"Finished brach {col.name}={v}")
    return DecisionTreeNumericNode(class_probabilities,column.name,column.split_value,child_left,child_right)

class NumericColumnInfo:
    def __init__(self, name:str,class_probabilities:list[np.ndarray], entropy:float,split_value:float):
        self.name=name
        self.class_probabilities=class_probabilities
        self.entropy=entropy
        self.split_value=split_value
    
    @classmethod
    def calculate_column_entropy(cls,x:pd.Series, y:pd.Series, classes:list,c:DecisionTreeConfig)->NominalColumnInfo:
        # Calculate entropy of the attribute
        # by searching for the best 
        values = x.unique()
        print(values,len(x))
        values.sort()
        split_points = [(v1+v2)/2 for v1,v2 in zip(values[:-1],values[1:])]
        if len(split_points)==0:
            return  NominalColumnInfo.calculate_column_entropy(x,y,classes,c)
        best_split = None
        best_column = None
        
        for split_point in split_points:
            cut_x = pd.cut(x,[-np.inf,split_point,np.inf])
            print(cut_x)
            column = NominalColumnInfo.calculate_column_entropy(cut_x,y,classes,c)
            if best_split is None or column.entropy<best_column.entropy:
                print(column.name)
                best_split = split_point
                best_column = column                
        return NumericColumnInfo(best_column.name,best_column.class_probabilities,best_column.entropy,best_split)
    
class NominalColumnInfo:
    def __init__(self, name:str,class_probabilities:dict[str,np.ndarray], entropy:float):
        self.name=name
        self.class_probabilities=class_probabilities
        self.entropy=entropy
        
    
    @classmethod
    def calculate_column_entropy(cls,x:pd.Series, y:pd.Series, classes:list,c:DecisionTreeConfig)->NominalColumnInfo:
        frequencies,percentages=NominalColumnInfo.calculate_frequencies(x,y,classes,c)
        # Calculate entropy of the attribute
        # by weighting the entropies of each value
        # with the percentage of samples of each value
        entropies = {}
        entropy = 0
        for v in frequencies.keys():
                entropies[v]=utils.calculate_entropy(frequencies[v])
                entropy+= entropies[v]*percentages[v]
        return NominalColumnInfo(x.name,frequencies,entropy)
    
    @classmethod
    def calculate_frequencies(cls,x:pd.Series, y:pd.Series, classes:list,config:DecisionTreeConfig):
        # Get counts for each value            
        counts = {v:len(y[x==v]) for v in x.unique()}
        # filter values that have less than minimal leaf size samples
        counts = {v:c for v,c in counts.items() if c>=config.minimal_leaf_size}
        #calculate percentages per values
        n = sum(counts.values())
        percentages = {v:c/n for v,c in counts.items()}
        
        # calculate class frecuencies for each value that passed the above filter
        frequencies = {v:utils.value_counts_base(y[x==v],classes) for v in counts.keys()}
        
        return frequencies,percentages
    


import numpy as np
import pandas as pd

if __name__ == '__main__':
    df=pd.read_csv("data/trabajos_ej4.csv", sep=",")
    x=df[df.columns[:-1]]

    y=df[df.columns[-1:]]["Contratar"]
    print(x)
    print("----")
    print(y)
    
    c = DecisionTreeConfig(verbose=True,max_height=3)

    dt = fit(x,y,c)
    
    # print(dt)
    print(dt.pretty_print())


