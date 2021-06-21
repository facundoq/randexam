from test_generator import *
from questions import preprocessing


class Discretization(DataQuestion):

    def __init__(self,d:Dataset,attribute_index:int,values:int):
        super().__init__(d)
        self.attribute_index=attribute_index
        self.values=values

    def answer(self,strategy,result):
        intervals,values=result
        e=Text(f"Resultado de la discretización por {strategy}:")
        v=Text(f"Valores: {values}")
        i=Text(f"Intervalos: {intervals}")
        a= Paragraphs([e,v,i])
        return a

    def generate(self, seed=None):
        n_intervals=self.values
        attribute_index=self.attribute_index
        q=Paragraphs([Text(f"Discretice el atributo {self.d.attributes[attribute_index]}  por a) frecuencia y b) rango en {n_intervals} valores. En ambos casos, indique los intervalos resultantes. Realice un gráfico de barras para visualizar la frecuencia de los valores resultantes.\n\n Nota: La discretización es solo para este ejercicio; utilizar los datos originales en los siguientes.")])

        values=self.d.column(attribute_index)
        strategies={"rango": preprocessing.discretize_by_range, "frecuencia": preprocessing.discretize_by_frequency}
        results={k:f(values,n_intervals) for k,f in strategies.items()}
        answers=[self.answer(k,r) for k,r in results.items()]
        a=Paragraphs(answers)
        return q,a

    def title(self):
        return "Discretización de atributos"