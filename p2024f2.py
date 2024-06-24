from tqdm import tqdm
from pathlib import Path

import random
import numpy as np
# random seed fixing
seed = 4
random.seed(seed)
np.random.seed(seed)
from test_generator import *
exam.random_seed = seed
import questions
questions.random_seed = seed

from random import randrange



def tumores(n=8):
    attributes = ["Tamaño", "Anticuerpos", "Síntomas"]
    header = attributes + ["Clase"]
    class_values = ["Benigno", "Maligno"]
    sintomas_values = ["Ninguno", "Leves", "Graves"]

    def random_example():
        p = np.random.rand()
        if p>0.4: 
            tamanio = max(10,int(np.random.normal(loc=30, scale=5)))
        elif p>0.1:
            tamanio = max(10,int(np.random.normal(loc=15, scale=1.5)))
        else:
            tamanio = max(10,int(np.random.normal(loc=110, scale=30)))

        tamanio = max(1,int(np.random.normal(loc=3, scale=1)))
        anticuerpos = randrange(10, 100)
        sintomas = sintomas_values[randrange(len(sintomas_values))]
        klass = class_values[randrange(len(class_values))]

        return [tamanio, anticuerpos, sintomas, klass]

    rows = [random_example() for i in range(n)]

    d = Dataset(rows, header, attributes, class_values, sintomas_values)
    # ensure all values appear at least once
    for i, values in [(2, sintomas_values), (3, class_values)]:
        col = d.column(i)
        missing_values = []
        for val in values:
            if not val in col:
                missing_values.append(val)
        for j, v in enumerate(missing_values):
            d.rows[j][i] = v
    return d

def parcial(id:int,fecha,year):
    
    d=tumores(n=8)
    d_numerized=d.numerize()
    d_numerized_unsupervised = d_numerized.copy()
    d_numerized_unsupervised.delete_column(3)
    values3=["Negativo","Leve","Alto"]
    values2=["Bajo","Alto"]

    d_discretized=d.discretize(0, values2, preprocessing.Discretization.frequency)
    d_discretized=d_discretized.discretize(1, values3, preprocessing.Discretization.frequency)

    question_list=[
                #questions.normalization.Normalization(d,0,interpret_sample=3),
                questions.discretization.Discretization(d,1,values3),
                questions.oner.OneRQuestion(d_discretized,points=1),
                #questions.quantiles.Quantiles(d,0),
                questions.rule_metrics.RuleMetrics(d),
                #questions.clustering.ClusteringAssignments(d_numerized,3,include_dataset=True,points=1.5),
                questions.clustering.ClusteringCentroids(d_numerized_unsupervised,2,4,include_dataset=True,points=1),
                questions.concepts.ConceptsSubset([3,12,17,18],points=2),
                questions.info_gain.InformationGain(d,numeric_attributes=0  ,nominal_attributes=2,class_index=3,points=2,log_base=2,include_table=True),
                questions.perceptron.Perceptron(d_numerized,class_column=3,points=1.5),
                ]
    
    space="&nbsp;"*12
    header = [f"Nombres","Apellidos","DNI/N° Legajo","#Hojas"]
    header = [h+space for h in header]
    t=Table([["","","",""]],header=header,row_header=None)

    
    intro=Paragraphs([t,DisplayTable(d)])
    exam=Exam(f"Minería de Datos usando Sistemas Inteligentes - Tema {id}",intro,question_list,
    subtitle=f" Fecha {fecha} - 28 de Junio de {year} \n",geometry="margin=1.6cm",show_points=False)
    return exam



if __name__ == "__main__":

    fecha = 2
    year = 2024
    n_exams=1
    folderpath=Path(f"exams/{year}_f{fecha}")
    for i in tqdm(range(n_exams)):
        exam=parcial(i+1+1,fecha,year)
        filename = f"exam{i+1:02d}"
        generate_and_save(exam,folderpath,filename,delete_md=False,format="pdf")

