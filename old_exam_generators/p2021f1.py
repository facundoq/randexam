from tqdm import tqdm
import questions
from test_generator import *
from random import seed,randrange
from questions import preprocessing


# Incluir cuentas en clustering



from pathlib import Path
import numpy as np



def engines_dataset( n=8):
    attributes = ["Velocidad", "Cilindros", "Antigüedad"]
    header = attributes + ["Clase"]
    class_values = ["Deportivo", "Utilitario"]
    skill_values = ["Baja", "Media", "Alta"]

    def random_person():
        cilindros = randrange(2, 16)
        velocidad = int(np.random.normal(loc=150, scale=15))

        antiguedad = skill_values[randrange(len(skill_values))]
        klass = class_values[randrange(len(class_values))]

        return [velocidad, cilindros, antiguedad, klass]

    rows = [random_person() for i in range(n)]

    d = Dataset(rows, header, attributes, class_values, skill_values)
    # ensure all values appear at least once
    for i, values in [(2, skill_values), (3, class_values)]:
        col = d.column(i)
        missing_values = []
        for val in values:
            if not val in col:
                missing_values.append(val)
        for j, v in enumerate(missing_values):
            d.rows[j][i] = v
    return d

def parcial1():
    
    d=engines_dataset(n=8)
    d_numerized=d.numerize()
    d_discretized=d.discretize(0, ["Baja","Media","Alta"], preprocessing.Discretization.frequency)
    d_discretized=d_discretized.discretize(1, ["Pocos","Muchos"], preprocessing.Discretization.frequency)

    question_list=[
                questions.Discretization(d,attribute_index=0,values=4),
                questions.Normalization(d,attribute_index=1,meanstd=False),
                questions.rule_metrics.RuleMetrics(d),
                questions.OneRQuestion(d_discretized),
                questions.numerization.Numerization(d,d_numerized,attribute_index=2),
                questions.clustering.ClusteringAssignments(d_numerized),
                questions.clustering.ClusteringEvaluationQuestions2(),
                questions.correlation.CorrelationMatrix3(d_numerized),
                questions.concepts.Concepts2(),
                # questions.InformationGain(d, numeric_attribute=1,nominal_attribute=2,class_index=3),
                # questions.Perceptron(d_numerized),
                # questions.TrueOrFalse(),
                # questions.RandomQuestions(),
                ]
    intro=DisplayTable(d)
    exam=Exam("Minería de Datos usando Sistemas Inteligentes",intro,question_list,
    subtitle="Primera Fecha - 17 de Junio de 2021 - Promoción",geometry="margin=2cm")
    return exam

if __name__ == "__main__":
    seed(1)
    np.random.seed(1)
    n_exams=50
    folderpath=Path("p2021/p1")
    for i in tqdm(range(n_exams)):
        exam=parcial1()
        filename = f"exam{i+1:02d}"
        generate_and_save(exam,folderpath,filename,pdf=True)

