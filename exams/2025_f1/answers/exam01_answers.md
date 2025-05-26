---
title: Minería de Datos usando Sistemas Inteligentes - Tema 3 (Respuestas)
author:  Fecha 1 - 26 de Junio de 2025 

date: 
geometry: margin=1.6cm
---



### 1. Normalización de atributos (Puntos: 1)
 Normalización rango con transformación (x--17.00)/22.00

Valores normalizados: 0.55, 1.00, 0.09, 1.00, 0.00, 0.64, 0.59, 0.59

Normalización mu/std con transformación (x--4.75)/8.01

Valores normalizados: -0.03, 1.22, -1.28, 1.22, -1.53, 0.22, 0.09, 0.09

### 2. Discretización de atributos (Puntos: 1)
 Resultado de la discretización por rango:

Valores: ['Medio', 'Alto', 'Poco', 'Alto', 'Poco', 'Medio', 'Medio', 'Medio']

Intervalos: [[-17.0,-9.67), [-9.67,-2.33), [-2.33,5.0]]

Resultado de la discretización por frecuencia:

Valores: ['Poco', 'Alto', 'Poco', 'Alto', 'Poco', 'Alto', 'Medio', 'Medio']

Intervalos: [[-17,-4), [-4,-3), [-3,5]]

### 3. Modelo OneR (Puntos: 1)
 
|NVDI|Temperatura|Salinidad|Clase|
|----------|----------|----------|----------|
|Pocos|Poco|Media|Apto|
|Muchos|Alto|Media|Apto|
|Pocos|Poco|Baja|Apto|
|Muchos|Alto|Alta|No Apto|
|Muchos|Poco|Baja|No Apto|
|Muchos|Alto|Baja|Apto|
|Muchos|Medio|Baja|Apto|
|Pocos|Medio|Media|Apto|


Mejor atributo: Salinidad


|Reglas con NVDI (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|NVDI = Pocos → Clase = Apto|1.00|3|
|NVDI = Muchos → Clase = Apto|0.60|5|



|Reglas con Temperatura (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Temperatura = Alto → Clase = Apto|0.67|3|
|Temperatura = Poco → Clase = Apto|0.67|3|
|Temperatura = Medio → Clase = Apto|1.00|2|



|Reglas con Salinidad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Salinidad = Alta → Clase = No Apto|1.00|1|
|Salinidad = Baja → Clase = Apto|0.75|4|
|Salinidad = Media → Clase = Apto|1.00|3|


### 4. Métricas de Reglas (Puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Salinidad = Alta → Clase = No Apto|0.125|0.125|1.000|4.000|
|Clase = Apto → Salinidad = Baja|0.375|0.750|0.500|1.000|
|NVDI < 0 and Salinidad = Media → Temperatura < -5|0.000|0.250|0.000|0.000|


### 5. Agrupamiento de datos - Cálculo de asignaciones (Puntos: 1.5)
 
| |d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|2|102|1|
|2|83|1|2|
|3|121|405|1|


### 6. Agrupamiento de datos - Cálculo de centroides (Puntos: 1)
 
| |NVDI|Temperatura|Salinidad|Cluster Asignado|
|----------|----------|----------|----------|
|1|-0.5|-4|1.5|
|2|0.5|-10|1|


### 7. Conceptos de Minería de Datos (Puntos: 2)
 a. El algoritmo FPGrowth ¿genera reglas de Asociación?
 RESPUESTA:
No, FPGrowth genera itemsets

b. Los modelos de Reglas de Clasificación ¿son casos particulares de los modelos de Árboles de Clasificación?
 RESPUESTA:
Falso, es al revés, ya que todo árbol puede expresarse como un conjunto de reglas pero no viceversa.

c. Dadas dos reglas con valor de confianza=1 (perfectas) será más interesante la que tenga un menor valor de soporte para el consecuente.
 RESPUESTA:
V

d. El índice Silhouette siempre mejora a medida que se aumenta el número de clusters k
 RESPUESTA:
Falso, como el Silhouette depende también de la separación entre clusters, puede que decremente o que aumente si se tienen muchos clusters pequeños pero cercanos entre sí. 

e. Dado un conjunto de datos con 3 clases, y 3 atributos de entrada nominales, cada uno con 6 valores, y 9374 ejemplos. Si se entrena un árbol de clasificación con este conjunto de datos ¿puedo saber cuántas hojas tendrá como máximo el árbol?
 RESPUESTA:
VERDADERO. Como se sabe cuántos atributos hay y cuántos valores tiene cada uno, sabemos que en el peor de los casos, el arbol tendrá 6^3 hojas, ya que si el árbol llega al máximo de su complejidad, en cada nivel cada nodo se dividirá en 6 ramas. Además,se tiene la cantidad de ejemplos, con lo cual tampoco puede superar los 9374 nodos.

### 8. Ganancia de Información (Puntos: 2)
 Entropías calculadas con logaritmo con base 2

Entropía general: 0.8112781244591328


|Atributo|NVDI|Salinidad|
|----------|----------|----------|
|Entropía|0.74|0.41|
|Ganancia|0.07|0.41|



|NVDI: Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|-0.5|0.81|0|
|0.5|0.74|0.07|

