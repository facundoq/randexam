from test_generator import *
from test_generator.exam import QA

clustering_qas= [  QA("El costo computacional del cálculo del índice Silhouette ¿suele ser mayor que el de Davies-Bouldin?", "La afirmación es verdadera porque el Silhouette calcula para cada ejemplo su distancia promedio con los de su grupo y con los del grupo más cercano con esto obtiene el índice de cada ejmplo y finalmente los promedia. Por otro lado, DB compara agrupamientos y se espera que la cantidad de grupos sea considerablemente menor a la de ejemplos. Si esto último no ocurre, podría darse que DB fuera más costoso computacionalmente hablando pero este escenario no tiene mucho sentido en un contexto donde se busca construir un modelo descriptivo."),
            QA("¿Es preciso conocer la posición de los centros para calcular el índice Silhouette del agrupamiento?","Falso, ya que calcula distancias entre ejemplos y no centroides."),
            QA("Indique si la siguiente afirmación es verdadera o falsa: \n En el índice Sillhouette, tanto -1 como 1 son buenos valores, donde -1 indica correlación negativa y 1 positiva, y 0 indica que el clustering no es bueno.","Falso, 1 es bueno y -1 es malo"),
             QA("El indice Silhouette es superior a Davies Bouldin ya que considera distancias inter e intra cluster.",
                "Falso, ambos consideran esas distancias."),
            QA("Es preciso conocer la posición de los centros para calcular el índice Davies-Bouldin del agrupamiento",
               "Verdadero, ya que calcula distancias entre los centroides y los ejemplos de cada cluster."),
            QA("En el índice Silhouette, el clustering es perfecto cuando vale 0, y los valores extremos -1 y 1 indican desviaciones negativas y positivas del óptimo.",
               "Falso, como el indice se define como (b(i)-a(i))/max(b(i),a(i)), donde b es la distancia inter cluster promedio y a es la intracluster, entonces si vale 1 quiere decir que la distancia intercluster es grande y la intracluster es baja",),
            QA("El índice Silhouette siempre mejora a medida que se aumenta el número de clusters k",
               "Falso, como el Silhouette depende también de la separación entre clusters, puede que decremente o que aumente si se tienen muchos clusters pequeños pero cercanos entre sí. ",
),]

all_qa = [QA("Es posible calcular la mediana de un atributo ordinal",
                "VERDADERO. Vimos en clase como hacerlo"),
            QA("""El valor de la Ganancia de Información (Information Gain) de un atributo que toma siempre el mismo valor en todos los ejemplos es cero.""",
""" Verdadero. Si sólo tiene 1 valor, no separa los ejemplos por lo
que su entropía coincide con la entroía de conjunto original. Luego la
ganancia de información será la resta de 2 valores iguales."""),
            QA("Si se busca construir un árbol de clasificación, el atributo de clase (marcado como label) debe ser de tipo ordinal.",
                "FALSO. En realidad debe ser CUALITATIVO, es decir, ordinal o nominal."),
            QA("No es posible calcular la Tasa de Ganancia (Gain Ratio) de un atributo numérico continuo (con decimales).",
               "FALSO. La cantidad de valores del atributo será finita por lo que se ordenan los valores "
               "distintos (no importa que tenga decimales) y se calcula como vimos en clase."),
            QA("Es posible que al representar el diagrama de barras de un atributo discretizado por frecuencia se observen barras con alturas diferentes.",
                "VERDADERO. Esto ocurre cuando hay valores repetidos."),
            QA(" Un atributo nominal puede tener 2 modas.",
               "VERDADERO. Si dos de sus valores ocurren con la misma frecuencia y se trata del valor con más apariciones, ambos serán valores de MODA."),
            QA("Es posible calcular la tasa de acierto (accuracy) de un conjunto de reglas de asociación utilizando una matriz de confusión.",
               "Verdadero. Las reglas de asociación son un modelo descriptivo."),
               QA("La normalización lineal uniforme ¿es sensible a valores anómalos? ¿y la normalización por media/varianza?",
               "Lineal si, media/varianza también pero menos",
               ),

            QA("En un árbol de clasificación ¿a qué corresponden los nodos intermedios, los nodos hoja y las aristas?",
               "Los nodos intermedios corresponden a atributos, las aristas a valores de esos atributos, y los nodos hoja a decisiones o predicciones de la clase",
               ),
            QA("Dado un itemset con 3 items A,B,C, ¿cuántas reglas de asociación pueden generarse en base al itemset?",
               "6, A->(B,C) B->(A,C) C->(A,B), idem con 2 items en el antecedente",),
            QA("El algoritmo Apriori ¿genera reglas de Asociación?",
               "No, genera itemsets",),
            QA("El algoritmo FPGrowth ¿genera reglas de Asociación?",
               "No, genera itemsets",),
            
            
            QA("""Se tiene un problema de clasificación de 100 ejemplos con 3 columnas, una es la de la clase con 4 valores distintos, otra es nominal con 5 valores,
               y la otra es de un atributo numérico con 10 valores distintos. 
               Si se entrena un modelo de Naive Bayes ¿cuántas distribuciones gaussianas se deberán estimar?""",
               "Se estima una gaussiana para cada clase, o sea, 4 gaussianas."),
            QA("Dado un conjunto de atributos, puede afirmarse que los que tengan el mismo valor de entropía también tendrán el mismo valor de Ganancia de Información (Information Gain).",
                "Verdadero, ya que I(A) = E - E(A) "
               ),
            QA("El índice Silhouette se calcula en base a la dispersión de los ejemplos de cada grupo (cluster) y la distancia entre los centros.",
               "Falso, solo entre ejemplos"
            ),
            QA("Dado un conjunto de datos de 10 ejemplos con 2 columnas, una es la de la clase con 3 valores distintos, "
               "y la otra es un atributo nominal de 5 valores distintos. ¿Cuántos valores serán necesarios para almacenar un "
               "modelo Naive Bayes para clasificar los ejemplos?"
               ,"$3 \\times 5=15$, ya que para cada clase (3) debemos almacenar la distribución de probabilidad de los valores (5)"),
            QA("¿Cuál de las normalizaciones vistas es más sensible a los valores anómalos/extremos?",
               "La lineal, ya que si hay un valor extremo afecta al máximo/mínimo directamente.",
               ),

            QA("Los modelos de Reglas de Clasificación son casos particulares de los modelos de Árboles de Clasificación",
               "Falso, es al revés, ya que todo árbol puede expresarse como un conjunto de reglas pero no viceversa.",
               ),
            QA("Dada una regla, (A=Si,B=No) → C=Si, con soporte 0.3, ¿Puedo inferir el soporte de la regla (A=Si) → (B=No, C=Si) sin los datos?",
               "No se puede; se podría inferir la de (A=Si,B=No) ← C=Si ya que es la misma, pero para la del enunciado se requieren los datos.  ",),
            QA("Dado un conjunto de datos de 5 ejemplos con 2 columnas, una es la de la clase con 3 valores distintos, "
               "y la otra es un atributo nominal de 4 valores distintos. ¿Cuántos valores serán necesarios para almacenar un "
               "modelo Naive Bayes para clasificar los ejemplos?"
               ,"$4 \\times 5=20$, ya que para cada clase (5) debemos almacenar la distribución de probabilidad de los valores (4)"),
            QA("""Se tiene un problema de clasificación de 100 ejemplos con 3 atributos/columnas, la primera es la de la clase con 3 valores distintos, la segunda tiene valores nominales con 4 valores distintos y la tercera tiene valores numéricos con 5 valores distintos. 
               Si se entrena un modelo de Naive Bayes ¿cuántas distribuciones gaussianas se deberán estimar?""",
               "Se estima una gaussiana para cada clase y atributo numérico, o sea, 3x1 = 3 gaussianas."),
            QA("Dado un conjunto de datos con 3 clases, 5 atributos nominales y 100000 ejemplos. Si se entrena un árbol de clasificación con este conjunto de datos ¿puedo saber cuántos nodos tendrá como máximo el árbol?",
                "No, ya que también debería saber cuántos valores hay en cada atributo nominal."
               ),
            QA("El índice Davies Bouldin se calcula en base a la dispersión de los ejemplos de cada grupo (cluster) y la distancia entre los centros.",
               "Verdadero"
            ),
             QA("Dado un conjunto de atributos, puede afirmarse que los que tengan el mismo valor de entropía también tendrán el mismo valor de Ganancia de Información (Information Gain).", "V"),
            QA("El índice Silhouette se calcula en base a la dispersión de los ejemplos de cada grupo (cluster) y la distancia entre los centros.","F"),
            QA("Si se busca construir un árbol de clasificación, el atributo de clase no puede ser numérico.","V"),
            QA("Las reglas de clasificación que se generan con OneR pueden ejecutarse en cualquier orden a diferencia de las generadas con el método PART.","V"),
            QA("Dadas dos reglas con valor de confianza=1 (perfectas) será más interesante la que tenga un menor valor de soporte para el consecuente.","V"),
            QA("Un atributo nominal sólo aparecerá una vez en una misma regla generada con el método PART (recuerde que se generan como una rama de un árbol parcialmente construido con C4.5)","V"),
            QA("Para poder agrupar un conjunto de ejemplos utilizando el método K-Means es obligatorio que los valores de los atributos estén escalados.","F"),
              QA("Entre la normalización lineal uniforme y la normalización por media/varianza ¿cuál es más sensible a valores extremos?","La lineal. La de media/varianza también pero menos"),
            QA("En un árbol de clasificación ¿a qué corresponden los nodos intermedios, los nodos hoja y las aristas?","Los nodos intermedios corresponden a atributos, las aristas a valores de esos atributos, y los nodos hoja a decisiones o predicciones de la clase"),
            QA("Dado un itemset con 3 items A,B,C, ¿cuántas reglas pueden generarse en base al itemset?","6, A->(B,C) B->(A,C) C->(A,B), idem con 2 items en el antecedente"),
            QA("El algoritmo Apriori ¿genera reglas de Asociación?","No, genera itemsets"),
            QA("El algoritmo FPGrowth ¿genera reglas de Asociación?","No, genera itemsets"),
            QA("Al generar reglas con APriori o FPGrowth ¿es necesario generar itemsets?","Si, justamente generan itemsets"),
            QA("Dados los items A y B, si A->B tiene soporte 0.7 ¿cuál será el soporte de B->A?","El mismo"),
            QA("¿Cuáles son las dos propiedades que deben cumplir los grupos (clusters) para obtener un buen agrupamiento?", "Alta cohesión intra cluster y alta separación intercluster.") ,
            QA("El peso de una red neuronal correspondiente al atributo A es negativo (por ejemplo, -10). Dado un ejemplo, si el valor del ejemplo para el atributo de A baja, ¿a qué clase se acercará el ejemplo?","A la clase 0, ya que a mayor valor de A, menor valor de la entrada neta.")
            ]+clustering_qas





class ConceptsQuestion(QAQuestion):
    def __init__(self, qas: list[QA],points:int):
        title = "Conceptos de Minería de Datos"
        instructions = "Responda las preguntas o indique el valor de verdad de  las siguientes afirmaciones. Justifique sus respuestas."
        super().__init__(title, instructions, qas,points)

class Concepts2(ConceptsQuestion):

    def __init__(self):
        super().__init__(qas= all_qa[:7])

class Concepts3(ConceptsQuestion):

    def __init__(self):
        super().__init__( all_qa[7:15])


class Concepts4(ConceptsQuestion):

    def __init__(self):
        super().__init__(all_qa[15:23])

import random
class ConceptsRandom(ConceptsQuestion):

    def __init__(self,n:int,points:int):
        qas = all_qa.copy()
        random.shuffle(qas)
        super().__init__(qas[:n],points)



class ClusteringConcepts1(ConceptsQuestion):
       def __init__(self,points:int):
        super().__init__(clustering_qas[:3],points)

class ClusteringConcepts2(ConceptsQuestion):
       def __init__(self,points:int):
        super().__init__(clustering_qas[3:7],points)        