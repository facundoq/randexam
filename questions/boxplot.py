from test_generator import *
import math
from .quantiles import Quantiles

class Boxplot(DataQuestion):

    def __init__(self,d:Dataset,attribute_index:int):
        super().__init__(d) 
        q = Quantiles(d,attribute_index)
        self.q=q
        self.iqr = q.q3-q.q1
        self.iqr_mild = self.iqr*1.5
        self.iqr_extreme = self.iqr*3
        self.intervals ={
            "Atípicos Extremos bajos": (-math.inf,q.q1-self.iqr_extreme),
            "Atípicos Leves bajos": (q.q1-self.iqr_extreme,q.q1-self.iqr_mild) ,
            "Atípicos Leves altos": (q.q3+self.iqr_mild,q.q3+self.iqr_extreme) ,
            "Atípicos Extremos altos": (q.q3+self.iqr_extreme,math.inf),
        }
        self.b1= self.q

    def answer(self):
        
        def outliers(interval):
            l,h=interval
            return [v for v in self.q.values if l<=v<h]
        return [
            self.q.answer(),
            f"IQR: {self.iqr}",
        ]+ [f"{name}: {i}, valores: {outliers(i)}" for name,i in self.intervals.items()]
        

    def _generate(self, seed=None):
        
        q=[f"Calcule los cuartiles, el rango intercuartil, los valores de los bigotes, y los rangos de valores atípicos leves y extremos dados por el diagrama de caja del atributo  {self.d.attributes[self.q.attribute_index]}. Dibuje el diagrama.\n\n Nota: Utilice la definición de cuartil vista en la teoría. Presente los valores calculados como una tabla."]
        return q,self.answer()

    def title(self):
        return "Diagrama de Caja"