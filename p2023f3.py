from tqdm import tqdm
import questions
from test_generator import *
from random import randrange
import random

# TODO: Incluir cuentas en clustering


from pathlib import Path
import numpy as np
from questions import Boxplot

from questions.naive_bayes.model import NaiveBayes,CategoricalVariable,GaussianVariable,NaiveBayesSingleClass

import pandas as pd

def fruit_models():
    class_names = np.array(["Ma","Pe"])
    columns = ["Color","Esfericidad"]

    color_manzana = CategoricalVariable({"Amarillo":0.8,"Mezcla":0.0,"Rojo":0.2})
    esfericidad_manzana = GaussianVariable(0.5,0.3)
    manzana = NaiveBayesSingleClass(dict(zip(columns,[color_manzana,esfericidad_manzana])))

    color_pera = CategoricalVariable({"Amarillo":0.1,"Mezcla":0.6,"Rojo":0.3})
    esfericidad_pera = GaussianVariable(0.8,0.2)
    pera = NaiveBayesSingleClass(dict(zip(columns,[color_pera,esfericidad_pera])))

    class_probabilities1 = CategoricalVariable(dict(zip(class_names,[0.5,0.5])))
    model1 = NaiveBayes(class_names,[manzana,pera],class_probabilities1)

    class_probabilities2 = CategoricalVariable(dict(zip(class_names,[0.01,0.99])))
    model2 = NaiveBayes(class_names,[manzana,pera],class_probabilities2)
    df = pd.DataFrame([["Amarillo",0.6],["Mezcla",0.8]],columns=columns)
    return model1,model2,df

def ejercicio(id:int):
    
    fruta_model1,fruta_model2,fruta_df = fruit_models()

    def estrellas(filepath):
        d = pd.read_excel(Path(filepath))
        y = d["Clase Espectral"].to_numpy()
        x = d.iloc[:,:3]
        model = NaiveBayes.fit(x,y)
        return x,y,model
    
    x1,y1,estrellas_model1 = estrellas("data/estrellas_p3.xlsx")
    x2,y2,estrellas_model2 = estrellas("data/estrellas_p3_d.xlsx")
    question_list=[
                questions.naivebayes.ApplyNaiveBayes(fruta_model1,fruta_df),
                questions.naivebayes.ApplyNaiveBayes(fruta_model2,fruta_df),
                questions.naivebayes.GenerateNaiveBayes(x1,y1),
                questions.naivebayes.ApplyNaiveBayes(estrellas_model1,x1),
                questions.naivebayes.GenerateNaiveBayes(x2,y2),
                questions.naivebayes.ApplyNaiveBayes(estrellas_model2,x2),
                
                
 
                ]
    intro=[""]
    exam=Exam(f"Minería de Datos usando Sistemas Inteligentes",intro,question_list,
    subtitle=f" Practica 3 - 2023\n",geometry="margin=1.8cm",show_points=False,questions_in_answers=True)
    return exam

if __name__ == "__main__":
    seed = 2
    random.seed(seed)
    np.random.seed(seed)
    n_exams=1
    folderpath=Path("assignments/")
    for i in tqdm(range(n_exams)):
        exam=ejercicio(0)
        filename = f"p3"
        generate_and_save(exam,folderpath,filename,format="pdf",delete_md=False)

