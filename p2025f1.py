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
    description = "El siguiente conjunto de datos detalla estadísticas de mallines, que son humedales de la patagonia, y si los mismos son aptos para la pastura de ovejas. El atributo NDVI es el Normalized Difference Vegetation Index o Índice Normalizado de Diferencia de Vegetación."
    attributes = ["NVDI",  "Temperatura","Salinidad"]
    header = attributes + ["Clase"]
    class_values = ["Apto", "No Apto"]
    salinidad_values = ["Baja", "Media", "Alta"]

    def random_example():
        nvdi = min(1,max(-1,int(np.random.normal(loc=0, scale=1))))
        temperatura = randrange(-20,20)
        salinidad = salinidad_values[randrange(len(salinidad_values))]
        klass = class_values[randrange(len(class_values))]

        return [nvdi, temperatura, salinidad, klass]

    rows = [random_example() for i in range(n)]

    d = Dataset(rows, header, attributes, class_values, salinidad_values)
    # ensure all values appear at least once
    for i, values in [(2, salinidad_values), (3, class_values)]:
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

    values3=["Poco","Medio","Alto"]
    d_discretized=d_discretized.discretize(1, values3, preprocessing.Discretization.frequency)

    question_list=[
                questions.normalization.Normalization(d,1,interpret_sample=3,include_parameters=True),
                questions.discretization.Discretization(d,1,values3),
                questions.oner.OneRQuestion(d_discretized,points=1),
                #questions.quantiles.Quantiles(d,0),
                questions.rule_metrics.RuleMetrics(d),
                questions.clustering.ClusteringAssignments(d_numerized,3,include_dataset=True,points=1.5),
                questions.clustering.ClusteringCentroids(d_numerized_unsupervised,2,4,include_dataset=True,points=1),
                questions.concepts.ConceptsSubset([11,16,27,50,41],points=2),
                questions.info_gain.InformationGain(d,numeric_attributes=0  ,nominal_attributes=2,class_index=3,points=2,log_base=2,include_table=True),
                #questions.perceptron.Perceptron(d_numerized,class_column=3,points=1.5),
                ]
    
    space="&nbsp;"*12
    header = [f"Nombres","Apellidos","DNI/N° Legajo","#Hojas"]
    header = [h+space for h in header]
    t=Table([["","","",""]],header=header,row_header=None)

    
    intro=Paragraphs([t,description,DisplayTable(d)])
    exam=Exam(f"Minería de Datos usando Sistemas Inteligentes - Tema {id}",intro,question_list,
    subtitle=f" Fecha {fecha} - 26 de Junio de {year} \n",geometry="margin=1.6cm",show_points=False)
    return exam



if __name__ == "__main__":

    fecha = 1
    year = 2025
    n_exams=1
    folderpath=Path(f"exams/{year}_f{fecha}")
    for i in tqdm(range(n_exams)):
        exam=parcial(i+3,fecha,year)
        filename = f"exam{i+1:02d}"
        generate_and_save(exam,folderpath,filename,delete_md=False,format="pdf")

