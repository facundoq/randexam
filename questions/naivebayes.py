from test_generator import *

class ApplyNaiveBayes(DataQuestion):

    def generate(self, seed=None):


        # header = ["Ejemplo"]
        # distances_table = Table([["1", "$\sqrt{valor}$", "$\sqrt{valor}$", "(c1 o c2)"], ["..."] * 4], header=header)
        #
        # header = ["Centroide"] + self.d.attributes
        #
        # rows_with_id = [[f"**c{i + 1}**"] + row for i, row in enumerate(centroids.str_rows)]
        # centroid_table = Table(rows_with_id, header=header)
        n_samples = 3
        # b_q, b_a = self.silhouette_values()
        q = Paragraphs(
            [Text(
                f"Dado el modelo de Naive Bayes siguiente, indicar la clase de los 2 primeros ejemplos del conjunto de datos."),
             # centroid_table,

             ])
        a = Paragraphs([Text("Resultado")])
        return q, a

    def title(self):
        return "Clasificador Bayesiano"

    class NaiveBayesQuestions(MultipleQuestions):

        def __init__(self):

        def title(self):
            return "Conceptos sobre Clasificador Bayesiano"