from test_generator import *

class TrueOrFalse(MultipleQuestions):

    def __init__(self):
        title = "Conceptos de Minería de Datos"
        instructions = "Indique si las siguientes afirmaciones son Verdaderas o Falsas. Justifique su respuesta."
        questions = [
            "Dado un conjunto de atributos, puede afirmarse que los que tengan el mismo valor de entropía también tendrán el mismo valor de Ganancia de Información (Information Gain).",
            "El índice Silhouette se calcula en base a la dispersión de los ejemplos de cada grupo (cluster) y la distancia entre los centros.",
            "Si se busca construir un árbol de clasificación, el atributo de clase no puede ser numérico.",
            "Las reglas de clasificación que se generan con OneR pueden ejecutarse en cualquier orden a diferencia de las generadas con el método PART.",
            "Dadas dos reglas con valor de confianza=1 (perfectas) será más interesante la que tenga un menor valor de soporte para el consecuente.",
            "Un atributo nominal sólo aparecerá una vez en una misma regla generada con el método PART (recuerde que se generan como una rama de un árbol parcialmente construido con C4.5)",
            "Para poder agrupar un conjunto de ejemplos utilizando el método K-Means es obligatorio que los valores de los atributos estén escalados."
        ]
        answers = ["V", "F", "V", "V", "V", "V", "F"]
        super().__init__(title, instructions, questions, answers)



class RandomQuestions(MultipleQuestions):

    def __init__(self):
        title = "Conceptos de Minería de Datos"
        instructions = "Indique la respuesta a las siguientes preguntas. Justifique sus respuestas."
        questions = [
            "La normalización lineal uniforme ¿es sensible a valores anómalos? ¿y la normalización por media/varianza?",
            "En un árbol de clasificación ¿a qué corresponden los nodos intermedios, los nodos hoja y las aristas?",
            "Dado un itemset con 3 items A,B,C, ¿cuántas reglas pueden generarse en base al itemset?",
            "El algoritmo Apriori ¿genera reglas de Asociación?",
            "El algoritmo FPGrowth ¿genera reglas de Asociación?",
            "Al generar reglas con APriori o FPGrowth ¿es necesario generar itemsets?",
            "Dados los items A y B, si A->B tiene soporte 0.7 ¿cuál será el soporte de B->A?",
            "¿Cuáles son las dos propiedades que deben cumplir los grupos (clusters) para obtener un buen agrupamiento?",
            "El peso de una red neuronal correspondiente al atributo A es negativo. Dado un ejemplo, si el valor de A sube, ¿a qué clase se acercará el ejemplo?",
        ]

        answers = [
            "Lineal si, media/varianza también pero menos",
            "Los nodos intermedios corresponden a atributos, las aristas a valores de esos atributos, y los nodos hoja a decisiones o predicciones de la clase",
            "6, A->(B,C) B->(A,C) C->(A,B), idem con 2 items en el antecedente",
            "No, genera itemsets",
            "No, genera itemsets",
            "Si, justamente generan itemsets",
            "El mismo",
            "Alta cohesión intra cluster y alta separación intercluster.",
            " A la clase 0, ya que a mayor valor de A, menor valor de la entrada neta.",
        ]

        super().__init__(title,instructions,questions,answers)

class Concepts2(QAQuestion):

    def __init__(self):
        title = "Conceptos de Minería de Datos"
        instructions = "Indique el valor de verdad de a las siguientes afirmaciones. Justifique sus respuestas."
        qas= [
            QA("Es posible calcular la mediana de un atributo ordinal",
                "VERDADERO. Vimos en clase como hacerlo"),
            QA("""El valor de la Ganancia de Información (Information Gain) de un
atributo que toma siempre el mismo valor en todos los ejemplos es cero.""",
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
               "Verdadero. Las reglas de asociación son un modelo descriptivo.")
        ]

        super().__init__(title,instructions,qas)


class Concepts3(QAQuestion):

    def __init__(self):
        title = "Conceptos de Minería de Datos"
        instructions = "Responda las preguntas o indique el valor de verdad de las afirmaciones. Justifique sus respuestas en ambos casos."
        qas= [
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
            # QA("El algoritmo FPGrowth ¿genera reglas de Asociación?",
            #    "No, genera itemsets",),
            # QA("Al generar reglas con APriori o FPGrowth ¿es necesario generar itemsets?",
            #    "Si, justamente generan itemsets",),
            QA("Dado un conjunto de datos de 10 ejemplos con 2 columnas, una es la de la clase con 3 valores distintos, "
               "y la otra es un atributo nominal de 5 valores distintos. ¿Cuántos valores serán necesarios para almacenar un "
               "modelo Naive Bayes para clasificar los ejemplos?"
               ,"$3 \\times 5=15$, ya que para cada clase (3) debemos almacenar la distribución de probabilidad de los valores (5)"),
            QA("""Se tiene un problema de clasificación de 100 ejemplos con 2 columnas, una es la de la clase con 5 valores distintos,
               y la otra es de un atributo numérico con 20 valores distintos. 
               Si se entrena un modelo de Naive Bayes ¿cuántas distribuciones gaussianas se deberán estimar?""",
               "Se estima una gaussiana para cada clase, o sea, 5 gaussianas."),
            QA("Dado un conjunto de atributos, puede afirmarse que los que tengan el mismo valor de entropía también tendrán el mismo valor de Ganancia de Información (Information Gain).",
                "Verdadero, ya que I(A) = E - E(A) "
               ),
            QA("El índice Silhouette se calcula en base a la dispersión de los ejemplos de cada grupo (cluster) y la distancia entre los centros.",
               "Falso, solo entre ejemplos"
            ),
        ]

        super().__init__(title,instructions,qas)
