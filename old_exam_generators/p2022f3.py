from tqdm import tqdm
import questions
from test_generator import *
from random import randrange
from questions import preprocessing
import random

# TODO: Incluir cuentas en clustering


from pathlib import Path
import numpy as np



def enfermedad(n=8):
    attributes = ["Edad", "Tiempo tratamiento", "Síntomas"]
    header = attributes + ["Clase"]
    class_values = ["Con enfermedad", "Sin enfermedad"]
    skill_values = ["Bajos", "Medios", "Altos"]

    def random_example():
        edad = int(np.random.normal(loc=50, scale=12))
        tiempo_tratamiento = randrange(1, 10)
        sintomas = skill_values[randrange(len(skill_values))]
        klass = class_values[randrange(len(class_values))]

        return [edad, tiempo_tratamiento, sintomas, klass]

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
    
    d=enfermedad(n=8)
    d_numerized=d.numerize()
    d_discretized=d.discretize(0, ["Baja","Media","Alta"], preprocessing.Discretization.frequency)
    d_discretized=d_discretized.discretize(1, ["Corto","Largo"], preprocessing.Discretization.frequency)

    question_list=[
                #questions.discretization.Discretization(d,0,2),
                questions.normalization.Normalization(d,0),
                questions.oner.OneRQuestion(d_discretized),
                questions.rule_metrics.RuleMetrics(d),
                questions.clustering.ClusteringAssignments(d_numerized,include_dataset=True),
                questions.correlation.CorrelationMatrixJugador(d),
                questions.concepts.Concepts2(),
                questions.info_gain.InformationGain(d, numeric_attribute=1,nominal_attribute=2,class_index=3),
                ]
    required_data = f"""
**Datos personales**

 * Nombres:
 * Apellidos:
 * DNI / Nº Legajo:
 * Cantidad de hojas entregadas:

"""
    intro=Paragraphs([Text(required_data),DisplayTable(d)])
    exam=Exam(f"Minería de Datos usando Sistemas Inteligentes - Tema {id}",intro,question_list,
    subtitle=f" Tercera Fecha - 13 de Julio de 2022\n",geometry="margin=1.8cm",show_points=False)
    return exam

if __name__ == "__main__":
    seed = 2
    random.seed(seed)
    np.random.seed(seed)
    n_exams=1
    folderpath=Path("p2022/f3")
    for i in tqdm(range(n_exams)):
        exam=parcial(i+1+1)
        filename = f"exam{i+1:02d}"
        generate_and_save(exam,folderpath,filename,pdf=True,delete_md=True)

