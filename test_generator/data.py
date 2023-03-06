from .exam import Question
from questions import preprocessing
import copy

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
        # rows = df.to_string(header=False,
        #           index=False,
        #           index_names=False).split('\n')
        # rows = [row.strip().split(" ") for row in rows]
        return Dataset(rows,header,attributes,class_values)

    def __init__(self, rows, header: [str], attributes: [str], class_values: [str], ordinal_values=None):
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
        n_intervals = len(new_values)
        d = self.copy()
        values = d.column(col)
        intervals, values = preprocessing.discretize(values, n_intervals, strategy)

        values = [new_values[i] for i in values]
        d.replace_column(col, values)
        return d

    def replace_column(self, col, values):
        for r, v in zip(self.rows, values):
            r[col] = v

    def copy(self):
        rows = copy.deepcopy(self.rows)
        header = copy.deepcopy(self.header)
        attributes = copy.deepcopy(self.attributes)
        class_values = copy.deepcopy(self.class_values)
        return Dataset(rows, header, attributes, class_values, self.ordinal_values)
    
    def __repr__(self) -> str:
        rows_str = [", ".join(map(str,row)) for row in self.str_rows]
        return "Dataset:\n"+self.header+"\n"+"\n".join(rows_str)
    # @classmethod
    # def people(cls, n=8):
    #     attributes = ["Edad", "Altura", "Habilidad"]
    #     header = attributes + ["Clase"]
    #     class_values = ["Si", "No"]
    #     skill_values = ["Baja", "Media", "Alta"]
    #
    #     def random_person():
    #         age = randrange(15, 20)
    #         height = int(np.random.normal(loc=170, scale=20))
    #
    #         skill = skill_values[randrange(len(skill_values))]
    #         klass = class_values[randrange(len(class_values))]
    #         return [age, height, skill, klass]
    #
    #     rows = [random_person() for i in range(n)]
    #
    #     d = Dataset(rows, header, attributes, class_values, skill_values)
    #     # ensure all values appear at least once
    #     for i, values in [(2, skill_values), (3, class_values)]:
    #         col = d.column(i)
    #         missing_values = []
    #         for val in values:
    #             if not val in col:
    #                 missing_values.append(val)
    #         for j, v in enumerate(missing_values):
    #             d.rows[j][i] = v
    #     return d

    def numerize(self):
        # self.ordinal_values
        # ordinal = self.column(2)
        rows = [row.copy() for row in self.rows]
        for i in range(len(rows)):
            v = rows[i][2]
            rows[i][2] = self.ordinal_values.index(v) + 1

        return Dataset(rows, self.header, self.attributes, self.class_values)


class DataQuestion(Question):
    def __init__(self, d: Dataset):
        self.d = d


from .markdown import *

class DisplayTable(Renderable):
    def __init__(self,d:Dataset):
        self.d=d
    def render(self, seed=None):
        title=Text("**Tabla de datos**")
        t=Table(self.d.str_rows,header=self.d.header,number_rows=True)
        p=Paragraphs([title,t])
        return p.render()