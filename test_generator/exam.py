import abc
from .markdown import Sections,Document,Renderable, Paragraphs,Text
from pathlib import Path
import pypandoc
import string

RenderableQA = tuple[Renderable,Renderable]

class Question(abc.ABC):
    def __init__(self,points=1) -> None:
        super().__init__()
        self._points=points

    @abc.abstractmethod
    def generate(self,seed:int=None)->RenderableQA:
        pass

    @abc.abstractmethod
    def title(self)->str:
        pass
    
    def points(self)->str:
        return self._points

class QA:
    def __init__(self,q:str,a:str):
        self.q=q
        self.a=a

def to_enumeration(a: list[str]):
        items = string.ascii_lowercase
        if len(a)> len(items):
            raise ValueError(f"Not enough item ids for the enumeration (max {len(items)})")

        a = [f"{items[i]}) {x}" for i, x in enumerate(a)]
        return "\n\n".join(a)

class QAQuestion(Question):
    def __init__(self,title_str:str,instructions:str,qas:list[QA],points:int):
        super().__init__(points=points)
        self.instructions=instructions
        self.title_str=title_str
        self.qas=qas
        

    def generate(self,seed:int=None) ->RenderableQA:
        questions = to_enumeration([qa.q for qa in self.qas])
        enunciado = Text(self.instructions)
        q = Paragraphs([enunciado, Text(questions)])
        answers = to_enumeration([qa.a for qa in self.qas])
        return q, Text(answers)
    
    def title(self) ->str:
        return self.title_str


class Exam:
    def __init__(self,title:str,intro:Renderable,questions:list[Question],subtitle=None,date=None,geometry=None, show_points = False,questions_in_answers = False):
        self.intro=intro
        self.title=title
        self.questions=questions
        self.subtitle=subtitle
        self.date=date
        self.geometry=geometry
        self.show_points = show_points
        self.questions_in_answers = questions_in_answers
        

    def generate_exam(self,title:str,intro:Renderable,titles:list[str],section_bodies:list[Renderable],points:list[int])->Renderable:
        depth=3

        s=Sections(titles,section_bodies,depth=depth)
        body=Paragraphs([intro,s])
        d=Document(title,body,subtitle=self.subtitle,date=self.date,geometry=self.geometry)
        return d

    def generate(self,seed:int=None)->RenderableQA:
        qa=[q.generate() for q in self.questions]
        points=[q.points() for q in self.questions]
        questions,answers= zip(*qa)
        if self.show_points:
            titles=[ f"{q.title()}\n **Puntaje:** \t &nbsp;&nbsp;&nbsp;    /{q.points()}\n" for q in self.questions]
            total_points = sum(points)
            point_form =f"**Puntaje total:** ___ /{total_points}"
            titles = titles
            intro_question = [point_form,self.intro]
        else:
            intro_question = self.intro
            titles=[q.title() for q in self.questions]
        titles_answer=[ f"{q.title()} (Puntos: {q.points()})" for q in self.questions]
        
        question_sheet=self.generate_exam(self.title,intro_question,titles,questions,points)
        if self.questions_in_answers:
            answers = [ ["**Pregunta**:",q,"**Respuesta**",a]  for q,a in qa]
            intro_answers = intro_question
        else:
            intro_answers = ""
        answer_sheet=self.generate_exam(self.title+" (Respuestas)",intro_answers,titles_answer,answers,points)
        return question_sheet,answer_sheet


def generate_and_save(exam: Exam, base_folderpath: Path, filename: str,delete_md=False,format="pdf"):
    tags = ["questions", "answers"]
    q, a = exam.generate()
    for version, tag in zip((q, a), tags):
        folderpath = base_folderpath / tag
        folderpath.mkdir(exist_ok=True, parents=True)
        md_name = f"{filename}_{tag}.md"
        pdf_name = f"{filename}_{tag}.{format}"
        md_filepath = folderpath / md_name
        md = version.render()
        with open(md_filepath, "w") as f:
            print(md, file=f)
        if not format is None:
            pypandoc.convert_file(str(md_filepath), format, outputfile=str(folderpath / pdf_name))
        if delete_md:
            Path(md_filepath).unlink()




