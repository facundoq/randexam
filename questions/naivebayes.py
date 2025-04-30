from test_generator import *

import pandas as pd
import numpy as np

from questions.naive_bayes.model import NaiveBayes

class GenerateNaiveBayes(DataFrameQuestion):
    def __init__(self,x:pd.DataFrame,y:np.ndarray):
        super().__init__(x)
        self.x=x
        self.y=y

    def _generate(self, seed=None):
        d = self.x.copy()
        d["Clase"]=self.y
        q = [f"Dado el conjunto de datos, generar un modelo de Naive Bayes sin corrección de Laplace.",
             DisplayDataFrame(d)]
        model = NaiveBayes.fit(self.x,self.y)
        y_pred = model.predict_classes(self.x)
        accuracy = np.mean(self.y==y_pred)
        a = [Table(model.table(),header=["NB",f"Accuracy {accuracy:.2f}"])]
        return q, a

    def title(self):
        return "Entrenar Clasificador Bayesiano"

from test_generator.utils import capture
class ApplyNaiveBayes(DataQuestion):
    def __init__(self,model:NaiveBayes,samples:pd.DataFrame):
        super().__init__(samples)
        self.model=model
        self.samples=samples
        
    def _generate(self, seed=None):

        q = [f"Dado el modelo de Naive Bayes siguiente, indicar la clase de los ejemplos de la tabla. Incluir todos los cálculos intermedios ",
             Table(self.model.table()),
             DisplayDataFrame(self.samples)
             ]
        prediction,details = self.model.predict(self.samples,debug=True)
        pred = self.model.predict_classes(self.samples)
        columns=[f"p(c={i})" for i in self.model.class_names]
        prediction_df = pd.DataFrame(prediction,columns=columns)
        prediction_df["Predicción"] = pred
        a = ["Resultado",
             DisplayDataFrame(prediction_df),
             Table(details)]
        return q, a

    def title(self):
        return "Clasificador Bayesiano"

