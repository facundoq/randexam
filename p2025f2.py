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

def mallin(n=8):
    description = "El siguiente conjunto de datos tiene datos clínicos de personas que tuvieron COVID, incluyendo la cantidad de contactos estrechos, edad y presión de las personas, y si las mismas tuvieron compĺicaciones (CC) o no (SC)."
    attributes = ["Estrechos",  "Edad","Presión"]
    header = attributes + ["Clase"]
    class_values = ["SC", "CC"]
    presion_values = ["Baja", "Media", "Alta"]

    def random_example():
        nvdi = min(5,max(0,int(np.random.normal(loc=3, scale=1))))
        edad = randrange(0,80)
        presion = presion_values[randrange(len(presion_values))]
        klass = class_values[randrange(len(class_values))]

        return [nvdi, edad, presion, klass]

    rows = [random_example() for i in range(n)]

    d = Dataset(rows, header, attributes, class_values, presion_values)
    # ensure all values appear at least once
    for i, values in [(2, presion_values), (3, class_values)]:
        col = d.column(i)
        missing_values = []
        for val in values:
            if not val in col:
                missing_values.append(val)
        for j, v in enumerate(missing_values):
            d.rows[j][i] = v
    return d,description

def parcial(id:int,fecha,year):
    
    d,description=mallin(n=8)
    d_numerized=d.numerize()
    d_numerized_unsupervised = d_numerized.copy()
    d_numerized_unsupervised.delete_column(3)
    
    values2=["Pocos","Muchos"]
    d_discretized=d.discretize(0, values2, preprocessing.Discretization.frequency)

    values3=["Joven","Mediana","Adulta"]
    d_discretized=d_discretized.discretize(1, values3, preprocessing.Discretization.frequency)

    question_list=[
                # questions.normalization.Normalization(d,1,interpret_sample=3,include_parameters=True),
                # questions.discretization.Discretization(d,1,values3),
                questions.oner.OneRQuestion(d_discretized,points=1),
                questions.rule_metrics.RuleMetrics(d),
                questions.clustering.ClusteringAssignments(d_numerized,3,include_dataset=True,points=1.5),
                questions.clustering.ClusteringCentroids(d_numerized_unsupervised,2,4,include_dataset=True,points=1),
                questions.concepts.ConceptsSubset([12,17,28,49,42],points=2),
                questions.info_gain.InformationGain(d,numeric_attributes=0  ,nominal_attributes=2,class_index=3,points=2,log_base=2,include_table=True),
                questions.perceptron.Perceptron(d_numerized,class_column=3,points=1.5),
                questions.quantiles.Quantiles(d,0),
                ]
    
    space="&nbsp;"*12
    header = [f"Nombres","Apellidos","DNI/N° Legajo","#Hojas extra"]
    header = [h+space for h in header]
    t=Table([["","","",""]],header=header,row_header=None)

    
    intro=Paragraphs([t,description,DisplayTable(d)])
    exam=Exam(f"Minería de Datos usando Sistemas Inteligentes - Tema {id}",intro,question_list,
    subtitle=f" Fecha {fecha} - 18 de Junio de {year} \n",geometry="margin=1.6cm",show_points=False)
    return exam



if __name__ == "__main__":

    fecha = 2
    year = 2025
    n_exams=1
    folderpath=Path(f"exams/{year}_f{fecha}")
    for i in tqdm(range(n_exams)):
        exam=parcial(i+3,fecha,year)
        filename = f"exam{i+1:02d}"
        generate_and_save(exam,folderpath,filename,delete_md=False,format="pdf")

