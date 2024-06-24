from tqdm import tqdm
import questions
from test_generator import *
from random import randrange
from questions import preprocessing
import random

# TODO: Incluir cuentas en clustering


from pathlib import Path
import numpy as np



def bebes(n=8):
    attributes = ["Edad", "Llanto", "Leche"]
    header = attributes + ["Clase"]
    class_values = ["Con Cólicos", "Sin Cólicos"]
    skill_values = ["Materna", "Mixta", "Fórmula"]

    def random_example():
        dias = int(np.random.normal(loc=50, scale=12))
        llanto = randrange(1, 10)
        leche = skill_values[randrange(len(skill_values))]
        klass = class_values[randrange(len(class_values))]

        return [dias, llanto, leche, klass]

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

def parcial(id:int,fecha,year):
    
    d=bebes(n=8)
    d_numerized=d.numerize()
    d_numerized_unsupervised = d_numerized.copy()
    d_numerized_unsupervised.delete_column(3)
    values=["Bajo","Alto"]
    d_discretized=d.discretize(0, ["Baja","Media","Alta"], preprocessing.Discretization.frequency)
    d_discretized=d_discretized.discretize(1, ["Leve","Grave"], preprocessing.Discretization.frequency)

    question_list=[
                questions.normalization.Normalization(d,0),
                questions.oner.OneRQuestion(d_discretized,points=1),
                questions.quantiles.Quantiles(d,0),
                questions.rule_metrics.RuleMetrics(d),
                # questions.clustering.ClusteringAssignments(d_numerized,3,include_dataset=True,points=1.5),
                questions.clustering.ClusteringCentroids(d_numerized_unsupervised,2,4,include_dataset=True,points=1),
                questions.concepts.ConceptsRandom(8,2),
                questions.info_gain.InformationGain(d, numeric_attributes=1,nominal_attributes=2,class_index=3,points=2),
                questions.perceptron.Perceptron(d_numerized,class_column=3),
                ]
    
    space="&nbsp;"*12
    header = [f"Nombres","Apellidos","DNI/N° Legajo","#Hojas"]
    header = [h+space for h in header]
    t=Table([["","","",""]],header=header,row_header=None)

    
    intro=Paragraphs([t,DisplayTable(d)])
    exam=Exam(f"Minería de Datos usando Sistemas Inteligentes - Tema {id}",intro,question_list,
    subtitle=f" Fecha {fecha} - 23 de Junio de {year} \n",geometry="margin=1.6cm",show_points=False)
    return exam



if __name__ == "__main__":
    seed = 3
    questions.random_seed = seed
    random.seed(seed)
    np.random.seed(seed)
    fecha = 2
    year = 2023
    n_exams=1
    folderpath=Path(f"p{year}/f{fecha}")
    for i in tqdm(range(n_exams)):
        exam=parcial(i+1+1,fecha,year)
        filename = f"exam{i+1:02d}"
        generate_and_save(exam,folderpath,filename,delete_md=False,format="pdf")

