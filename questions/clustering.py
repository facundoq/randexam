from test_generator import *

class Clustering(DataQuestion):
    def __init__(self,d:Dataset,include_dataset=False):
        super().__init__(d)
        self.include_dataset=include_dataset

    def generate_centroids(self):
        col0 = self.d.column(0)
        col1 = self.d.column(1)
        col2=self.d.column(2)
        col0.sort(), col1.sort()
        c1 = [col0[2], col1[3], col2[2]]
        c2 = [col0[-3], col1[-2], col2[3]]

        c = Dataset([c1, c2], self.d.attributes[:3], self.d.attributes[:3], [])
        return c

    def calculate_distances(self, cd: Dataset):
        n_samples = self.d.n
        samples = [r[:-1] for r in self.d.rows]
        centroids = cd.rows
        n_centroids = cd.n
        distances_rows = []
        for i in range(n_samples):
            row = []
            for j in range(n_centroids):
                sample, centroid = samples[i], centroids[j]
                distance = sum([(s - c) ** 2 for s, c in zip(sample, centroid)])
                row.append(distance)
            assigned_centroid = row.index(min(row))
            row.append(assigned_centroid + 1)
            distances_rows.append(row)
        attributes = ["d(c1)", "d(c2)", "Centroide asignado"]
        return Dataset(distances_rows, attributes, attributes, [])



    def generate(self,  seed=None):
        centroids = self.generate_centroids()
        distances = self.calculate_distances(centroids)

        header = ["Ejemplo"] + distances.attributes
        distances_table = Table([["1", "$\sqrt{valor}$", "$\sqrt{valor}$", "(c1 o c2)"], ["..."] * 4], header=header)

        header = ["Centroide"] + self.d.attributes
        rows_with_id = [[f"**c{i + 1}**"] + row for i, row in enumerate(centroids.str_rows)]
        centroid_table = Table(rows_with_id, header=header)
        n_samples = 3
        data_table = Table(self.d.str_rows[:n_samples], self.d.header, number_rows=True)


        # b_q, b_a = self.silhouette_values()
        q = Paragraphs(
            [Text(
                f"Dados los datos de los {n_samples} primeros ejemplos de la tabla donde se numerizaron las columnas nominales, y dados los centroides **c1** y **c2**, "
                f"calcule la distancia euclídea de los ejemplos hacia estos centroides, "
                f"y a cuál de ellos estarían asignados. No utilizar la clase en este ejercicio."),
             data_table,
             centroid_table,
             Text(
                 "Nota: Para presentar los resultados, no calcule las raíces cuadradas. "
                 "En lugar de eso, deje expresada los distancias como $\sqrt{valor}$. "
                 "Utilice una tabla como la siguiente:"),
             distances_table
             ])

        results_table = Table(distances.str_rows[:n_samples], distances.header, number_rows=True)
        a = Paragraphs([results_table])
        return q, a

    def title(self):
        return "Agrupamiento de datos"




class ClusteringEvaluationQuestions(MultipleQuestions):

    def __init__(self):
        title = "Conceptos de Agrupamientos"
        instructions = "Indique la respuesta a las siguientes preguntas. Justifique su respuesta."
        questions = [
            "El costo computacional del cálculo del índice Silhouette ¿suele ser mayor que el de Davies-Bouldin?",
            "¿Es preciso conocer la posición de los centros para calcular el índice Silhouette del agrupamiento?",
            "Indique si la siguiente afirmación es verdadera o falsa: \n En el índice Sillhouette, tanto -1 como 1 son buenos valores, donde -1 indica correlación negativa y 1 positiva, y 0 indica que el clustering no es bueno."
        ]

        answers = [
            "La afirmación es verdadera porque el Silhouette calcula para cada ejemplo su distancia promedio con los de su grupo y con los del grupo más cercano con esto obtiene el índice de cada ejmplo y finalmente los promedia. Por otro lado, DB compara agrupamientos y se espera que la cantidad de grupos sea considerablemente menor a la de ejemplos. Si esto último no ocurre, podría darse que DB fuera más costoso computacionalmente hablando pero este escenario no tiene mucho sentido en un contexto donde se busca construir un modelo descriptivo.",
            "Falso, ya que calcula distancias entre ejemplos y no centroides.",
            "",
        ]
        super().__init__(title,instructions,questions,answers)

class ClusteringEvaluationQuestions2(MultipleQuestions):

    def __init__(self):
        title = "Conceptos de Agrupamientos"
        instructions = "Indique verdadero (V) o falso (F) para las siguientes preguntas. **Justifique** su respuesta."
        questions = [
            "El indice Silhouette es superior a Davies Bouldin ya que considera distancias inter e intra cluster.",
            "Es preciso conocer la posición de los centros para calcular el índice Davies-Bouldin del agrupamiento",
            "En el índice Silhouette, el clustering es perfecto cuando vale 0, y los valores extremos -1 y 1 indican desviaciones negativas y positivas del óptimo.",
            "El índice Silhouette siempre mejora a medida que se aumenta el número de clusters k",

        ]

        answers = [
            "Falso, ambos consideran esas distancias.",
            "Verdadero, ya que calcula distancias entre los centroides y los ejemplos de cada cluster.",
            "Falso, como el indice se define como (b(i)-a(i))/max(b(i),a(i)), donde b es la distancia inter cluster promedio y a es la intracluster, entonces si vale 1 quiere decir que la distancia intercluster es grande y la intracluster es baja",
            "Falso, como el Silhouette depende también de la separación entre clusters, puede que decremente o que aumente si se tienen muchos clusters pequeños pero cercanos entre sí. ",
        ]
        super().__init__(title,instructions,questions,answers)
