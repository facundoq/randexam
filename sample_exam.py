
from test_generator.markdown import Text,Paragraphs,Table
from test_generator.exam import Exam,Question,generate_and_save
from random import randrange

class SimpleQuestion(Question):
    def _generate(self, seed=None):
        header=["Chorizos","Mortadelas","Cúrcuma"]
        def rs():
            return str(randrange(10))
        rows = [[rs(),rs(),rs()] for i in range(5)]
        t=Table(rows,header=header)
        q=Paragraphs([Text("¿Qué comiste ayer a la noche?"),t])
        a=Text("Un salvavidas")
        return q,a
    def title(self):
        return "Una Pregunta Inconveniente"


from pathlib import Path
if __name__ == "__main__":
    exam=Exam("Un examen muy difícil",[SimpleQuestion() for i in range(5)])
    q,a=exam.generate()
    print(q.render())
    print(a.render())
    folderpath=Path("sample_exam")
    generate_and_save(exam,folderpath,n=2,pdf=True)

