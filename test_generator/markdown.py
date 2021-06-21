
import abc


class Renderable(abc.ABC):

    @abc.abstractmethod
    def render(self)->str:
        pass


class Table(Renderable):
    def __init__(self,data,header=None,number_rows=False):
        self.data=data
        self.header=header
        self.number_rows=number_rows

    def render(self):
        header=self.header
        data=self.data
        if len(data)==0 and header is None:
            return ""
        if len(data)>0:
            columns=len(data[0])
        else:
            columns=len(header)
        if self.number_rows:
            columns+=1

        table="\n"
        if not header is None:
            if self.number_rows:
                header=["Fila"]+header
            table+=self.render_row(header)+"\n"
        table+=self.render_header_separator(columns)+"\n"
        for i,row in enumerate(data):
            if self.number_rows:
                row=[f"{i+1}"]+row
            table+=self.render_row(row)+"\n"
        return table

    def render_header_separator(self,columns:int)->str:
        row = ["----------" for i in range(columns)]
        return self.render_row(row)

    def render_row(self,row:[str])->str:
        middle="|".join([str(a) for a in row])
        return f"|{middle}|"

    def __repr__(self):
        return f"Table({self.header},rows={len(self.data)})"

class Text(Renderable):
    def __init__(self,text):
        self.text=text
    def render(self):
        return self.text
    def __repr__(self):
        return f"Text({self.text})"

class Paragraphs(Renderable):
    def __init__(self,items:[Renderable],separator="\n\n"):
        assert(isinstance(items,list))
        self.items=items
        self.separator=separator

    def render(self):
        return self.separator.join([item.render() for item in self.items])

    def __repr__(self):
        return f"Paragraphs(items={len(self.items)})"
        
class Sections(Renderable):
    def __init__(self,titles:[str],bodies:[Renderable],depth=2):
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
        self.body=body
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

