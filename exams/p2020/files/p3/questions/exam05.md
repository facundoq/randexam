---
title: Minería de Datos usando Sistemas Inteligentes
author: Tercera Fecha - 15 de Julio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|121|Media|No|
|2|19|172|Alta|Si|
|3|17|177|Media|Si|
|4|18|197|Baja|Si|
|5|17|180|Baja|Si|
|6|18|153|Baja|No|
|7|18|170|Alta|No|
|8|16|180|Media|No|


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
|Edad < 17 and Habilidad = Baja → Altura < 169|||||


### 5. Modelo OneR
 Dado la siguiente discretización del conjunto de datos original, aplique el algoritmo OneR para encontrar el mejor atributo y las reglas asociadas para clasificar los ejemplos según el atributo Clase. 


|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|
|Baja|Baja|Media|No|
|Alta|Baja|Alta|Si|
|Media|Alta|Media|Si|
|Alta|Alta|Baja|Si|
|Media|Alta|Baja|Si|
|Alta|Baja|Baja|No|
|Alta|Baja|Alta|No|
|Baja|Alta|Media|No|


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
|**c1**|17|172|1|
|**c2**|18|180|2|


b) En el índice Sillhouette, tanto -1 como 1 son buenos valores, donde -1 indica correlación negativa y 1 positiva, y 0 indica que el clustering no es bueno.

Nota: Para presentar los resultados, no calcule las raíces cuadradas. En lugar de eso, deje expresada los distancias como $\sqrt{valor}$. Utilice una tabla como la siguiente:


|Ejemplo|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|$\sqrt{valor}$|$\sqrt{valor}$|(c1 o c2)|
|...|...|...|...|


### 8. Perceptrón
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[12, 2, 106]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=743*:

a) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cuál es el valor máximo del atributo Edad  para que un ejemplo con Altura=121 y Habilidad=2 pertenezca a la Clase=No?

b) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Edad vale 17, Altura vale 121 y Habilidad vale 2?

### 9. Preguntas conceptuales
 Indique la respuesta a las siguientes preguntas. Justifique su respuesta.

1) La normalización lineal uniforme ¿es sensible a valores anómalos? ¿y la normalización por media/varianza?

2) En un árbol de clasificación ¿a qué corresponden los nodos intermedios, los nodos hoja y las aristas?Dado un itemset con 3 items A,B,C, ¿cuántas reglas pueden generarse en base al itemset?

3) El algoritmo Apriori ¿genera reglas de Asociación?

4) El algoritmo FPGrowth ¿genera reglas de Asociación?

5) Al generar reglas con APriori o FPGrowth ¿es necesario generar itemsets?

6) Dados los items A y B, si A->B tiene soporte 0.7 ¿cuál será el soporte de B->A?

7) ¿Cuáles son las dos propiedades que deben cumplir los grupos (clusters) para obtener un buen agrupamiento?

8) El peso de una red neuronal correspondiente al atributo A es negativo. Dado un ejemplo, si el valor de A sube, ¿a qué clase se acercará el ejemplo?
