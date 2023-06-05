---
title: Minería de Datos usando Sistemas Inteligentes - Tema 2
author:  Primera Fecha - 9 de Junio de 2023 - Promoción

date: 
geometry: margin=1.6cm
---

**Puntaje total:** ___ /10


|Nombres&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Apellidos&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|DNI/N° Legajo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|#Hojas&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
|----------|----------|----------|----------|
|||||


**Tabla de datos**


| |Visión |Dolor|Diabetes|Clase|
|----------|----------|----------|----------|----------|
|1|44|1|Tipo 1|Normal|
|2|49|6|Tipo 1|Retinopatía|
|3|24|5|Gestacional|Normal|
|4|69|1|Gestacional|Normal|
|5|28|7|Gestacional|Retinopatía|
|6|39|9|Tipo 2|Retinopatía|
|7|56|9|Tipo 2|Normal|
|8|35|1|Tipo 2|Retinopatía|


### 1. Discretización de atributos
 **Puntaje:** 	 &nbsp;&nbsp;&nbsp;    /1

 Discretice el atributo Visión   por a) frecuencia y b) rango en los valores ['Bajo', 'Alto']. En ambos casos, indique los intervalos resultantes. Realice un gráfico de barras para visualizar la frecuencia de los valores resultantes.

 Nota: La discretización es solo para este ejercicio; utilizar los datos originales en el resto de los ejercicios.

### 2. Modelo OneR
 **Puntaje:** 	 &nbsp;&nbsp;&nbsp;    /1

 Dada la siguiente discretización del conjunto de datos original, aplique el algoritmo OneR para encontrar el mejor atributo y las reglas asociadas para clasificar los ejemplos según el atributo Clase. 


|Visión |Dolor|Diabetes|Clase|
|----------|----------|----------|----------|
|Medio|Leve|Tipo 1|Normal|
|Alto|Grave|Tipo 1|Retinopatía|
|Bajo|Leve|Gestacional|Normal|
|Alto|Leve|Gestacional|Normal|
|Bajo|Grave|Gestacional|Retinopatía|
|Medio|Grave|Tipo 2|Retinopatía|
|Alto|Grave|Tipo 2|Normal|
|Bajo|Leve|Tipo 2|Retinopatía|


Mostrar el accuracy de cada atributo, y las reglas finales del OneR:


||Visión |Dolor|Diabetes|
|----------|----------|----------|----------|
|Accuracy||||



|Reglas con [atributo]|
|----------|
|...|


### 3. Métricas de Reglas
 **Puntaje:** 	 &nbsp;&nbsp;&nbsp;    /1

 Calcule el soporte, cobertura, confianza, e interés de las siguientes reglas:


|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Diabetes = Gestacional → Clase = Retinopatía|||||
|Clase = Retinopatía → Diabetes = Gestacional|||||
|Visión  < 43 and Diabetes = Tipo 1 → Dolor < 5|||||


Presentar los resultados en forma de tabla, e incluir los cálculos realizados en la hoja.

### 4. Agrupamiento de datos - Cálculo de asignaciones
 **Puntaje:** 	 &nbsp;&nbsp;&nbsp;    /1

 Dados los datos de los 3 primeros ejemplos de la tabla, donde se numerizaron las columnas nominales, y dados los centroides **c1** y **c2**, calcule la distancia euclídea de los ejemplos hacia estos centroides, y a cuál de ellos estarían asignados. No utilizar la clase en este ejercicio.


| |Visión |Dolor|Diabetes|
|----------|----------|----------|----------|
|1|44|1|1|
|2|49|6|1|
|3|24|5|3|



|Centroide|Visión |Dolor|Diabetes|
|----------|----------|----------|----------|
|**c1**|35|5|3|
|**c2**|49|9|3|


Nota: Para presentar los resultados, no calcule las raíces cuadradas.En lugar de eso, deje expresada los distancias como $\sqrt{valor}$. Utilice una tabla como la siguiente:


|Ejemplo|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|$\sqrt{valor}$|$\sqrt{valor}$|(c1 o c2)|
|...|...|...|...|


### 5. Agrupamiento de datos - Cálculo de centroides
 **Puntaje:** 	 &nbsp;&nbsp;&nbsp;    /1

 Dados los datos de los 3 primeros ejemplos de la tabla donde se numerizaron las columnas nominales, y la asignación a distintos clusters, calcule los nuevos valores de los centroides. No utilizar la clase en este ejercicio.


| |Visión |Dolor|Diabetes|Cluster Asignado|
|----------|----------|----------|----------|----------|
|1|44|1|1|0|
|2|49|6|1|0|
|3|24|5|3|1|


### 6. Matriz de Correlación
 **Puntaje:** 	 &nbsp;&nbsp;&nbsp;    /1

 Dada la siguiente matriz de correlación, indique la verdad (V) o falsedad (F) de las afirmaciones. Justificar en cada caso.


| |#Cigarrillo/día|Capacidad pulmonar|Riesgo cardiovascular|Cancer|
|----------|----------|----------|----------|----------|
|#Cigarrillo/día|1|-0.6|0.7|0.8|
|Capacidad pulmonar|-0.6|1|-0.4|-0.1|
|Riesgo cardiovascular|0.7|-0.4|1|0.14|
|Cancer|0.8|-0.1|0.14|1|


a) Los atributos Capacidad pulmonar y Cancer son aproximadamente independientes.
b) Es probable que si sube #Cigarrillo/día, también suba Cancer.
c) Los atributos #Cigarrillo/día y Riesgo cardiovascular están correlacionados linealmente, y la correlación es **Fuerte**.
d) Los atributos #Cigarrillo/día y Capacidad pulmonar están correlacionados linealmente, y la correlación es **Débil**.
e) Si dos atributos A y B están fuertemente correlacionados, y los atributos B y C también lo estánm eso implica que A y C también lo deben estar. Justificar en el contexto de los atributos presentados.

### 7. Conceptos de Minería de Datos
 **Puntaje:** 	 &nbsp;&nbsp;&nbsp;    /2

 Responda las preguntas o indique el valor de verdad de a las siguientes afirmaciones. Justifique sus respuestas.

a) Es posible calcular la mediana de un atributo ordinal

b) Dados los items A y B, si A->B tiene soporte 0.7 ¿cuál será el soporte de B->A?

c) Es posible calcular la tasa de acierto (accuracy) de un conjunto de reglas de asociación utilizando una matriz de confusión.

d) Si se busca construir un árbol de clasificación, el atributo de clase (marcado como label) debe ser de tipo ordinal.

e) El índice Davies Bouldin se calcula en base a la dispersión de los ejemplos de cada grupo (cluster) y la distancia entre los centros.

f) En el índice Silhouette, el clustering es perfecto cuando vale 0, y los valores extremos -1 y 1 indican desviaciones negativas y positivas del óptimo.

g) Dado un itemset con 3 items A,B,C, ¿cuántas reglas de asociación pueden generarse en base al itemset?

h) Es posible que al representar el diagrama de barras de un atributo discretizado por frecuencia se observen barras con alturas diferentes.

### 8. Ganancia de Información
 **Puntaje:** 	 &nbsp;&nbsp;&nbsp;    /2

 Utilizando los datos originales, calcule la entropía general del conjunto de datos en base al atributo de clase. Luego, calcule la entropía y ganancia de información para los atributos Diabetes y Dolor. Utilice la siguiente tabla para presentar los resultados:


|Atributo|Diabetes|Dolor|
|----------|----------|----------|
|Entropía| | |
|Ganancia de Información| | |


En base a estos valores, indique cuál de los 2 atributos se elegiría para generar la raíz de un árbol de decisión.
Utilice dos decimales para los cálculos. 
Recuerde que para los atributos numéricos debe calcular la ganancia de información de todos los puntos de corte.
Utilice logaritmo con base 2 para todos los cálculos (obligatorio).

Algunos de logaritmos base 2 (use su calculadora para otros):


|log(0/8)|log(1/8)|log(2/8)|log(3/8)|log(4/8)|log(5/8)|log(6/8)|log(7/8)|log(8/8)|
|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|$-\infty$|-0.90|-0.60|-0.43|-0.30|-0.20|-0.12|-0.06|0.00|

