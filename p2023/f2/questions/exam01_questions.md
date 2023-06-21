---
title: Minería de Datos usando Sistemas Inteligentes - Tema 2
author:  Fecha 2 - 23 de Junio de 2023 

date: 
geometry: margin=1.6cm
---

**Puntaje total:** ___ /10


|Nombres&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Apellidos&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|DNI/N° Legajo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|#Hojas&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
|----------|----------|----------|----------|
|||||


**Tabla de datos**


| |Días |Llanto|Leche|Clase|
|----------|----------|----------|----------|----------|
|1|71|4|Materna|Cólicos|
|2|55|6|Fórmula|Otro|
|3|51|2|Fórmula|Cólicos|
|4|27|8|Mixta|Cólicos|
|5|46|4|Fórmula|Otro|
|6|45|9|Fórmula|Otro|
|7|49|7|Fórmula|Cólicos|
|8|42|4|Fórmula|Cólicos|


### 1. Normalización de atributos
 **Puntaje:** 	 &nbsp;&nbsp;&nbsp;    /1

 Normalice el atributo Días  mediante: 

1. rango lineal uniforme (min/max)

2. media/varianza


Indicar los valores resultantes normalizados. 
 Nota: La normalización es solo para este ejercicio. Utilizar los datos originales en los siguientes.

### 2. Modelo OneR
 **Puntaje:** 	 &nbsp;&nbsp;&nbsp;    /1

 Dada la siguiente discretización del conjunto de datos original, aplique el algoritmo OneR para encontrar el mejor atributo y las reglas asociadas para clasificar los ejemplos según el atributo Clase. 


|Días |Llanto|Leche|Clase|
|----------|----------|----------|----------|
|Alto|Leve|Materna|Cólicos|
|Alto|Grave|Fórmula|Otro|
|Alto|Leve|Fórmula|Cólicos|
|Bajo|Grave|Mixta|Cólicos|
|Medio|Leve|Fórmula|Otro|
|Bajo|Grave|Fórmula|Otro|
|Medio|Grave|Fórmula|Cólicos|
|Bajo|Leve|Fórmula|Cólicos|


Mostrar el accuracy de cada atributo, y las reglas finales del OneR:


||Días |Llanto|Leche|
|----------|----------|----------|----------|
|Accuracy||||



|Reglas con [atributo]|
|----------|
|...|


### 3. Cuartiles
 **Puntaje:** 	 &nbsp;&nbsp;&nbsp;    /1

 Calcule la mediana y los dos cuartiles del atributo Días .

 Nota: Utilice la definición de cuartil vista en la teoría.

### 4. Métricas de Reglas
 **Puntaje:** 	 &nbsp;&nbsp;&nbsp;    /1

 Calcule el soporte, cobertura, confianza, e interés de las siguientes reglas:


|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Leche = Fórmula → Clase = Cólicos|||||
|Clase = Otro → Leche = Fórmula|||||
|Días  < 48 and Leche = Fórmula → Llanto < 6|||||


Presentar los resultados en forma de tabla, e incluir los cálculos realizados en la hoja.

### 5. Agrupamiento de datos - Cálculo de centroides
 **Puntaje:** 	 &nbsp;&nbsp;&nbsp;    /1

 Dado el siguiente conjunto de ejemplos numerizado, calcule los valores de los 2 centroides numerados desde 0 hasta 1 usando la asignación provista. No utilizar la clase en este ejercicio. Este ejercicio es independiente del resto del examen. Utilice una tabla con 2 filas y tantas columnas como atributos haya para presentar los centroides resultantes.


| |Días |Llanto|Leche|Cluster Asignado|
|----------|----------|----------|----------|----------|
|1|46|4|3|0|
|2|45|9|3|1|
|3|49|7|3|0|
|4|42|4|3|1|


### 6. Conceptos de Minería de Datos
 **Puntaje:** 	 &nbsp;&nbsp;&nbsp;    /2

 Responda las preguntas o indique el valor de verdad de  las siguientes afirmaciones. Justifique sus respuestas.

a) Se corre el algoritmo K-Medias sobre un conjunto de datos, encontrando algunos clusters con 1 solo ejemplo. Esto ¿indica que el algoritmo no pudo converger?

b) Dado un conjunto de datos con 3 clases, 5 atributos nominales y 100000 ejemplos. Si se entrena un árbol de clasificación con este conjunto de datos ¿puedo saber cuántos nodos tendrá como máximo el árbol?

c) Dado un conjunto de atributos, puede afirmarse que los que tengan el mismo valor de entropía también tendrán el mismo valor de Ganancia de Información (Information Gain).

d) El algoritmo FPGrowth ¿genera reglas de Asociación?

e) El peso de una red neuronal correspondiente al atributo A es negativo (por ejemplo, -10). Dado un ejemplo, si el valor del ejemplo para el atributo de A baja, ¿a qué clase se acercará el ejemplo?

f) Es preciso conocer la posición de los centros para calcular el índice Davies-Bouldin de un agrupamiento.

g) La normalización lineal uniforme ¿es sensible a valores anómalos? ¿y la normalización por media/varianza?

h) Los modelos de Reglas de Clasificación ¿son casos particulares de los modelos de Árboles de Clasificación?

### 7. Ganancia de Información
 **Puntaje:** 	 &nbsp;&nbsp;&nbsp;    /2

 Utilizando los datos originales, calcule la entropía general del conjunto de datos en base al atributo de clase. Luego, calcule la entropía y ganancia de información para los atributos Llanto y Leche. Tenga en cuenta que el atributo Llanto es numérico.  Utilice la siguiente tabla para presentar los resultados:


|Atributo|Llanto|Leche|
|----------|----------|----------|
|Entropía| | |
|Ganancia de Información| | |


En base a estos valores, indique cuál de los 2 atributos se elegiría para generar la raíz de un árbol de decisión.
Utilice dos decimales para los cálculos. 
Recuerde que para los atributos numéricos debe calcular la ganancia de información de todos los puntos de corte.
Utilice logaritmo con base 2 para todos los cálculos (obligatorio).

### 8. Perceptrón
 **Puntaje:** 	 &nbsp;&nbsp;&nbsp;    /1

 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[1, 9, 19]* (para los atributos Días , Llanto, Leche, respectivamente) y *sesgo=147*:

a) Asumiendo que Clase=Cólicos está codificado con un 0, y Clase=Otro con un 1, ¿cuál es el valor máximo del atributo Días   para que un ejemplo con Llanto=2 y Leche=1 pertenezca a la Clase=Otro?

b) Asumiendo que Clase=Cólicos está codificado con un 0, y Clase=Otro con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Días  vale 49, Llanto vale 7 y Leche vale 3?
