from .exam import Question
from questions import preprocessing
import copy
import pandas as pd
from pathlib import Path
import pandas as pd

class Dataset:

    @classmethod
    def from_csv(cls,path:Path,class_index:int):
        df = pd.read_csv(path)
        header = list(df.columns)
        attributes = header[:class_index]+header[class_index+1:]
        class_values = df.iloc[class_index].unique()
        rows = df.to_numpy().tolist()
        return Dataset(rows,header,attributes,class_values)

    def __init__(self, rows:list, header: list[str], attributes: list[str], class_values: list[str], ordinal_values=None):
        self.rows = rows
        self.header = header
        self.attributes = attributes
        self.class_values = class_values
        self.ordinal_values = ordinal_values

    @property
    def n(self):
        return len(self.rows)

    @property
    def m(self):
        return len(self.header)

    @property
    def str_rows(self):
        return [[str(v) for v in row] for row in self.rows]

    def column(self, column: int):
        return [row[column] for row in self.rows]

    def attribute(self, attribute: str):
        column = self.attributes.index(attribute)
        return self.column()

    def row(self, row: int):
        return self.rows[row]

    def discretize(self, col, new_values, strategy: preprocessing.Discretization):
        
        d = self.copy()
        values = d.column(col)
        
        intervals, values = preprocessing.discretize(values, new_values, strategy)

        #values = [new_values[i] for i in values]
        d.replace_column(col, values)
        return d

    def replace_column(self, col, values):
        for r, v in zip(self.rows, values):
            r[col] = v
    def delete_column(self,col):
        for r in self.rows:
            del r[col]
        del self.header[col]

    def insert_column(self,values,header,index):
        self.header.insert(index,header)
        for r,v in zip(self.rows,values):
            r.insert(index,v)

    def copy(self):
        rows = copy.deepcopy(self.rows)
        header = copy.deepcopy(self.header)
        attributes = copy.deepcopy(self.attributes)
        class_values = copy.deepcopy(self.class_values)
        return Dataset(rows, header, attributes, class_values, self.ordinal_values)
    
    def __repr__(self) -> str:
        rows_str = [", ".join(map(str,row)) for row in self.str_rows]
        header_str = ", ".join(self.header)
        return "Dataset:\n"+header_str+"\n"+"\n".join(rows_str)

    def numerize(self):
        # self.ordinal_values
        # ordinal = self.column(2)
        d = self.copy()
        for i in range(d.n):
            v = d.rows[i][2]
            d.rows[i][2] = self.ordinal_values.index(v) + 1

        return d


class DataQuestion(Question):
    def __init__(self, d: Dataset,points:int=1):
        super().__init__(points=points)
        self.d = d

class DataFrameQuestion(Question):
    def __init__(self, d: pd.DataFrame,points:int=1):
        super().__init__(points=points)
        self.d = d

from .markdown import *

class DisplayTable(Renderable):
    def __init__(self,d:Dataset):
        self.d=d
    def render(self, seed=None):
        title=Text("**Tabla de datos**")
        t=Table(self.d.str_rows,header=self.d.header,row_header="numbers")
        p=Paragraphs([title,t])
        return p.render()
    
import matplotlib.pyplot as plt
import tempfile

from pathlib import Path

temp_dir = Path("temp")

class MatplotlibFigure(Renderable):
    
    temp_dir.mkdir(exist_ok=True,parents=True)
    temp_dir = temp_dir

    def __init__(self,figure,alt="",title=""):
        super().__init__()
        self.alt=alt
        self.title=title
        self.figure=figure
        self.path= temp_dir / f"{self.id}.png"
        print(f"Saving image to {self.path}")
        figure.savefig(self.path)
        plt.close(figure)
    def render(self,seed=None):
        return f"![{self.alt}]({self.path} \"{self.title}\")"
