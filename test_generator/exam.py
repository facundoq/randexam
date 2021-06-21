import abc
from .markdown import Sections,Document,Renderable, Paragraphs,Text
from pathlib import Path
import pypandoc
import string

class Question(abc.ABC):
    @abc.abstractmethod
    def generate(self,seed:int=None)->(Renderable,Renderable):
        pass

    @abc.abstractmethod
    def title(self)->str:
        pass

    def points(self)->str:
        return 1

class QA:
    def __init__(self,q:str,a:str):
        self.q=q
        self.a=a
def to_enumeration(a: [str]):
        items = string.ascii_lowercase
        if len(a)> len(items):
            raise ValueError(f"Not enough item ids for the enumeration (max {len(items)})")

        a = [f"{items[i]}) {x}" for i, x in enumerate(a)]
        return "\n\n".join(a)

class QAQuestion(Question):
    def __init__(self,title_str:str,instructions:str,qas:[QA]):
        super().__init__()
        self.instructions=instructions
        self.title_str=title_str
        self.qas=qas

    def generate(self,seed:int=None) ->(Renderable,Renderable):
        questions = to_enumeration([qa.q for qa in self.qas])
        enunciado = Text(self.instructions)
        q = Paragraphs([enunciado, Text(questions)])
        answers = to_enumeration([qa.a for qa in self.qas])
        return q, Text(answers)

    def title(self) ->str:
        return self.title_str

class MultipleQuestions(Question):
    def __init__(self,title_str:str,instructions:str,questions:[str],answers:[str]):
        super().__init__()
        nq,na=len(questions),len(answers)
        assert nq==na, f"The number of questions ({nq}) must match the number of answers ({na})."
        self.instructions=instructions
        self.questions=questions
        self.answers=answers
        self.title_str=title_str

    def generate(self,seed:int=None) ->(Renderable,Renderable):


        questions = to_enumeration(self.questions)
        enunciado = Text(self.instructions)
        q = Paragraphs([enunciado, Text(questions)])
        answers = to_enumeration(self.answers)
        return q, Text(answers)

    def title(self) ->str:
        return self.title_str

class Exam:
    def __init__(self,title:str,intro:Renderable,questions:[Question],subtitle=None,date=None,geometry=None):
        self.intro=intro
        self.title=title
        self.questions=questions
        self.subtitle=subtitle
        self.date=date
        self.geometry=geometry
        

    def generate_exam(self,intro:Renderable,titles:[str],section_bodies:[Renderable],points:[int]=None)->Renderable:
        depth=3
        
        if not points is None:
            titles=[f"{t} (puntos: {p})" for t,p in zip(titles,points)]
        s=Sections(titles,section_bodies,depth=depth)
        body=Paragraphs([intro,s])
        d=Document(self.title,body,subtitle=self.subtitle,date=self.date,geometry=self.geometry)
        return d

    def generate(self,seed:int=None)->(Renderable,Renderable):
        qa=[q.generate() for q in self.questions]
        points=[q.points() for q in self.questions]
        questions,answers= zip(*qa)
        titles=[q.title() for q in self.questions]
        question_sheet=self.generate_exam(self.intro,titles,questions)
        answer_sheet=self.generate_exam(self.intro,titles,answers,points=points)
        return question_sheet,answer_sheet


def generate_and_save(exam: Exam, base_folderpath: Path, filename: str, pdf=False):
    tags = ["questions", "answers"]
    q, a = exam.generate()
    for version, tag in zip((q, a), tags):
        folderpath = base_folderpath / tag
        folderpath.mkdir(exist_ok=True, parents=True)
        md_name = f"{filename}_{tag}.md"
        pdf_name = f"{filename}_{tag}.pdf"
        filepath = folderpath / md_name
        md = version.render()
        with open(filepath, "w") as f:
            print(md, file=f)
        if pdf:
            pypandoc.convert_file(str(filepath), 'pdf', outputfile=str(folderpath / pdf_name))



