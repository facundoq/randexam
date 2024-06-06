---
title: Minería de Datos usando Sistemas Inteligentes - Tema 2
author:  Fecha 1 - 7 de Junio de 2024 

date: 
geometry: margin=1.6cm
---


|Nombres&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Apellidos&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|DNI/N° Legajo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|#Hojas&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
|----------|----------|----------|----------|
|||||


**Tabla de datos**


| |Peso|Altura|Color|Clase|
|----------|----------|----------|----------|----------|
|1|86|60|Tostado|Común|
|2|41|80|Tostado|Común|
|3|72|41|Claro|Común|
|4|83|81|Oscuro|Raro|
|5|79|37|Claro|Raro|
|6|83|65|Claro|Común|
|7|136|63|Claro|Común|
|8|79|63|Tostado|Común|


### 1. Normalización de atributos
 Normalice el atributo Peso mediante: 

1. rango lineal uniforme (min/max)

2. media/varianza


Indicar las ecuaciones utilizadas, y los valores resultantes normalizados.Inteprete los valores normalizados obtenidos para Peso=83. Para el rango lineal uniforme (min/max), indique qué significa en la escala 0-1.
 Para la normalización media/varianza, indique qué significa en relación a estos valores.
 

 Estas normalizaciones ¿Son equivalentes? ¿A qué valor de la normalización min/max corresponde la media de los valores?. Justifique. 

 Nota: La normalización es solo para este ejercicio. Utilizar los datos originales en los siguientes.

### 2. Modelo OneR
 Dada la siguiente discretización del conjunto de datos original, aplique el algoritmo OneR para encontrar el mejor atributo y las reglas asociadas para clasificar los ejemplos según el atributo Clase. 


|Peso|Altura|Color|Clase|
|----------|----------|----------|----------|
|Alto|Bajo|Tostado|Común|
|Bajo|Alto|Tostado|Común|
|Bajo|Bajo|Claro|Común|
|Alto|Alto|Oscuro|Raro|
|Medio|Bajo|Claro|Raro|
|Alto|Alto|Claro|Común|
|Alto|Alto|Claro|Común|
|Medio|Alto|Tostado|Común|


Mostrar el accuracy de cada atributo, y las reglas finales del OneR:


||Peso|Altura|Color|
|----------|----------|----------|----------|
|Accuracy||||



|Reglas con [atributo]|
|----------|
|...|


### 3. Métricas de Reglas
 Calcule el soporte, cobertura, confianza, e interés de las siguientes reglas:


|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Color = Oscuro → Clase = Raro|||||
|Clase = Común → Color = Claro|||||
|Peso < 82 and Color = Tostado → Altura < 61|||||


Presentar los resultados en forma de tabla, e incluir los cálculos realizados en la hoja.

### 4. Agrupamiento de datos - Cálculo de asignaciones
 Dado el siguiente conjunto de ejemplos numerizado, y dados los centroides **c1** y **c2**, calcule la distancia euclídea de los ejemplos hacia estos centroides, y a cuál de ellos estarían asignados. No utilizar la clase en este ejercicio.


| |Peso|Altura|Color|Clase|
|----------|----------|----------|----------|----------|
|1|86|60|2|Común|
|2|41|80|2|Común|
|3|72|41|1|Común|



|Centroide|Peso|Altura|Color|
|----------|----------|----------|----------|
|**c1**|79|63|1|
|**c2**|83|80|3|


Nota: Para presentar los resultados, no calcule las raíces cuadradas. En lugar de eso, deje expresadas las distancias como $\sqrt{valor}$. Utilice una tabla como la siguiente:


|Ejemplo|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|$\sqrt{valor}$|$\sqrt{valor}$|(c1 o c2)|
|...|...|...|...|


### 5. Conceptos de Minería de Datos
 Responda las preguntas o indique el valor de verdad de  las siguientes afirmacione, y justifique sus respuestas. La justificación es necesaria en todos los casos para obtener puntaje.

a) Si se busca construir un árbol de clasificación, el atributo de clase (marcado como label) debe ser de tipo ordinal.

b)  Dada una regla de asociación, la principal métrica para saber si es buena o mala es la tasa de acierto (accuracy) .

c) La normalización lineal uniforme ¿es sensible a valores anómalos? ¿y la normalización por media/varianza?

d) Dado un conjunto de datos de 10 ejemplos con 2 columnas, una es la de la clase con 3 valores distintos, y la otra es un atributo nominal de 5 valores distintos. ¿Cuántos valores serán necesarios para almacenar un modelo Naive Bayes para clasificar los ejemplos?

e) Los modelos de Reglas de Clasificación ¿son casos particulares de los modelos de Árboles de Clasificación?

f) Al generar reglas de asociación, los algoritmos  APriori o FPGrowth ¿generan las reglas?

g) El peso de una red neuronal correspondiente al atributo A es negativo (por ejemplo, -10). Dado un ejemplo, si el valor del ejemplo para el atributo de A baja, ¿a qué clase se acercará el ejemplo?

h) Dado un conjunto de datos con 3 clases, y 3 atributos de entrada nominales, cada uno con 6 valores, y 158 ejemplos. Si se entrena un árbol de clasificación con este conjunto de datos ¿puedo saber cuántas hojas tendrá como máximo el árbol?

### 6. Diagrama de Caja
 Calcule los cuartiles, el rango intercuartil, los valores de los bigotes, y los rangos de valores atípicos leves y extremos dados por el diagrama de caja del atributo  Peso. Dibuje el diagrama.

 Nota: Utilice la definición de cuartil vista en la teoría. Presente los valores calculados como una tabla.

### 7. Ganancia de Información
 Utilizando los datos originales, calcule la entropía general del conjunto de datos en base al atributo de clase. Luego, calcule la entropía y ganancia de información para los atributos Altura y Color. Tenga en cuenta que el atributo Altura es numérico, por lo cual deberá utilizar la variante del algoritmo que busca la mejor discretización probando todos los puntos de corte posibles.  Utilice la siguiente tabla para presentar los resultados:


|Atributo|Altura|Color|
|----------|----------|----------|
|Entropía| | |
|Ganancia de Información| | |


En base a estos valores, indique cuál de los 2 atributos se elegiría para generar la raíz de un árbol de decisión.
Utilice dos decimales para los cálculos. 
Recuerde que para los atributos numéricos debe calcular la ganancia de información de todos los puntos de corte.
Utilice logaritmo con base 2 para todos los cálculos (obligatorio).

Algunos de logaritmos base 2 (use su calculadora para otros):


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

