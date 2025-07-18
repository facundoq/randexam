
from src.markdown import Text,Paragraphs,Table
from src.exam import Exam,Question,generate_and_save
from random import randrange

class SimpleQuestion(Question):
    def _generate(self, seed=None):
        header=["Health","Defense","Attack"]
        n,m = 5, len(header)
        rs = lambda: randrange(10)
        rows = [[rs() for h in header] for i in range(n)]
        t=Table(rows,header=header)
        q=Paragraphs([Text("Compute the mean of each column."),t])
        means = []
        for i in range(m):
            column = [row[i] for row in rows]
            means.append(sum(column)/m)
        t_a=Table([means],header=header)
        a=["Result:",t_a]
        return q,a
    def title(self):
        return "A Very Interesting Question"


from pathlib import Path
if __name__ == "__main__":
    exam=Exam("A Very Hard Exam","This exam is very difficult", [SimpleQuestion() for i in range(5)])
    q,a=exam.generate()
    print(q.render())
    print(a.render())
    folderpath=Path("sample_exam")
    filename = "test.pdf"
    generate_and_save(exam,folderpath,filename,format="pdf")

