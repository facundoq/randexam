
import abc
from collections.abc import Iterable
import pandas as pd

import uuid
class Renderable(abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        self.id = uuid.uuid1()

    @abc.abstractmethod
    def render(self)->str:
        pass
    

    

class Table(Renderable):
    def __init__(self,data,header=None,row_header=None):
        self.data=data
        self.header=header
        self.row_header=row_header

    def render(self):
        header=self.header
        data=self.data
        row_header = self.row_header
        if row_header == "numbers":
            row_header = [f"{i+1}" for i in range(len(data))]        
        
        if len(data)==0 and header is None:
            return ""
        if len(data)>0:
            columns=len(data[0])
        else:
            columns=len(header)
        if not row_header is None:
            columns+=1
        
        table="\n"
        if header is None:
            header = [" "]*columns
        if not row_header is None:
                header=[" "]+header
        table+=self.render_row(header)+"\n"
        table+=self.render_header_separator(columns)+"\n"
        for i,row in enumerate(data):
            if not row_header is None:
                row=[row_header[i]]+row
            table+=self.render_row(row)+"\n"
        return table

    def render_header_separator(self,columns:int)->str:
        row = ["----------" for i in range(columns)]
        return self.render_row(row)

    def render_row(self,row:list[str])->str:
        middle="|".join([str(a) for a in row])
        return f"|{middle}|"

    def __repr__(self):
        return f"Table({self.header},rows={len(self.data)})"

class DisplayDataFrame(Renderable):
    def __init__(self,d:pd.DataFrame,title="**Datos**",row_header=None):
        self.d=d
        self.title=title
        self.row_header=row_header
    def render(self, seed=None):
        rows = self.d.to_numpy().tolist()
        t=Table(rows,header=self.d.columns.tolist(),row_header=self.row_header)
        p=Paragraphs([self.title,t])
        return p.render()
    
class Text(Renderable):
    def __init__(self,text):
        self.text=text
    def render(self):
        return self.text
    def __repr__(self):
        return f"Text({self.text})"

def make_renderable(x:object):
    if isinstance(x, Renderable):
        return x
    elif isinstance(x, str):
        return Text(x)
    elif isinstance(x,Iterable):
        return Paragraphs(x)
    elif isinstance(x,pd.DataFrame):
        return DisplayDataFrame(x)
    else:
        raise Exception(f"Rendering not supported for type {type(x)}, value {x}")

class Paragraphs(Renderable):
    def __init__(self,items:list[Renderable],separator="\n\n"):
        assert(isinstance(items,Iterable))
        items = [make_renderable(x) for x in items]
        self.items=items
        self.separator=separator

    def render(self):
        return self.separator.join([item.render() for item in self.items])

    def __repr__(self):
        return f"Paragraphs(items={len(self.items)})"
        
class Sections(Renderable):
    def __init__(self,titles:list[str],bodies:list[Renderable],depth=2):
        bodies = [make_renderable(x) for x in bodies]

        self.depth=depth
        self.titles=titles
        self.bodies=bodies
        

    def render(self)->str:
        dm="#"*self.depth
        sections=zip(self.titles,self.bodies)
    
        sections=[f"{dm} {i+1}. {title}\n {body.render()}" for i,(title,body) in enumerate(sections)]
        return "\n\n".join(sections)
    def __repr__(self):
        return f"Sections(items={len(self.titles)})"

class Document(Renderable):
    def __init__(self,title:str, body:Renderable,subtitle:str=None,date:str=None,geometry:str=None):
        self.title=title
        self.body=make_renderable(body)
        self.subtitle=subtitle
        self.date=date
        self.geometry=geometry
    
    # def render(self)->str:
    #     title=f"# {self.title}"
    #     if not self.subtitle is None:
    #         title+=f"\n## {self.subtitle}"
    #     return f"{title}\n\n{self.body.render()}"
    def render(self)->str:
        date= "" if self.date is None else self.date
        subtitle= "" if self.subtitle is None else self.subtitle
        fields=f"title: {self.title}\nauthor: {subtitle}\ndate: {date}\n"
        if not self.geometry is None:
            fields+=f"geometry: {self.geometry}\n"
        header=f"---\n{fields}---\n"


        return f"{header}\n{self.body.render()}"

    def __repr__(self):
        return f"Document({self.title})"

