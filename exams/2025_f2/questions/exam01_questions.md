---
title: Minería de Datos usando Sistemas Inteligentes - Tema 3
author:  Fecha 2 - 18 de Junio de 2025 

date: 
geometry: margin=1.6cm
---


|Nombres&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Apellidos&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|DNI/N° Legajo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|#Hojas extra&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
|----------|----------|----------|----------|
|||||


El siguiente conjunto de datos tiene datos clínicos de personas que tuvieron COVID, incluyendo la cantidad de contactos estrechos, edad y presión de las personas, y si las mismas tuvieron compĺicaciones (CC) o no (SC).

**Tabla de datos**


| |Estrechos|Edad|Presión|Clase|
|----------|----------|----------|----------|----------|
|1|1|30|Media|SC|
|2|3|50|Media|SC|
|3|1|11|Baja|SC|
|4|4|51|Alta|CC|
|5|3|7|Baja|CC|
|6|4|35|Baja|SC|
|7|3|33|Baja|SC|
|8|1|33|Media|SC|


### 1. Modelo OneR
 Dada la siguiente discretización del conjunto de datos original, aplique el algoritmo OneR para encontrar el mejor atributo y las reglas asociadas para clasificar los ejemplos según el atributo Clase. 


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


Mostrar el accuracy de cada atributo, y las reglas finales del OneR:


||Estrechos|Edad|Presión|
|----------|----------|----------|----------|
|Accuracy||||



|Reglas con [atributo]|
|----------|
|...|


### 2. Métricas de Reglas
 Calcule el soporte, cobertura, confianza, e interés de las siguientes reglas:


|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Presión = Alta → Clase = CC|||||
|Clase = SC → Presión = Baja|||||
|Estrechos < 2 and Presión = Media → Edad < 31|||||


Presentar los resultados en forma de tabla, e incluir los cálculos realizados en la hoja.

### 3. Agrupamiento de datos - Cálculo de asignaciones
 Dado el siguiente conjunto de ejemplos numerizado, y dados los centroides **c1** y **c2**, calcule la distancia euclídea de los ejemplos hacia estos centroides, y a cuál de ellos estarían asignados. No utilizar la clase en este ejercicio.


| |Estrechos|Edad|Presión|Clase|
|----------|----------|----------|----------|----------|
|1|1|30|2|SC|
|2|3|50|2|SC|
|3|1|11|1|SC|



|Centroide|Estrechos|Edad|Presión|
|----------|----------|----------|----------|
|**c1**|1|33|1|
|**c2**|3|50|3|


Nota: Para presentar los resultados, no calcule las raíces cuadradas. En lugar de eso, deje expresadas las distancias como $\sqrt{valor}$. Utilice una tabla como la siguiente:


|Ejemplo|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|$\sqrt{valor}$|$\sqrt{valor}$|(c1 o c2)|
|...|...|...|...|


### 4. Agrupamiento de datos - Cálculo de centroides
 Dado el siguiente conjunto de ejemplos numerizado, calcule los valores de los 2 centroides numerados desde 0 hasta 1 usando la asignación provista. No utilizar la clase en este ejercicio. Este ejercicio es independiente del resto del examen. Utilice una tabla con 2 filas y tantas columnas como atributos haya para presentar los centroides resultantes.


| |Estrechos|Edad|Presión|Cluster Asignado|
|----------|----------|----------|----------|----------|
|1|3|7|1|1|
|2|4|35|1|1|
|3|3|33|1|0|
|4|1|33|2|0|


### 5. Conceptos de Minería de Datos
 Responda las preguntas o indique el valor de verdad de  las siguientes afirmaciones, y justifique sus respuestas. La justificación es necesaria en todos los casos para obtener puntaje.

a. Se tiene un problema de clasificación de 100 ejemplos con 3 columnas, una es la de la clase con 4 valores distintos, otra es nominal con 5 valores,
   y la otra es de un atributo numérico con 10 valores distintos. 
   Si se entrena un modelo de Naive Bayes ¿cuántas distribuciones gaussianas se deberán estimar?

b. ¿Cuál de las normalizaciones vistas es más sensible a los valores anómalos/extremos?

c. Un atributo nominal sólo aparecerá una vez en una misma regla generada con el método PART (recuerde que se generan como una rama de un árbol parcialmente construido con C4.5)

d. En el índice Silhouette, el clustering es perfecto cuando vale 0, y los valores extremos -1 y 1 indican desviaciones negativas y positivas del óptimo.

e. Dado un conjunto de datos con 6 clases, 6 atributos de entrada nominales, 1 atributo de entrada numérico y 650 ejemplos. Si se entrena un árbol de clasificación con este conjunto de datos ¿puedo saber cuántos nodos tendrá como máximo el árbol?

### 6. Ganancia de Información
 Utilizando los datos originales, calcule la entropía general del conjunto de datos en base al atributo de clase. Luego, calcule la entropía y ganancia de información para los atributos Estrechos y Presión. Tenga en cuenta que para los atributos numéricos deberá utilizar la variante del algoritmo que busca la mejor discretización probando todos los puntos de corte posibles. Utilice la siguiente tabla para presentar los resultados:


|Atributo|Estrechos|Presión|
|----------|----------|----------|
|Entropía| | |
|Ganancia de Información| | |


En base a estos valores, indique cuál de los 2 atributos se elegiría para generar la raíz de un árbol de decisión.
Utilice dos decimales para los cálculos. 
Utilice logaritmo con base 2 para todos los cálculos (obligatorio).

Logaritmos de base 2


| | | | | | | | |
|----------|----------|----------|----------|----------|----------|----------|----------|
|$log_{2}(1/2)$|$log_{2}(1/3)$|$log_{2}(2/3)$|$log_{2}(1/4)$|$log_{2}(2/4)$|$log_{2}(3/4)$|$log_{2}(1/5)$|$log_{2}(2/5)$|
|-1.000|-1.585|-0.585|-2.000|-1.000|-0.415|-2.322|-1.322|
|$log_{2}(3/5)$|$log_{2}(4/5)$|$log_{2}(1/6)$|$log_{2}(2/6)$|$log_{2}(3/6)$|$log_{2}(4/6)$|$log_{2}(5/6)$|$log_{2}(1/7)$|
|-0.737|-0.322|-2.585|-1.585|-1.000|-0.585|-0.263|-2.807|
|$log_{2}(2/7)$|$log_{2}(3/7)$|$log_{2}(4/7)$|$log_{2}(5/7)$|$log_{2}(6/7)$|$log_{2}(1/8)$|$log_{2}(2/8)$|$log_{2}(3/8)$|
|-1.807|-1.222|-0.807|-0.485|-0.222|-3.000|-2.000|-1.415|
|$log_{2}(4/8)$|$log_{2}(5/8)$|$log_{2}(6/8)$|$log_{2}(7/8)$|
|-1.000|-0.678|-0.415|-0.193|


### 7. Perceptrón
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[13, 1, 20]* (para los atributos Estrechos, Edad, Presión, respectivamente) y *sesgo=96*:

b) Asumiendo que Clase=CC está codificado con un 0, y Clase=SC con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Estrechos vale 3, Edad vale 50 y Presión vale 1?

a) Asumiendo que Clase=CC está codificado con un 0, y Clase=SC con un 1, ¿cuál es el valor máximo del atributo Estrechos  para que un ejemplo con Edad=50 y Presión=2 pertenezca a la Clase=SC?

### 8. Cuartiles
 Calcule la mediana y los dos cuartiles del atributo Estrechos.

 Nota: Utilice la definición de cuartil vista en la teoría.
