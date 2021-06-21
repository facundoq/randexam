from test_generator import *


class Numerization(DataQuestion):
    def __init__(self, d: Dataset, d_numerized: Dataset,attribute_index:int):
        super().__init__(d)
        self.d_numerized = d_numerized
        self.attribute_index=attribute_index

    def generate(self, seed=None):
        col = self.attribute_index
        q = Text(
            f"Numerizar el atributo **{self.d.attributes[col]}** del conjunto de datos original. "
            f"Utilizar la estrategia de generar un valor entero por cada valor numérico. "
            f"Comenzar con el valor 1, y respetar el orden natural de dicho atributo, de menor a mayor. "
            f"Mostrar los valores resultantes.")

        original = Text(f"Valores originales: {self.d.column(col)}\n")
        nuevos = Text(f"Valores nuevos: {self.d_numerized.column(col)}\n")
        t = Table(self.d_numerized.str_rows, header=self.d_numerized.header, number_rows=True)
        a = Paragraphs([original, nuevos, t])

        return q, a

    def title(self):
        return "Numerización de datos"