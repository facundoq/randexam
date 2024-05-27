---
title: Minería de Datos usando Sistemas Inteligentes
author: Segunda Fecha - 1 de Julio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|202|Alta|Si|
|2|17|157|Baja|No|
|3|18|159|Media|No|
|4|16|148|Baja|No|
|5|15|187|Media|No|
|6|19|123|Baja|No|
|7|17|204|Alta|Si|
|8|19|154|Baja|No|


### 1. Discretización de atributos
 Discretice el atributo Altura  por a) frecuencia y b) rango en 3 valores. En ambos casos, indique los intervalos resultantes. Realice un gráfico de barras para visualizar la frecuencia de los valores resultantes.

 Nota: La discretización es solo para este ejercicio; utilizar los datos originales en los siguientes.

### 2. Normalización de atributos
 Normalice el atributo Edad mediante a) rango lineal uniforme y b) media/varianza. En ambos casos, indicar los valores resultantes. 
 Nota: La normalización es solo para este ejercicio; utilizar los datos originales en los siguientes.

### 3. Ganancia de Información
 Calcule la entropía general del conjunto de datos en base al atributo de clase. Luego, calcule la entropía y ganancia de información para los atributos Edad y Habilidad. Utilice la siguiente tabla para presentar los resultados:


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía| | |
|Ganancia de Información| | |


En base a estos valores, indique cuál de los 2 atributos se elegiría para generar la raíz de un árbol de decisión.

### 4. Métricas de Reglas
 Calcule el soporte, cobertura, confianza, e interés de las siguientes reglas:


|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|||||
|Edad < 17 and Habilidad = Baja → Altura < 167|||||


### 5. Modelo OneR
 Dado la siguiente discretización del conjunto de datos original, aplique el algoritmo OneR para encontrar el mejor atributo y las reglas asociadas para clasificar los ejemplos según el atributo Clase. 


|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|
|Baja|Alta|Alta|Si|
|Media|Baja|Baja|No|
|Alta|Alta|Media|No|
|Baja|Baja|Baja|No|
|Baja|Alta|Media|No|
|Alta|Baja|Baja|No|
|Media|Alta|Alta|Si|
|Alta|Baja|Baja|No|


Mostrar el accuracy de cada atributo, y las reglas finales del OneR:


||Edad|Altura|Habilidad|
|----------|----------|----------|----------|
|Accuracy||||



|Reglas con [atributo]|
|----------|
|...|


### 6. Numerización de datos
 Numerizar el atributo Habilidad del conjunto de datos, con la estrategia de generar un valor entero por cada valor numérico. Comenzar con el valor 1, y respetar el orden natural de dicho atributo (Baja < Media < Alta). Mostrar los valores resultantes.

### 7. Agrupamiento de datos
 a) Utilizando la numerización de datos generada anteriormente, y dados los centroides **c1** y **c2**, calcule la distancia euclídea de los 3 primeros ejemplos hacia estos centroides, y a cuál de ellos estarían asignados. No utilizar la clase en este ejercicio.


|Centroide|Edad|Altura|Habilidad|
|----------|----------|----------|----------|
|**c1**|16|157|1|
|**c2**|18|202|2|


b) El costo computacional del cálculo del índice Silhouette ¿suele ser mayor que el de Davies-Bouldin?. Justifique su respuesta.

Nota: Para presentar los resultados, no calcule las raíces cuadradas. En lugar de eso, deje expresada los distancias como $\sqrt{valor}$. Utilice una tabla como la siguiente:


|Ejemplo|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|$\sqrt{valor}$|$\sqrt{valor}$|(c1 o c2)|
|...|...|...|...|


### 8. Perceptrón
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[6, 1, 56]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=367*:

a) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cuál es el valor máximo del atributo Edad  para que un ejemplo con Altura=202 y Habilidad=3 pertenezca a la Clase=No?

b) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Edad vale 16, Altura vale 204 y Habilidad vale 3?

### 9. Verdadero o Falso
 Indique el valor de verdad de las siguientes afirmaciones. Justifique su respuesta.

1) Dado un conjunto de atributos, puede afirmarse que los que tengan el mismo valor de entropía también tendrán el mismo valor de Ganancia de Información (Information Gain).

2) El índice Silhouette se calcula en base a la dispersión de los ejemplos de cada grupo (cluster) y la distancia entre los centros.

3) Si se busca construir un árbol de clasificación, el atributo de clase no puede ser numérico.

4) Las reglas de clasificación que se generan con OneR pueden ejecutarse en cualquier orden a diferencia de las generadas con el método PART.

5) Dadas dos reglas con valor de confianza=1 (perfectas) será más interesante la que tenga un menor valor de soporte para el consecuente.

6) Un atributo nominal sólo aparecerá una vez en una misma regla generada con el método PART (recuerde que se generan como una rama de un árbol parcialmente construido con C4.5)

7) Para poder agrupar un conjunto de ejemplos utilizando el método K-Means es obligatorio que los valores de los atributos estén escalados.
