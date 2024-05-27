from test_generator import *


class Discretization(DataQuestion):

    def __init__(self,d:Dataset,attribute_index:int,values:list,points:int=1):
        super().__init__(d,points=points)
        self.attribute_index=attribute_index
        self.values=values
        

    def answer(self,strategy,result):
        intervals,values=result
        e=Text(f"Resultado de la discretización por {strategy}:")
        v=Text(f"Valores: {values}")
        i=Text(f"Intervalos: {intervals}")
        a= Paragraphs([e,v,i])
        return a

    def _generate(self, seed=None):
        attribute_index=self.attribute_index
        q=Paragraphs([f"Discretice el atributo {self.d.attributes[attribute_index]}  por a) frecuencia y b) rango en los valores {self.values}. En ambos casos, indique los intervalos resultantes. Realice un gráfico de barras para visualizar la frecuencia de los valores resultantes.\n\n Nota: La discretización es solo para este ejercicio; utilizar los datos originales en el resto de los ejercicios."])

        x=self.d.column(attribute_index)
        strategies={"rango": preprocessing.discretize_by_range, "frecuencia": preprocessing.discretize_by_frequency}
        results={k:f(x,self.values) for k,f in strategies.items()}
        answers=[self.answer(k,r) for k,r in results.items()]
        a=Paragraphs(answers)
        return q,a

    def title(self):
        return "Discretización de atributos"