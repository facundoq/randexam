from test_generator import *
from test_generator import Dataset

class ClusteringQuestion(DataQuestion):
    def __init__(self,d:Dataset,n_samples:int,include_dataset=False,points:int=2):
        super().__init__(d,points=points)
        self.include_dataset=include_dataset
        self.n_samples=n_samples

    def calculate_distances(self, cd: Dataset):
        n_samples = self.d.n
        samples = [r[:-1] for r in self.d.rows]
        centroids = cd.rows
        n_centroids = cd.n
        distances_rows = []
        for i in range(self.n_samples):
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


class ClusteringAssignments(ClusteringQuestion):
    def initialize_centroids(self):
        col0 = self.d.column(0)
        col1 = self.d.column(1)
        col2=self.d.column(2)
        col0.sort(), col1.sort()
        c1 = [col0[2], col1[3], col2[2]]
        c2 = [col0[-3], col1[-2], col2[3]]

        c = Dataset([c1, c2], self.d.attributes[:3], self.d.attributes[:3], [])
        return c
    
    def generate(self,  seed=None):
        centroids = self.initialize_centroids()
        distances = self.calculate_distances(centroids)

        header = ["Ejemplo"] + distances.attributes
        distances_table = Table([["1", "$\sqrt{valor}$", "$\sqrt{valor}$", "(c1 o c2)"], ["..."] * 4], header=header)

        header = ["Centroide"] + self.d.attributes
        rows_with_id = [[f"**c{i + 1}**"] + row for i, row in enumerate(centroids.str_rows)]
        centroid_table = Table(rows_with_id, header=header)
        
        data_table = Table(self.d.str_rows[:self.n_samples], self.d.header, row_header="numbers")


        # b_q, b_a = self.silhouette_values()
        
        q = Paragraphs(
            [Text(
                f"Dado el siguiente conjunto de ejemplos numerizado, y dados los centroides **c1** y **c2**, "
                f"calcule la distancia euclídea de los ejemplos hacia estos centroides, "
                f"y a cuál de ellos estarían asignados. No utilizar la clase en este ejercicio."),
             data_table,
             centroid_table,
             Text(
                 "Nota: Para presentar los resultados, no calcule las raíces cuadradas."
                 "En lugar de eso, deje expresada los distancias como $\sqrt{valor}$. "
                 "Utilice una tabla como la siguiente:"),
             distances_table
             ])

        results_table = Table(distances.str_rows[:self.n_samples], distances.header, row_header="numbers")
        a = Paragraphs([results_table])
        return q, a

    def title(self):
        return "Agrupamiento de datos - Cálculo de asignaciones"


import random
import numpy as np
def indices_of(l:list,v):
    return [i for i,vi in enumerate(l) if v==vi]

class ClusteringCentroids(ClusteringQuestion):
    def __init__(self, d: Dataset, k:int, n_samples:int, include_dataset=False,points:int=2):
        super().__init__(d, n_samples,include_dataset,points=points)
        self.k=k
    def calculate_centroids(self,d:Dataset,assignments:list[int]):
        n_assignments = max(assignments)+1
        centroids = []
        for i in range(n_assignments):
            samples = [d.rows[j] for j in indices_of(assignments,i)]
            centroid =np.array(samples).mean(axis=0)
            centroids.append(list(centroid))
        return Dataset(centroids,d.header,d.attributes,d.class_values,d.ordinal_values)
        
    def generate(self,  seed=None):
        d = self.d.copy()
        d.rows = d.rows[-self.n_samples:]
        # generate assigments
        # ensure each centroid has a sample
        assert self.k<=d.n
        rest = d.n-self.k
        assignments = list(range(self.k))
        assignments += [random.randrange(0,self.k) for _ in range(rest)]
        random.shuffle(assignments)
        centroids = self.calculate_centroids(d,assignments)
        
        d.insert_column(assignments,"Cluster Asignado",d.m)
        
        
        data_table = Table(d.rows,d.header,row_header="numbers")

        # b_q, b_a = self.silhouette_values()
        q = Paragraphs(
            [
                f"Dado el siguiente conjunto de ejemplos numerizado, calcule los valores de los {self.k} centroides numerados desde 0 hasta {self.k-1} usando la asignación provista. No utilizar la clase en este ejercicio. Este ejercicio es independiente del resto del examen. Utilice una tabla con {self.k} filas y tantas columnas como atributos haya para presentar los centroides resultantes.",
             data_table,
             ])

        results_table = Table(centroids.rows, centroids.header, row_header="numbers")
        a = Paragraphs([results_table])
        return q, a

    def title(self):
        return "Agrupamiento de datos - Cálculo de centroides"