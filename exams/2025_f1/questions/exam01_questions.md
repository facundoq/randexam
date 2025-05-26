---
title: Minería de Datos usando Sistemas Inteligentes - Tema 3
author:  Fecha 1 - 26 de Junio de 2025 

date: 
geometry: margin=1.6cm
---


|Nombres&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Apellidos&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|DNI/N° Legajo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|#Hojas&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
|----------|----------|----------|----------|
|||||


El siguiente conjunto de datos detalla estadísticas de mallines, que son humedales de la patagonia, y si los mismos son aptos para la pastura de ovejas. El atributo NDVI es el Normalized Difference Vegetation Index o Índice Normalizado de Diferencia de Vegetación.

**Tabla de datos**


| |NVDI|Temperatura|Salinidad|Clase|
|----------|----------|----------|----------|----------|
|1|-1|-5|Media|Apto|
|2|0|5|Media|Apto|
|3|-1|-15|Baja|Apto|
|4|1|5|Alta|No Apto|
|5|0|-17|Baja|No Apto|
|6|1|-3|Baja|Apto|
|7|0|-4|Baja|Apto|
|8|-1|-4|Media|Apto|


### 1. Normalización de atributos
 Normalice el atributo Temperatura mediante: 

1. rango lineal uniforme (min/max)

2. media/desviación


 Como ayuda, te damos el valor de la media, $\mu=-4.75$, y la desviación estándar, $\sigma=8.01$.
Indicar las ecuaciones utilizadas, y los valores resultantes normalizados. Inteprete los valores normalizados obtenidos para Temperatura=5. Para el rango lineal uniforme (min/max), indique qué significa en la escala 0-1.
 Para la normalización media/varianza, indique qué significa en relación a estos valores.
 

 Estas normalizaciones ¿Son equivalentes? ¿A qué valor de la normalización min/max corresponde la media de los valores?. Justifique. 

 Nota: La normalización es solo para este ejercicio. Utilizar los datos provistos en el resto de los ejercicios.

### 2. Discretización de atributos
 Discretice el atributo Temperatura  por a) frecuencia y b) rango en los valores ['Poco', 'Medio', 'Alto']. En ambos casos, indique los intervalos resultantes. Realice un gráfico de barras para visualizar la frecuencia de los valores resultantes.

 Nota: La discretización es solo para este ejercicio; utilizar los datos provistos en el resto de los ejercicios.

### 3. Modelo OneR
 Dada la siguiente discretización del conjunto de datos original, aplique el algoritmo OneR para encontrar el mejor atributo y las reglas asociadas para clasificar los ejemplos según el atributo Clase. 


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


Mostrar el accuracy de cada atributo, y las reglas finales del OneR:


||NVDI|Temperatura|Salinidad|
|----------|----------|----------|----------|
|Accuracy||||



|Reglas con [atributo]|
|----------|
|...|


### 4. Métricas de Reglas
 Calcule el soporte, cobertura, confianza, e interés de las siguientes reglas:


|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Salinidad = Alta → Clase = No Apto|||||
|Clase = Apto → Salinidad = Baja|||||
|NVDI < 0 and Salinidad = Media → Temperatura < -5|||||


Presentar los resultados en forma de tabla, e incluir los cálculos realizados en la hoja.

### 5. Agrupamiento de datos - Cálculo de asignaciones
 Dado el siguiente conjunto de ejemplos numerizado, y dados los centroides **c1** y **c2**, calcule la distancia euclídea de los ejemplos hacia estos centroides, y a cuál de ellos estarían asignados. No utilizar la clase en este ejercicio.


| |NVDI|Temperatura|Salinidad|Clase|
|----------|----------|----------|----------|----------|
|1|-1|-5|2|Apto|
|2|0|5|2|Apto|
|3|-1|-15|1|Apto|



|Centroide|NVDI|Temperatura|Salinidad|
|----------|----------|----------|----------|
|**c1**|-1|-4|1|
|**c2**|0|5|3|


Nota: Para presentar los resultados, no calcule las raíces cuadradas. En lugar de eso, deje expresadas las distancias como $\sqrt{valor}$. Utilice una tabla como la siguiente:


|Ejemplo|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|$\sqrt{valor}$|$\sqrt{valor}$|(c1 o c2)|
|...|...|...|...|


### 6. Agrupamiento de datos - Cálculo de centroides
 Dado el siguiente conjunto de ejemplos numerizado, calcule los valores de los 2 centroides numerados desde 0 hasta 1 usando la asignación provista. No utilizar la clase en este ejercicio. Este ejercicio es independiente del resto del examen. Utilice una tabla con 2 filas y tantas columnas como atributos haya para presentar los centroides resultantes.


| |NVDI|Temperatura|Salinidad|Cluster Asignado|
|----------|----------|----------|----------|----------|
|1|0|-17|1|1|
|2|1|-3|1|1|
|3|0|-4|1|0|
|4|-1|-4|2|0|


### 7. Conceptos de Minería de Datos
 Responda las preguntas o indique el valor de verdad de  las siguientes afirmaciones, y justifique sus respuestas. La justificación es necesaria en todos los casos para obtener puntaje.

a. El algoritmo FPGrowth ¿genera reglas de Asociación?

b. Los modelos de Reglas de Clasificación ¿son casos particulares de los modelos de Árboles de Clasificación?

c. Dadas dos reglas con valor de confianza=1 (perfectas) será más interesante la que tenga un menor valor de soporte para el consecuente.

d. El índice Silhouette siempre mejora a medida que se aumenta el número de clusters k

e. Dado un conjunto de datos con 3 clases, y 3 atributos de entrada nominales, cada uno con 6 valores, y 9374 ejemplos. Si se entrena un árbol de clasificación con este conjunto de datos ¿puedo saber cuántas hojas tendrá como máximo el árbol?

### 8. Ganancia de Información
 Utilizando los datos originales, calcule la entropía general del conjunto de datos en base al atributo de clase. Luego, calcule la entropía y ganancia de información para los atributos NVDI y Salinidad. Tenga en cuenta que para los atributos numéricos deberá utilizar la variante del algoritmo que busca la mejor discretización probando todos los puntos de corte posibles. Utilice la siguiente tabla para presentar los resultados:


|Atributo|NVDI|Salinidad|
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

