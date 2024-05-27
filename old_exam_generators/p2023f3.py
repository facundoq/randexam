from tqdm import tqdm
import questions
from test_generator import *
from random import randrange
from questions import preprocessing
import random

from pathlib import Path
import numpy as np



def personajes(n=8):
    attributes = ["Vida", "Fuerza", "Habilidad Especial"]
    header = attributes + ["Clase"]
    class_values = ["Mítico", "Normal"]
    skill_values = ["Salto", "Rapidez", "Defensa"]

    def random_example():
        vida = int(np.random.normal(loc=40, scale=20))
        fuerza = randrange(1, 10)
        habilidad = skill_values[randrange(len(skill_values))]
        klass = class_values[randrange(len(class_values))]

        return [vida, fuerza, habilidad, klass]

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
    
    d=personajes(n=8)
    d_numerized=d.numerize()
    d_numerized_unsupervised = d_numerized.copy()
    d_numerized_unsupervised.delete_column(3)
    values=["Débil","Normal","Robusto"]
    d_discretized=d.discretize(0, ["Baja","Media","Alta"], preprocessing.Discretization.frequency)
    d_discretized=d_discretized.discretize(1, ["Leve","Grave"], preprocessing.Discretization.frequency)

    question_list=[
                questions.normalization.Normalization(d,0),
                questions.discretization.Discretization(d,0,values),
                questions.oner.OneRQuestion(d_discretized,points=1),
                questions.quantiles.Quantiles(d,0),
                questions.rule_metrics.RuleMetrics(d),
                questions.clustering.ClusteringAssignments(d_numerized,3,include_dataset=True,points=1.5),
                #questions.clustering.ClusteringCentroids(d_numerized_unsupervised,2,4,include_dataset=True,points=1),
                questions.concepts.ConceptsSubset([1,5,8,18,20,26,39,40],points=2),
                # questions.info_gain.InformationGain(d, numeric_attribute=1,nominal_attribute=2,class_index=3,points=2),
                questions.perceptron.Perceptron(d_numerized,class_column=3,points=1.5),
                ]
    
    space="&nbsp;"*12
    header = [f"Nombres","Apellidos","DNI/N° Legajo","#Hojas"]
    header = [h+space for h in header]
    t=Table([["","","",""]],header=header,row_header=None)

    
    intro=Paragraphs([t,DisplayTable(d)])
    exam=Exam(f"Minería de Datos usando Sistemas Inteligentes - Tema {id}",intro,question_list,
    subtitle=f" Fecha {fecha} - 7 de Julio de {year} \n",geometry="margin=1.6cm",show_points=False)
    return exam



if __name__ == "__main__":
    seed = 4
    questions.random_seed = seed
    random.seed(seed)
    np.random.seed(seed)
    fecha = 3
    year = 2023
    n_exams=1
    folderpath=Path(f"exams/{year}_f{fecha}")
    for i in tqdm(range(n_exams)):
        exam=parcial(i+1+1,fecha,year)
        filename = f"exam{i+1:02d}"
        generate_and_save(exam,folderpath,filename,delete_md=False,format="pdf")

