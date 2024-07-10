---
title: Minería de Datos usando Sistemas Inteligentes - Tema 2
author:  Fecha 3 - 12 de Julio de 2024 

date: 
geometry: margin=1.6cm
---


|Nombres&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Apellidos&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|DNI/N° Legajo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|#Hojas&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
|----------|----------|----------|----------|
|||||


El siguiente conjunto de datos detalla estadísticas de equipos de fútbol, y si los mismos clasificaron para un torneo.

**Tabla de datos**


| |Goles|Pases|Tipo|Clase|
|----------|----------|----------|----------|----------|
|1|1|55|Normal|Clasifica|
|2|3|86|Normal|No Clasifica|
|3|1|49|Novato|Clasifica|
|4|4|41|Normal|No Clasifica|
|5|3|91|Novato|Clasifica|
|6|4|73|Preferido|No Clasifica|
|7|3|57|Novato|Clasifica|
|8|1|56|Novato|Clasifica|


### 1. Normalización de atributos
 Normalice el atributo Pases mediante: 

1. rango lineal uniforme (min/max)

2. media/desviación


 Como ayuda, te damos el valor de la media, $\mu=63.50$, y la desviación estándar, $\sigma=17.89$.
Indicar las ecuaciones utilizadas, y los valores resultantes normalizados. Inteprete los valores normalizados obtenidos para Pases=41. Para el rango lineal uniforme (min/max), indique qué significa en la escala 0-1.
 Para la normalización media/varianza, indique qué significa en relación a estos valores.
 

 Estas normalizaciones ¿Son equivalentes? ¿A qué valor de la normalización min/max corresponde la media de los valores?. Justifique. 

 Nota: La normalización es solo para este ejercicio. Utilizar los datos originales en el resto de los ejercicios.

### 2. Discretización de atributos
 Discretice el atributo Pases  por a) frecuencia y b) rango en los valores ['Poco', 'Medio', 'Alto']. En ambos casos, indique los intervalos resultantes. Realice un gráfico de barras para visualizar la frecuencia de los valores resultantes.

 Nota: La discretización es solo para este ejercicio; utilizar los datos originales en el resto de los ejercicios.

### 3. Modelo OneR
 Dada la siguiente discretización del conjunto de datos original, aplique el algoritmo OneR para encontrar el mejor atributo y las reglas asociadas para clasificar los ejemplos según el atributo Clase. 


|Goles|Pases|Tipo|Clase|
|----------|----------|----------|----------|
|Pocos|Poco|Normal|Clasifica|
|Muchos|Alto|Normal|No Clasifica|
|Pocos|Poco|Novato|Clasifica|
|Muchos|Poco|Normal|No Clasifica|
|Muchos|Alto|Novato|Clasifica|
|Muchos|Alto|Preferido|No Clasifica|
|Muchos|Medio|Novato|Clasifica|
|Pocos|Medio|Novato|Clasifica|


Mostrar el accuracy de cada atributo, y las reglas finales del OneR:


||Goles|Pases|Tipo|
|----------|----------|----------|----------|
|Accuracy||||



|Reglas con [atributo]|
|----------|
|...|


### 4. Métricas de Reglas
 Calcule el soporte, cobertura, confianza, e interés de las siguientes reglas:


|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Tipo = Normal → Clase = Clasifica|||||
|Clase = No Clasifica → Tipo = Novato|||||
|Goles < 2 and Tipo = Novato → Pases < 64|||||


Presentar los resultados en forma de tabla, e incluir los cálculos realizados en la hoja.

### 5. Agrupamiento de datos - Cálculo de asignaciones
 Dado el siguiente conjunto de ejemplos numerizado, y dados los centroides **c1** y **c2**, calcule la distancia euclídea de los ejemplos hacia estos centroides, y a cuál de ellos estarían asignados. No utilizar la clase en este ejercicio.


| |Goles|Pases|Tipo|Clase|
|----------|----------|----------|----------|----------|
|1|1|55|2|Clasifica|
|2|3|86|2|No Clasifica|
|3|1|49|1|Clasifica|



|Centroide|Goles|Pases|Tipo|
|----------|----------|----------|----------|
|**c1**|1|56|1|
|**c2**|3|86|2|


Nota: Para presentar los resultados, no calcule las raíces cuadradas. En lugar de eso, deje expresadas las distancias como $\sqrt{valor}$. Utilice una tabla como la siguiente:


|Ejemplo|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|$\sqrt{valor}$|$\sqrt{valor}$|(c1 o c2)|
|...|...|...|...|


### 6. Agrupamiento de datos - Cálculo de centroides
 Dado el siguiente conjunto de ejemplos numerizado, calcule los valores de los 2 centroides numerados desde 0 hasta 1 usando la asignación provista. No utilizar la clase en este ejercicio. Este ejercicio es independiente del resto del examen. Utilice una tabla con 2 filas y tantas columnas como atributos haya para presentar los centroides resultantes.


| |Goles|Pases|Tipo|Cluster Asignado|
|----------|----------|----------|----------|----------|
|1|3|91|1|1|
|2|4|73|3|1|
|3|3|57|1|0|
|4|1|56|1|0|


### 7. Conceptos de Minería de Datos
 Responda las preguntas o indique el valor de verdad de  las siguientes afirmaciones, y justifique sus respuestas. La justificación es necesaria en todos los casos para obtener puntaje.

a. Es posible calcular la mediana de un atributo ordinal

b. El valor de la Ganancia de Información (Information Gain) de un atributo que toma siempre el mismo valor en todos los ejemplos es cero.

c. No es posible calcular la Tasa de Ganancia (Gain Ratio) de un atributo numérico continuo (con decimales).

d. Es posible que al representar el diagrama de barras de un atributo discretizado por frecuencia se observen barras con alturas diferentes.

### 8. Ganancia de Información
 Utilizando los datos originales, calcule la entropía general del conjunto de datos en base al atributo de clase. Luego, calcule la entropía y ganancia de información para los atributos Goles y Tipo. Tenga en cuenta que para los atributos numéricos deberá utilizar la variante del algoritmo que busca la mejor discretización probando todos los puntos de corte posibles. Utilice la siguiente tabla para presentar los resultados:


|Atributo|Goles|Tipo|
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

