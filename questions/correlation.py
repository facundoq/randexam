from test_generator import *
import numpy as np

class CorrelationMatrix(DataQuestion):
    def generate(self,seed=None):
        q = ["Calcule la matriz de correlación entre los atributos del conjunto de datos"]
        v = np.array(self.d.rows)
        correlation_matrix = np.corrcoef(v.T)
        covariance_matrix = np.cov(v.T)
        a = [f"Medias: {v.mean(axis=0)}",
             f"Desviaciones: {v.std(axis=0)}",
             "Covarianza:",
             Table(covariance_matrix,header=self.d.header),
            "Correlación:",
             Table(correlation_matrix,header=self.d.header)],
        return q,a
    def title(self):
        return "Matriz de Correlación"
    
class CorrelationCoefficient(DataQuestion):
    def __init__(self,d:Dataset,a:int,b:int):
        super().__init__(d)
        self.a=a
        self.b=b
        x = np.array(self.d.rows)
        self.covariance = np.cov(x.T)[a,b]
        self.correlation = np.corrcoef(x.T)[a,b]
        self.means = (x.mean(axis=0)[a],x.mean(axis=0)[b])
        self.stds = (x.std(axis=0)[a],x.std(axis=0)[b])
        
        absc = abs(self.correlation)
        self.direction = "Positiva" if self.correlation>0 else "Negativa"
        self.intensity = "No hay" if absc< 0.3 else ("Débil" if absc<0.8 else "Fuerte")

    def generate(self,seed=None):
        q = [f"Calcule la matriz de correlación entre los atributos {self.d.attributes[self.a]}  y {self.d.attributes[self.b]} del conjunto de datos"]
        a = [f"Medias: {self.means}",
             f"Desviaciones: {self.stds}",
             f"Covarianza: {self.covariance}",
            f"Correlación: {self.correlation}",
            f"Intensidad: {self.intensity}",
            f"Tipo: {self.direction}",
        ]
        return q,a
    def title(self):
        return "Coeficiente de correlación"
    
class CorrelationMatrixJuego(DataQuestion):

    def generate(self,seed=None):
        attributes=["Ambiente","Temperatura","Humedad","Viento","Juega"]
        header = [" "]+attributes
        rows=[[1,0.28,0.11,0,-0.18],
              [0.28,1,0.75,-0.21,-0.11],
              [0.11,0.75,1,-0.12,-0.52],
              [0,-0.21,-0.12,1,-0.26],
              [-0.18,-0.11,-0.52,-.26,1]
             ]
        rows = [[str(v) for v in row] for row in rows]
        rows = [[a]+row for a,row in zip(attributes,rows)]

        correlation_matrix=Table(rows,header=header)
        q=Paragraphs(
            [Text("Dada la siguiente matriz de correlación, indique la verdad (V) o falsedad (F) de las afirmaciones:"),
            correlation_matrix,
            Text("a) Los atributos Ambiente y Viento son independientes.\nb) Es posible que si sube la Humedad, también suba el valor del atributo Juega.\nc) Los atributos Humedad y Temperatura están correlacionados linealmente, y la correlación es **fuerte**.\nd) La mayoría de los pares de atributos no están correlacionados linealmente."),
            ])
        aa=Text("a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viento=ambiente^2")
        ab=Text("b) Falso,  la correlación es negativa")
        ac=Text("c) Falso, la correlación es débil (0.5<x<0.8)")
        ad=Text("d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.")
        a=Paragraphs([Text("F,F,F,V"),aa,ab,ac,ad])
        return q,a
    def title(self):
        return "Matriz de Correlación"



class CorrelationMatrixAmbiente(DataQuestion):
    def generate(self,seed=None):
        attributes=["Ambiente","Temperatura","Humedad","Viento","Juega"]
        header = [" "]+attributes
        rows=[[1,0.28,1,0,-0.18],
              [0.28,1,0.75,-0.85,-0.11],
              [1,0.75,1,-0.12,-1],
              [0,-0.85,-0.12,1,-0.26],
              [-0.18,-0.11,-1,-.26,1]
             ]
        rows = [[str(v) for v in row] for row in rows]
        rows = [[a]+row for a,row in zip(attributes,rows)]

        correlation_matrix=Table(rows,header=header)
        q=Paragraphs(
            [Text("Dada la siguiente matriz de correlación, indique la verdad (V) o falsedad (F) de las afirmaciones:"),
            correlation_matrix,
            Text("a) Los atributos Ambiente y Humedad son independientes.\nb) Los atributos Juega y Humedad son independientes \nc) Los atributos Viento y Temperatura están correlacionados linealmente, y la correlación es **fuerte**.\nd) La mayoría de los pares de atributos están correlacionados linealmente."),
            ])
        aa=Text("a) Falso, un valor de 1 indica que son linealmente dependientes con dependencia positiva ")
        ab=Text("b) Falso,  un valor de -1 indica que son linealmente dependientes con dependencia positiva")
        ac=Text("c) Verdadero, la correlación es fuerte (<-0.8)")
        ad=Text("d) Falso, de los 5*4/2=10 pares solo 4 tienen correlación lineal débil o fuerte.")
        a=Paragraphs([Text("F,F,V,F"),aa,ab,ac,ad])
        return q,a
    def title(self):
        return "Matriz de Correlación"



class CorrelationMatrixBienestar(DataQuestion):

    def generate(self,seed=None):
        attributes=["Desarrollo","Contaminación","Calidad de Vida","Población"]
        header = [" "]+attributes
        rows=[[ 1,    -0.25, 0.88,  0.0001],
              [-0.25,  1,    0.75,  -0.72],
              [ 0.88,  0.75, 1,      0.12],
              [ 0.0001,  -0.72, 0.12,  1],
             ]
        rows = [[str(v) for v in row] for row in rows]
        rows = [[a]+row for a,row in zip(attributes,rows)]

        correlation_matrix=Table(rows,header=header)
        q=Paragraphs(
            [Text("Dada la siguiente matriz de correlación, indique la verdad (V) o falsedad (F) de las afirmaciones. Justificar en cada caso."),
            correlation_matrix,
            Text("a) Los atributos Desarrollo y Población son aproximadamente independientes.\n"
                 "b) Es probable que si sube el Desarrollo, también suba la Calidad de Vida.\n"
                 "c) Los atributos Desarrollo y Contaminación están correlacionados linealmente, y la correlación es **Débil**.\n"
                 "d) Los atributos Población y Contaminación están correlacionados linealmente, y la correlación es **Débil**.\n"
                 "e) La mayoría de los pares de atributos no están correlacionados linealmente."),
            ])
        aa=Text("a) Falso, si bien la correlación es casi 0, pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2")
        ab=Text("b) Verdadero,  la correlación es positiva y fuerte")
        ac=Text("c) Falso, no hay correlación (|x|<0.5)")
        ad=Text("d) Verdadero, la correlación es débil y negativa ya que 0.5 < |x| < 0.8.")
        ae=Text("e) Falso, justo la mitad está correlacionada y la mitad no.")
        a=Paragraphs([aa,ab,ac,ad,ae])
        return q,a
    def title(self):
        return "Matriz de Correlación"



class CorrelationMatrixJugador(DataQuestion):

    def generate(self,seed=None):
        attributes=["Velocidad","Fuerza","Destreza","Resistencia"]
        header = [" "]+attributes
        rows=[[ 1,    0.72, 0.88,  0.0001],
              [0.72,  1,    -0.65,  -0.2],
              [ 0.88,  -0.65, 1,      0.14],
              [ 0.0001,  -0.2, 0.14,  1],
             ]
        rows = [[str(v) for v in row] for row in rows]
        rows = [[a]+row for a,row in zip(attributes,rows)]

        correlation_matrix=Table(rows,header=header)
        q=Paragraphs(
            [Text("Dada la siguiente matriz de correlación, indique la verdad (V) o falsedad (F) de las afirmaciones. Justificar en cada caso."),
            correlation_matrix,
            Text("a) Los atributos Velocidad y Resistencia son aproximadamente independientes.\n"
                 "b) Es probable que si sube la Destreza, también suba la Velocidad.\n"
                 "c) Los atributos Velocidad y Fuerza están correlacionados linealmente, y la correlación es **Fuerte**.\n"
                 "d) Los atributos Destreza y Fuerza están correlacionados linealmente, y la correlación es **Débil**.\n"
                 "e) Hay más pares de atributos correlacionados que no correlacionados linealmente."),
            ])
        aa=Text("a) Falso, si bien la correlación es casi 0, pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, Velocidad=Resistencia^2")
        ab=Text("b) Verdadero,  la correlación es positiva y fuerte")
        ac=Text("c) Falso, la correlación es positiva pero débil (|x|<0.8)")
        ad=Text("d) Verdadero, la correlación es débil y negativa ya que 0.5 < |x| < 0.8.")
        ae=Text("e) Falso, justo la mitad está correlacionada y la mitad no.")
        a=Paragraphs([aa,ab,ac,ad,ae])
        return q,a
    def title(self):
        return "Matriz de Correlación"