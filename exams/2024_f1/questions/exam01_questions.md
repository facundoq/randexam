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
|1|41|31|Tostado|Común|
|2|49|93|Tostado|Raro|
|3|20|20|Claro|Común|
|4|53|3|Tostado|Raro|
|5|31|98|Claro|Común|
|6|8|67|Oscuro|Raro|
|7|27|36|Claro|Común|
|8|51|34|Claro|Común|


### 1. Normalización de atributos
 Normalice el atributo Peso mediante: 

1. rango lineal uniforme (min/max)

2. media/varianza


Indicar los valores resultantes normalizados. 
 Nota: La normalización es solo para este ejercicio. Utilizar los datos originales en los siguientes.

### 2. Discretización de atributos
 Discretice el atributo Peso  por a) frecuencia y b) rango en los valores ['Bajo', 'Medio', 'Alto']. En ambos casos, indique los intervalos resultantes. Realice un gráfico de barras para visualizar la frecuencia de los valores resultantes.

 Nota: La discretización es solo para este ejercicio; utilizar los datos originales en el resto de los ejercicios.

### 3. Modelo OneR
 Dada la siguiente discretización del conjunto de datos original, aplique el algoritmo OneR para encontrar el mejor atributo y las reglas asociadas para clasificar los ejemplos según el atributo Clase. 


|Peso|Altura|Color|Clase|
|----------|----------|----------|----------|
|Medio|Bajo|Tostado|Común|
|Alto|Alto|Tostado|Raro|
|Bajo|Bajo|Claro|Común|
|Alto|Bajo|Tostado|Raro|
|Medio|Alto|Claro|Común|
|Bajo|Alto|Oscuro|Raro|
|Bajo|Alto|Claro|Común|
|Alto|Bajo|Claro|Común|


Mostrar el accuracy de cada atributo, y las reglas finales del OneR:


||Peso|Altura|Color|
|----------|----------|----------|----------|
|Accuracy||||



|Reglas con [atributo]|
|----------|
|...|


### 4. Cuartiles
 Calcule la mediana y los dos cuartiles del atributo Peso.

 Nota: Utilice la definición de cuartil vista en la teoría.

### 5. Métricas de Reglas
 Calcule el soporte, cobertura, confianza, e interés de las siguientes reglas:


|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Color = Claro → Clase = Común|||||
|Clase = Raro → Color = Claro|||||
|Peso < 35 and Color = Claro → Altura < 48|||||


Presentar los resultados en forma de tabla, e incluir los cálculos realizados en la hoja.

### 6. Agrupamiento de datos - Cálculo de asignaciones
 Dado el siguiente conjunto de ejemplos numerizado, y dados los centroides **c1** y **c2**, calcule la distancia euclídea de los ejemplos hacia estos centroides, y a cuál de ellos estarían asignados. No utilizar la clase en este ejercicio.


| |Peso|Altura|Color|Clase|
|----------|----------|----------|----------|----------|
|1|41|31|2|Común|
|2|49|93|2|Raro|
|3|20|20|1|Común|



|Centroide|Peso|Altura|Color|
|----------|----------|----------|----------|
|**c1**|27|34|1|
|**c2**|49|93|2|


Nota: Para presentar los resultados, no calcule las raíces cuadradas.En lugar de eso, deje expresada los distancias como $\sqrt{valor}$. Utilice una tabla como la siguiente:


|Ejemplo|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|$\sqrt{valor}$|$\sqrt{valor}$|(c1 o c2)|
|...|...|...|...|


### 7. Conceptos de Minería de Datos
 Responda las preguntas o indique el valor de verdad de  las siguientes afirmacione, y justifique sus respuestas. La justificación es necesaria en todos los casos para obtener puntaje.

a) Si se busca construir un árbol de clasificación, el atributo de clase (marcado como label) debe ser de tipo ordinal.

b) Es posible calcular la tasa de acierto (accuracy) de un conjunto de reglas de asociación.

c) La normalización lineal uniforme ¿es sensible a valores anómalos? ¿y la normalización por media/varianza?

d) Dado un conjunto de datos de 10 ejemplos con 2 columnas, una es la de la clase con 3 valores distintos, y la otra es un atributo nominal de 5 valores distintos. ¿Cuántos valores serán necesarios para almacenar un modelo Naive Bayes para clasificar los ejemplos?

e) Los modelos de Reglas de Clasificación ¿son casos particulares de los modelos de Árboles de Clasificación?

f) Dado un conjunto de datos con 3 clases, 5 atributos nominales y 100000 ejemplos. Si se entrena un árbol de clasificación con este conjunto de datos ¿puedo saber cuántos nodos tendrá como máximo el árbol?

g) Al generar reglas con APriori o FPGrowth ¿es necesario generar itemsets?

h) El peso de una red neuronal correspondiente al atributo A es negativo (por ejemplo, -10). Dado un ejemplo, si el valor del ejemplo para el atributo de A baja, ¿a qué clase se acercará el ejemplo?

### 8. Ganancia de Información
 Utilizando los datos originales, calcule la entropía general del conjunto de datos en base al atributo de clase. Luego, calcule la entropía y ganancia de información para los atributos Altura y Color. Tenga en cuenta que el atributo Altura es numérico, por lo cual deberá utilizar la variante del algoritmo que busca la mejor discretización probando todos los puntos de corte posibles.  Utilice la siguiente tabla para presentar los resultados:


|Atributo|Altura|Color|
|----------|----------|----------|
|Entropía| | |
|Ganancia de Información| | |


En base a estos valores, indique cuál de los 2 atributos se elegiría para generar la raíz de un árbol de decisión.
Utilice dos decimales para los cálculos. 
Recuerde que para los atributos numéricos debe calcular la ganancia de información de todos los puntos de corte.
Utilice logaritmo con base 2 para todos los cálculos (obligatorio).
