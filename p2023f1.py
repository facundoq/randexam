from tqdm import tqdm
import questions
from test_generator import *
from random import randrange
from questions import preprocessing
import random

# TODO: Incluir cuentas en clustering


from pathlib import Path
import numpy as np



def cerveza(n=8):
    attributes = ["Visión ", "Dolor", "Diabetes"]
    header = attributes + ["Clase"]
    class_values = ["Normal", "Retinopatía"]
    skill_values = ["Tipo 1", "Tipo 2", "Gestacional"]

    def random_example():
        vision = int(np.random.normal(loc=50, scale=12))
        dolor = randrange(1, 10)
        diabetes = skill_values[randrange(len(skill_values))]
        klass = class_values[randrange(len(class_values))]

        return [vision, dolor, diabetes, klass]

    rows = [random_example() for i in range(n)]

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

def parcial(id:int):
    
    d=cerveza(n=8)
    d_numerized=d.numerize()
    d_numerized.delete_column(3)
    values=["Bajo","Alto"]
    d_discretized=d.discretize(0, ["Bajo","Medio","Alto"], preprocessing.Discretization.frequency)
    d_discretized=d_discretized.discretize(1, ["Leve","Grave"], preprocessing.Discretization.frequency)

    question_list=[
                questions.discretization.Discretization(d,0,values),
                questions.oner.OneRQuestion(d_discretized,points=1),
                questions.rule_metrics.RuleMetrics(d),
                questions.clustering.ClusteringAssignments(d_numerized,3,include_dataset=True,points=1.5),
                questions.clustering.ClusteringCentroids(d_numerized,2,4,include_dataset=True,points=1.5),
                questions.correlation.CorrelationMatrixFumar(d),
                questions.concepts.ConceptsRandom(8,2),
                questions.info_gain.InformationGain(d, numeric_attribute=1,nominal_attribute=2,class_index=3,points=1),
                ]
    
    space="&nbsp;"*12
    header = [f"Nombres","Apellidos","DNI/N° Legajo","#Hojas"]
    header = [h+space for h in header]
    t=Table([["","","",""]],header=header,row_header=None)


    intro=Paragraphs([t,DisplayTable(d)])
    exam=Exam(f"Minería de Datos usando Sistemas Inteligentes - Tema {id}",intro,question_list,
    subtitle=f" Primera Fecha - 9 de Junio de 2023 - Promoción\n",geometry="margin=1.6cm",show_points=True)
    return exam

if __name__ == "__main__":
    seed = 2
    questions.random_seed = 2
    random.seed(seed)
    np.random.seed(seed)
    
    n_exams=1
    folderpath=Path("p2023/f1")
    for i in tqdm(range(n_exams)):
        exam=parcial(i+1+1)
        filename = f"exam{i+1:02d}"
        generate_and_save(exam,folderpath,filename,delete_md=False,format="pdf")

