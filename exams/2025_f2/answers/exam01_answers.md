---
title: Minería de Datos usando Sistemas Inteligentes - Tema 3 (Respuestas)
author:  Fecha 2 - 18 de Junio de 2025 

date: 
geometry: margin=1.6cm
---



### 1. Modelo OneR (Puntos: 1)
 
|Estrechos|Edad|Presión|Clase|
|----------|----------|----------|----------|
|Pocos|Joven|Media|SC|
|Muchos|Adulta|Media|SC|
|Pocos|Joven|Baja|SC|
|Muchos|Adulta|Alta|CC|
|Muchos|Joven|Baja|CC|
|Muchos|Adulta|Baja|SC|
|Muchos|Mediana|Baja|SC|
|Pocos|Mediana|Media|SC|


Mejor atributo: Presión


|Reglas con Estrechos (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Estrechos = Pocos → Clase = SC|1.00|3|
|Estrechos = Muchos → Clase = SC|0.60|5|



|Reglas con Edad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Edad = Mediana → Clase = SC|1.00|2|
|Edad = Adulta → Clase = SC|0.67|3|
|Edad = Joven → Clase = SC|0.67|3|



|Reglas con Presión (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Presión = Media → Clase = SC|1.00|3|
|Presión = Baja → Clase = SC|0.75|4|
|Presión = Alta → Clase = CC|1.00|1|


### 2. Métricas de Reglas (Puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Presión = Alta → Clase = CC|0.125|0.125|1.000|4.000|
|Clase = SC → Presión = Baja|0.375|0.750|0.500|1.000|
|Estrechos < 2 and Presión = Media → Edad < 31|0.125|0.250|0.500|1.333|


### 3. Agrupamiento de datos - Cálculo de asignaciones (Puntos: 1.5)
 
| |d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|10|405|1|
|2|294|1|2|
|3|484|1529|1|


### 4. Agrupamiento de datos - Cálculo de centroides (Puntos: 1)
 
| |Estrechos|Edad|Presión|Cluster Asignado|
|----------|----------|----------|----------|
|1|2|33|1.5|
|2|3.5|21|1|


### 5. Conceptos de Minería de Datos (Puntos: 2)
 a. Se tiene un problema de clasificación de 100 ejemplos con 3 columnas, una es la de la clase con 4 valores distintos, otra es nominal con 5 valores,
   y la otra es de un atributo numérico con 10 valores distintos. 
   Si se entrena un modelo de Naive Bayes ¿cuántas distribuciones gaussianas se deberán estimar?
 RESPUESTA:
Se estima una gaussiana para cada clase, o sea, 4 gaussianas.

b. ¿Cuál de las normalizaciones vistas es más sensible a los valores anómalos/extremos?
 RESPUESTA:
La lineal, ya que si hay un valor extremo afecta al máximo/mínimo directamente.

c. Un atributo nominal sólo aparecerá una vez en una misma regla generada con el método PART (recuerde que se generan como una rama de un árbol parcialmente construido con C4.5)
 RESPUESTA:
V

d. En el índice Silhouette, el clustering es perfecto cuando vale 0, y los valores extremos -1 y 1 indican desviaciones negativas y positivas del óptimo.
 RESPUESTA:
Falso, como el indice se define como (b(i)-a(i))/max(b(i),a(i)), donde b es la distancia inter cluster promedio y a es la intracluster, entonces si vale 1 quiere decir que la distancia intercluster es grande y la intracluster es baja

e. Dado un conjunto de datos con 6 clases, 6 atributos de entrada nominales, 1 atributo de entrada numérico y 650 ejemplos. Si se entrena un árbol de clasificación con este conjunto de datos ¿puedo saber cuántos nodos tendrá como máximo el árbol?
 RESPUESTA:
Como hay un atributo numérico, se pueden generar nodos infinitamente. Por eso, la cantidad máxima sería igual al número de ejemplos, 650.

### 6. Ganancia de Información (Puntos: 2)
 Entropías calculadas con logaritmo con base 2

Entropía general: 0.8112781244591328


|Atributo|Estrechos|Presión|
|----------|----------|----------|
|Entropía|0.61|0.41|
|Ganancia|0.20|0.41|



|Estrechos: Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|2|0.61|0.2|
|3.5|0.74|0.07|


### 7. Perceptrón (Puntos: 1.5)
 b) Asumiendo que Clase=CC está codificado con un 0, y Clase=SC con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Estrechos vale 3, Edad vale 50 y Presión vale 1?

La salida neta es 13×3+1×50+20×1 =109, y por ende la salida es 1 (109>=96), con clase SC

a) Asumiendo que Clase=CC está codificado con un 0, y Clase=SC con un 1, ¿cuál es el valor máximo del atributo Estrechos  para que un ejemplo con Edad=50 y Presión=2 pertenezca a la Clase=SC?

Recordamos que w=13, 1, 20 y b=96

Dados esos valores, y asumiendo que $a_0$, $a_1$ y $a_2$ son los valores para los atributos Estrechos, Edad, Presión, para que el modelo esté entre generar 0 o 1 debe cumplirse:

$a_0 . w0 + a_1 . w_1 + a_2 . w_2 = b$

$a_0 . w0 = b - a_1 . w_1 - a_2 . w_2$

$a_0  = (b - a_1 . w_1 - a_2 . w_2)/w_0$

$a_0  = (96 - 50 . 1 - 2 20)/13$

$a_0 = 0.46153846153846156$

Como buscamos que esté en clase SC, y el signo de $w_0$ es positivo, necesitamos que $a_0$ tenga como valor máximo 0.46153846153846156.

### 8. Cuartiles (Puntos: 1)
 Valores ordenados de  Estrechos:

[1.0, 1.0, 1.0, 3.0, 3.0, 3.0, 4.0, 4.0]

Índices de los cuartiles:

2.25, 4.5, 6.75

Cuartiles:

q1=1.0, q2=3.0, q3=3.75
