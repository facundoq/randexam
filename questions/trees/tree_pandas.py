from __future__ import annotations
import numpy as np
import abc
import typing
import pandas as pd

Sample = dict[str,object]
ClassProbabilities = dict[str,float]
eps = 1e-8
default_sep = 4

class DecisionTree:

    def __init__(self,root:DecisionTreeNode,class_names:list[str]) -> None:
        self.root=root
        self.class_names=class_names

    @abc.abstractmethod
    def classify(self,x:Sample)->int:
        class_probabilities = self.root.classify(x)
        klass = class_probabilities.argmax()
        return klass,self.class_names[klass],class_probabilities

    @abc.abstractmethod
    def pretty_print(self,sep=default_sep)->str:
        return self.root.pretty_print(class_names=self.class_names)
    
class DecisionTreeNode(abc.ABC):
    '''
    Abstract DecisionTree class
    with Intermediate and Leaf concrete subclasses
    This design avoids ifs and unitialized values
    Since intermediate and leaf nodes hold very different data
    '''

    
    def __init__(self,class_probabilities:np.ndarray):
        if isinstance(class_probabilities,list):
            class_probabilities=np.array(class_probabilities)
        assert np.abs(np.sum(class_probabilities)-1)<eps, f"Probabilities should sum to 1 {class_probabilities}"
        self.class_probabilities=class_probabilities

    @property
    def most_frequent_class(self):
        return self.class_probabilities.argmax()
    
    def classify(self,x:Sample)->int:
        return self.class_probabilities

    @abc.abstractmethod
    def pretty_print(self,depth=0,sep=default_sep,class_names:list[str]=None)->str:
        pass

class DecisionTreeNumericNode(DecisionTreeNode):
    def __init__(self,class_probabilities:np.ndarray,column:str,split_value:int,child_left:DecisionTreeNode,child_right:DecisionTreeNode):
        super().__init__(class_probabilities)
        self.column=column
        self.child_left = child_left
        self.child_right = child_right
        self.split_value=split_value

    def classify(self,x:Sample)->int:
        if x[self.column]<=self.split_value:
            return self.child_left.classify(x)
        else:
            return self.child_right.classify(x)

    def __repr__(self)->str:
        return f"{self.__class__.__name__}(column={self.column},split_value={self.split_value})"
    @property
    def children(self):
        return {f"<={self.split_value}":self.child_left,f">{self.split_value}":self.child_right}
    
    def pretty_print(self,depth=0,sep=4,class_names:list[str]=None)->str:
        tabs = " "*depth*sep
        children_description = [f"{tabs}{self.column}={v} → {child.pretty_print(depth=depth+1,class_names=class_names)}" for v,child in self.children.items()]
        children_description = "\n".join(children_description)
        start = "\n" if depth>0 else ""        
        return f"{start}{children_description}\n"
    
class DecisionTreeNominalNode(DecisionTreeNode):
    def __init__(self,class_probabilities:np.ndarray,column:str,children:dict[object,DecisionTreeNode]):
        super().__init__(class_probabilities)
        self.column=column
        self.children=children

    def classify(self,x:Sample)->int:
        # Intermediate nodes of the decision tree just route samples to their children nodes
        value=x[self.column]
        # If there's a branch for this value, do a recursive call
        if value in self.children:
            return self.children[value].classify(x)
        # If not, just return the class distribution up to this node.
        else:
            return super().classify(x)
    
    def __repr__(self)->str:
        return f"{self.__class__.__name__}(children_column={self.column})"

    def pretty_print(self,depth=0,sep=4,class_names:list[str]=None)->str:
        tabs = " "*depth*sep
        children_description = [f"{tabs}{self.column}={v} → {child.pretty_print(depth=depth+1,class_names=class_names)}" for v,child in self.children.items()]
        children_description = "\n".join(children_description)
        start = "\n" if depth>0 else ""        
        return f"{start}{children_description}\n"

class DecisionTreeLeafNode(DecisionTreeNode):
    def __init__(self,class_probabilities:np.ndarray):
        super().__init__(class_probabilities)
    
    def __repr__(self)->str:
        return f"{self.__class__.__name__}(class={self.class_probabilities})"

    def pretty_print(self,depth=0,sep=3,class_names:list[str]=None)->str:
        if class_names is None:
            class_name = str(self.most_frequent_class)
        else:
            class_name = class_names[self.most_frequent_class]
        return f"Clase = {class_name} {self.class_probabilities}"



if __name__ == '__main__':
    cp = [0.5,0.5]
    tree = DecisionTree(DecisionTreeNominalNode(cp,"Titulo",{
        "SI":DecisionTreeNominalNode(cp,"Experiencia",{
            "BAJA": DecisionTreeLeafNode([0.75,0.25]),
            "MEDIA": DecisionTreeNominalNode(cp,"Trabaja",{
                "SI":DecisionTreeLeafNode([0.3,0.7]),
                "NO":DecisionTreeLeafNode([0.4,0.6]),
            }),
            "ALTA": DecisionTreeLeafNode([0.1,0.9],),
        }),
        "NO":DecisionTreeLeafNode([0.9,0.1]),
    }), ["NO","SI"])
    print(tree.pretty_print())

    df=pd.read_csv("data/trabajos_ej4.csv", sep=",")
    x=df[df.columns[:-1]]
    y=df[df.columns[-1:]]

    print(tree.classify(x.iloc[0,:]))