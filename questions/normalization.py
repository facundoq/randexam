from test_generator import *
from questions import preprocessing
import numpy as np

class Normalization(DataQuestion):


    def __init__(self,d:Dataset,attribute_index:int,range=True,meanstd=True):
        super().__init__(d)
        self.attribute_index=attribute_index
        self.range=range
        self.meanstd=meanstd


    def answer(self, strategy:str, norm: preprocessing.CenterScaleNormalization, values):
        a=Text(f"Normalización {strategy} con transformación {norm}")
        normalized_values=norm.apply(values)
        normalized_values=", ".join([f"{v:.2f}" for v in normalized_values])
        v=Text(f"Valores normalizados: {normalized_values}")
        return Paragraphs([a,v])

    def _generate(self, seed=None):
        attribute_index=self.attribute_index
        text =f"Normalice el atributo {self.d.attributes[attribute_index]} mediante: \n\n"
        count=1
        if self.range:
            text+= f"{count}. rango lineal uniforme (min/max)\n\n"
            count+=1
        if self.meanstd:
            text += f"{count}. media/varianza\n\n"
            count += 1
        note = f"\nIndicar los valores resultantes normalizados. " \
               f"\n Nota: La normalización es solo para este ejercicio. "\
               f"Utilizar los datos originales en los siguientes."
        text+=note
        q = Paragraphs([Text(text)])
        values = self.d.column(attribute_index)
        values = np.array(values,dtype=float)
        strategies = {}
        if self.range:
            strategies["rango"]=preprocessing.CenterScaleNormalization.min_max(values)
        if self.meanstd:
            strategies["mu/std"] = preprocessing.CenterScaleNormalization.mu_std(values)
        answers = [self.answer(name,norm,values) for name,norm in strategies.items()]
        a = Paragraphs(answers)
        return q,a

    def title(self):
        return "Normalización de atributos"
