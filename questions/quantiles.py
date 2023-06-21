from test_generator import *
from questions import preprocessing
import math

class Quantiles(DataQuestion):

    def __init__(self,d:Dataset,attribute_index:int,points=1):
        super().__init__(d,points=points)
        self.attribute_index=attribute_index
        values = self.d.column(attribute_index)
        values = list(map(float,values))
        values = sorted(values)
        self.values = values
        n = len(self.values)
        self.n1 = (n+1)/4
        self.n2 = self.n1*2
        self.n3 = self.n1*3

        def get_value(values,n):
            index = math.floor(n)
            extra = n-index
            if extra<1e-16:
                return values[index-1]
            else:
                return values[index-1]*(1-extra)+values[index]*extra
            
        self.q1 = get_value(self.values,self.n1)
        self.q2 = get_value(self.values,self.n2)
        self.q3 = get_value(self.values,self.n3)

    def answer(self):

        return [
        f"Valores ordenados de  {self.d.header[self.attribute_index]}:",
         str(self.values),
        f"Índices de los cuartiles:",       
        f"{self.n1}, {self.n2}, {self.n3}",
        f"Cuartiles:",
        f"q1={self.q1}, q2={self.q2}, q3={self.q3}",
        ]
        

    def _generate(self, seed=None):
        attribute_index=self.attribute_index
        q=[f"Calcule la mediana y los dos cuartiles del atributo {self.d.attributes[attribute_index]}.\n\n Nota: Utilice la definición de cuartil vista en la teoría."]
        return q,self.answer()

    def title(self):
        return "Cuartiles"