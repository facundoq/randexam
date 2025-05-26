from xml.etree.ElementInclude import include
from test_generator import *
import numpy as np

class Normalization(DataQuestion):


    def __init__(self,d:Dataset,attribute_index:int,range=True,meanstd=True,interpret_sample:int=None,include_parameters=False):
        super().__init__(d)
        self.attribute_index=attribute_index
        self.range=range
        self.meanstd=meanstd
        self.interpret_sample=interpret_sample
        self.include_parameters=include_parameters


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
        strategies = {}
        values = self.d.column(attribute_index)
        values = np.array(values,dtype=float)

        if self.range:
            strategies["rango"]=preprocessing.CenterScaleNormalization.min_max(values)
            text+= f"{count}. rango lineal uniforme (min/max)\n\n"
            count+=1
        if self.meanstd:
            text += f"{count}. media/desviación\n\n"
            count += 1
            strategies["mu/std"] = preprocessing.CenterScaleNormalization.mu_std(values)
            if self.include_parameters:
                text+= f"""\n Como ayuda, te damos el valor de la media, $\mu={strategies["mu/std"].center:.2f}$, y la desviación estándar, $\sigma={strategies["mu/std"].scale:.2f}$."""


        


        text+= f"""\nIndicar las ecuaciones utilizadas, y los valores resultantes normalizados."""
        if not self.interpret_sample is None:
            value = self.d.rows[self.interpret_sample][self.attribute_index]
            key = self.d.attributes[self.attribute_index]
            text+=f" Inteprete los valores normalizados obtenidos para {key}={value}."
            if self.range:
                text+= f" Para el rango lineal uniforme (min/max), indique qué significa en la escala 0-1.\n"
            if self.meanstd:
                text+= f" Para la normalización media/varianza, indique qué significa en relación a estos valores.\n"
        if self.meanstd and self.range:
            text+=f""" \n\n Estas normalizaciones ¿Son equivalentes? ¿A qué valor de la normalización min/max corresponde la media de los valores?. Justifique."""
        text+=f""" \n\n Nota: La normalización es solo para este ejercicio. Utilizar los datos provistos en el resto de los ejercicios."""
        q = Paragraphs([Text(text)])
        
      
        answers = [self.answer(name,norm,values) for name,norm in strategies.items()]
        a = Paragraphs(answers)
        return q,a

    def title(self):
        return "Normalización de atributos"
