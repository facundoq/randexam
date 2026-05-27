from randexam.markdown import Text, Paragraphs, Table
from randexam.exam import Exam, Question, generate_and_save
from random import randrange
from pathlib import Path
import tempfile

class SimpleQuestion(Question):
    def _generate(self, seed=None):
        header = ["Health", "Defense", "Attack"]
        n, m = 5, len(header)

        def rs():
            return randrange(10)

        rows = [[rs() for h in header] for i in range(n)]
        t = Table(rows, header=header)
        q = Paragraphs([Text("Compute the mean of each column."), t])
        means = []
        for i in range(m):
            column = [row[i] for row in rows]
            means.append(sum(column) / m)
        t_a = Table([means], header=header)
        a = ["Result:", t_a]
        return q, a

    def title(self):
        return "A Very Interesting Question"

def test_simple_question():
    q, a = SimpleQuestion()._generate()
    assert q.render()

def assert_generation(exam:Exam):
    q, a = exam.generate()
    print(q.render())
    print(a.render())
    folderpath = Path(tempfile.gettempdir())
    filename = "test_exam.pdf"
    generate_and_save(exam, folderpath, filename, format="pdf")
    filepath = folderpath/"questions"/filename
    assert  folderpath.exists()

def test_empty_exam():
    exam = Exam(
        "A Very Hard Exam",
        "This exam is very difficult",
        []
    )
    assert_generation(exam)

def test_exam_with_question():
    exam = Exam(
        "A Very Hard Exam",
        "This exam is very difficult",
        [SimpleQuestion() for i in range(5)],
    )
    assert_generation(exam)
    

