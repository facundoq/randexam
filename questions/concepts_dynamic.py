from test_generator.exam import QA
from numpy import random

class TreeSizeUnknownQA(QA):
    @classmethod
    def random(cls):
        return TreeSizeUnknownQA(random.randint(2,10),random.randint(3,7),random.randint(100,1000))
    def __init__(self,classes:int,nominal:int,samples:int):
        
        self.q=f"Dado un conjunto de datos con {classes} clases, {nominal} atributos de entrada nominales y {samples} ejemplos. Si se entrena un árbol de clasificación con este conjunto de datos, y solo dispongo esta información ¿puedo saber cuántas hojas tendrá como máximo el árbol?"
        self.a=f"Si, pero como no se sabe cuantos valores tiene cada atributo nominal, la cantidad máxima sería igual al número de ejemplos, {samples}."


class TreeSizeNumericQA(QA):
    @classmethod
    def random(cls):
        return TreeSizeNumericQA(random.randint(2,10),random.randint(3,7),random.randint(10,100)*10)
    def __init__(self,classes:int,nominal:int,samples:int):
        
        self.q=f"Dado un conjunto de datos con {classes} clases, {nominal} atributos de entrada nominales, 1 atributo de entrada numérico y {samples} ejemplos. Si se entrena un árbol de clasificación con este conjunto de datos ¿puedo saber cuántos nodos tendrá como máximo el árbol?"
        self.a=f"Como hay un atributo numérico, se pueden generar nodos infinitamente. Por eso, la cantidad máxima sería igual al número de ejemplos, {samples}."

class TreeSizeNominalQA(QA):
    @classmethod
    def random(cls):
        nominal = random.randint(3,5)
        values = nominal+ random.randint(1,6)
        return TreeSizeNominalQA(random.randint(2,10),nominal,values,random.randint(100,10000))
    def __init__(self,classes:int,nominal:int,values:int,samples:int):
        
        self.q=f"Dado un conjunto de datos con {classes} clases, y {nominal} atributos de entrada nominales, cada uno con {values} valores, y {samples} ejemplos. Si se entrena un árbol de clasificación con este conjunto de datos ¿puedo saber cuántas hojas tendrá como máximo el árbol?"
        self.a=f"VERDADERO. Como se sabe cuántos atributos hay y cuántos valores tiene cada uno, sabemos que en el peor de los casos, el arbol tendrá {values}^{nominal} hojas, ya que si el árbol llega al máximo de su complejidad, en cada nivel cada nodo se dividirá en {values} ramas. Además,se tiene la cantidad de ejemplos, con lo cual tampoco puede superar los {samples} nodos."

class NBNominalValuesQA(QA):
    @classmethod
    def random(cls):
        nominal = random.randint(3,5)
        values = nominal+ random.randint(1,6)
        return NBNominalValuesQA(random.randint(2,10),nominal,values,random.randint(100,1000))
    def __init__(self,classes:int,nominal:int,values:int,samples:int):
        
        self.q=f"Dado un conjunto de datos de 5 {samples} con {nominal} atributos nominales, donde uno de ellos es la de la clase con {classes} valores distintos, y los otros son atributos nominales de {values} valores distintos. ¿Cuántos valores serán necesarios para almacenar un modelo de Naive Bayes entrenado con ese conjunto de datos?."
        self.a=f" {classes} \\times {nominal}  \\times  ${values} ={classes*nominal*values}$, ya que para cada clase y cada atributo debemos almacenar la distribución de probabilidad de los valores, o sea, una probabilidad por cada valor."