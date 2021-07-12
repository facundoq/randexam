from tqdm import tqdm
import questions
from test_generator import *
from random import randrange
from questions import preprocessing
import random

# TODO: Incluir cuentas en clustering


from pathlib import Path
import numpy as np



def stars_dataset(n=8):
    attributes = ["Distancia", "Luminosidad", "Temperatura"]
    header = attributes + ["Clase"]
    class_values = ["Estrella", "Galaxia"]
    skill_values = ["Baja", "Media", "Alta"]

    def random_example():
        distancia = int(np.random.normal(loc=80, scale=12))
        luminosidad = randrange(5, 22)
        temperatura = skill_values[randrange(len(skill_values))]
        klass = class_values[randrange(len(class_values))]

        return [distancia, luminosidad, temperatura, klass]

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

def parcial1(id:int):
    
    d=stars_dataset(n=8)
    d_numerized=d.numerize()
    d_discretized=d.discretize(0, ["Baja","Media","Alta"], preprocessing.Discretization.frequency)
    d_discretized=d_discretized.discretize(1, ["Poca","Mucha"], preprocessing.Discretization.frequency)

    question_list=[
                # questions.correlation.CorrelationMatrix(d_numerized),
                questions.oner.OneRQuestion(d_discretized),
                questions.rule_metrics.RuleMetrics(d),
                questions.clustering.Clustering(d_numerized,include_dataset=True),
                questions.perceptron.Perceptron(d_numerized,class_column=3),
                questions.concepts.RandomQuestions(),
                questions.info_gain.InformationGain(d, numeric_attribute=1,nominal_attribute=2,class_index=3),
                ]
    required_data = f"""Incluir en la primer hoja:
    
 * Nombre
 * Apellido
 * DNI / Nº Legajo
 * Tema {id}
 * Fecha
                       
Incluir en cada carilla:

 * Nro de carilla / Total de carillas

Al enviar el examen, nombrar el archivo pdf como "Apellido, Nombre.pdf" 
"""
    intro=Paragraphs([Text(required_data),DisplayTable(d)])
    exam=Exam(f"Minería de Datos usando Sistemas Inteligentes - Tema {id}",intro,question_list,
    subtitle=f" Tercera Fecha - 15 de Julio de 2021 - Promoción",geometry="margin=2cm")
    return exam

if __name__ == "__main__":
    seed = 2
    random.seed(seed)
    np.random.seed(seed)
    n_exams=10
    folderpath=Path("p2021/p3")
    for i in tqdm(range(n_exams)):
        exam=parcial1(i+1)
        filename = f"exam{i+1:02d}"
        generate_and_save(exam,folderpath,filename,pdf=True,delete_md=True)

