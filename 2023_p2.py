from tqdm import tqdm
import questions
from test_generator import *
from random import randrange
import random

# TODO: Incluir cuentas en clustering


from pathlib import Path
import numpy as np
from questions import Boxplot


import pandas as pd
def parcial(id:int):
    
    
    d2 = pd.read_csv(Path("data/clustering.csv"))
    c1 = pd.read_csv(Path("data/clustering_c1.csv"))
    c2 = pd.read_csv(Path("data/clustering_c2.csv"))
    c3 = pd.read_csv(Path("data/clustering_c3.csv"))
    
    question_list=[
                questions.clustering_generic.ClusteringGeneric(d2,c1,n_steps=3,include_dataset=True),
                questions.clustering_generic.ClusteringGeneric(d2,c2,n_steps=3,include_dataset=True),
                questions.clustering_generic.ClusteringGeneric(d2,c3,n_steps=3,include_dataset=True),
                ]
    required_data = f"""
**Datos personales**

 * Nombres:
 * Apellidos:
 * DNI / Nº Legajo:
 * Cantidad de hojas entregadas:

"""
    intro=[""]
    exam=Exam(f"Minería de Datos usando Sistemas Inteligentes",intro,question_list,
    subtitle=f" Practica 2 - 2023\n",geometry="margin=1.8cm",show_points=False,questions_in_answers=True)
    return exam

if __name__ == "__main__":
    seed = 2
    random.seed(seed)
    np.random.seed(seed)
    n_exams=1
    folderpath=Path("2023")
    for i in tqdm(range(n_exams)):
        exam=parcial(i+1+1)
        filename = f"exam{i+1:02d}"
        generate_and_save(exam,folderpath,filename,pdf=True,delete_md=True)

