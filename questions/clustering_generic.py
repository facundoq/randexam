from test_generator import *
import pandas as pd
from scipy.spatial import distance
import numpy as np
import matplotlib.pyplot as plt
import uuid


class ClusteringGeneric(DataFrameQuestion):
    def __init__(self,d:pd.DataFrame,c:pd.DataFrame,n_steps=1,include_dataset=False):
        super().__init__(d)
        self.include_dataset=include_dataset
        self.n_steps = n_steps
        self.c=c

    def points(self) -> str:
        return 2

    def update_centroids(self,assignments:np.array,k:int):
        centroids = []
        for i in range(k):
            centroid_samples = self.d.iloc[assignments==i,:]
            if len(centroid_samples)==0:
                d = len(self.d.columns)
                centroid = [0]*d
            else:
                centroid = centroid_samples.mean(axis=0).tolist()
            
            centroids.append(centroid)
        
        return pd.DataFrame(centroids,columns=self.d.columns)

    def generate_step(self,c:pd.DataFrame,distances:np.array,assignments:np.array):
        k = len(c)
        columns = [f"d(c{i})" for i in range(k)]+ ["Centroide asignado"]
        centroid_row_header = [f"c{i}" for i in range(len(c))]

        distance_assignments = np.hstack([distances,assignments])
        distance_assignments_df =pd.DataFrame(distance_assignments,columns=columns)
        distances_table = DisplayDataFrame(distance_assignments_df,title="Distancias y asignaciones",row_header="numbers")
        centroids_table = DisplayDataFrame(c,title="Centroides resultantes",row_header=centroid_row_header)
        return [distances_table,centroids_table]
    
    def generate_steps(self):
        steps = []
        c = self.c
        dims = self.d.shape[1]
        for i in range(self.n_steps):
            if dims ==2:
                plt.scatter(self.d.iloc[:,0],self.d.iloc[:,1],c="g")
                plt.scatter(c.iloc[:,0],c.iloc[:,1],c="b")
                image = [MatplotlibFigure(plt.gcf())]
            else:
                image = []
            distances = distance.cdist(self.d, c, metric='sqeuclidean')
            assignments = distances.argmin(axis=1).reshape(-1,1)
            c = self.update_centroids(assignments,len(c))
            steps.append([f"Paso {i+1}"]+ image +self.generate_step(c,distances,assignments))
            
        return Paragraphs(steps)

        
    def generate(self,  seed=None):
        n_samples = len(self.d)
        data_table = DisplayDataFrame(self.d,row_header="numbers",title="Ejemplos")
        centroid_row_header = [f"c{i}" for i in range(len(self.c))]
        centroid_table = DisplayDataFrame(self.c,title="Centroides",row_header=centroid_row_header)


        # b_q, b_a = self.silhouette_values()
        q = [f"Dados ejemplos de la tabla, y dados los centroides, "
                f"calcule {self.n_steps} pasos del algoritmo K-Medias. En cada paso, incluya (a) la tabla de distancias euclídeas de los ejemplos hacia los centroides, (b) la tabla de las asignaciones de los ejemplos a los centroides, y (c) la tabla de los nuevos centroides calculados a partir de esas asignaciones.",
             data_table,
             centroid_table,
             "Nota: Utilizar la distancia euclidea al cuadrado, es decir, no calcular la raíz cuadrada al calcular la distancia."
             ]

        
        a = self.generate_steps()
        return q, a

    def title(self):
        return "Agrupamiento de datos"



