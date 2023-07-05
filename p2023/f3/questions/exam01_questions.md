---
title: Minería de Datos usando Sistemas Inteligentes - Tema 2
author:  Fecha 3 - 7 de Julio de 2023 

date: 
geometry: margin=1.6cm
---


|Nombres&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Apellidos&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|DNI/N° Legajo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|#Hojas&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
|----------|----------|----------|----------|
|||||


**Tabla de datos**


| |Vida|Fuerza|Habilidad Especial|Clase|
|----------|----------|----------|----------|----------|
|1|41|4|Rapidez|Mítico|
|2|49|7|Rapidez|Mítico|
|3|20|2|Salto|Mítico|
|4|53|7|Defensa|Normal|
|5|31|1|Salto|Normal|
|6|8|5|Salto|Mítico|
|7|27|5|Salto|Mítico|
|8|51|5|Rapidez|Mítico|


### 1. Normalización de atributos
 Normalice el atributo Vida mediante: 

1. rango lineal uniforme (min/max)

2. media/varianza


Indicar los valores resultantes normalizados. 
 Nota: La normalización es solo para este ejercicio. Utilizar los datos originales en los siguientes.

### 2. Discretización de atributos
 Discretice el atributo Vida  por a) frecuencia y b) rango en los valores ['Débil', 'Normal', 'Robusto']. En ambos casos, indique los intervalos resultantes. Realice un gráfico de barras para visualizar la frecuencia de los valores resultantes.

 Nota: La discretización es solo para este ejercicio; utilizar los datos originales en el resto de los ejercicios.

### 3. Modelo OneR
 Dada la siguiente discretización del conjunto de datos original, aplique el algoritmo OneR para encontrar el mejor atributo y las reglas asociadas para clasificar los ejemplos según el atributo Clase. 


|Vida|Fuerza|Habilidad Especial|Clase|
|----------|----------|----------|----------|
|Media|Leve|Rapidez|Mítico|
|Alta|Grave|Rapidez|Mítico|
|Baja|Leve|Salto|Mítico|
|Alta|Grave|Defensa|Normal|
|Media|Leve|Salto|Normal|
|Baja|Grave|Salto|Mítico|
|Baja|Grave|Salto|Mítico|
|Alta|Grave|Rapidez|Mítico|


Mostrar el accuracy de cada atributo, y las reglas finales del OneR:


||Vida|Fuerza|Habilidad Especial|
|----------|----------|----------|----------|
|Accuracy||||



|Reglas con [atributo]|
|----------|
|...|


### 4. Cuartiles
 Calcule la mediana y los dos cuartiles del atributo Vida.

 Nota: Utilice la definición de cuartil vista en la teoría.

### 5. Métricas de Reglas
 Calcule el soporte, cobertura, confianza, e interés de las siguientes reglas:


|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad Especial = Salto → Clase = Normal|||||
|Clase = Normal → Habilidad Especial = Salto|||||
|Vida < 35 and Habilidad Especial = Rapidez → Fuerza < 4|||||


Presentar los resultados en forma de tabla, e incluir los cálculos realizados en la hoja.

### 6. Agrupamiento de datos - Cálculo de asignaciones
 Dado el siguiente conjunto de ejemplos numerizado, y dados los centroides **c1** y **c2**, calcule la distancia euclídea de los ejemplos hacia estos centroides, y a cuál de ellos estarían asignados. No utilizar la clase en este ejercicio.


| |Vida|Fuerza|Habilidad Especial|Clase|
|----------|----------|----------|----------|----------|
|1|41|4|2|Mítico|
|2|49|7|2|Mítico|
|3|20|2|1|Mítico|



|Centroide|Vida|Fuerza|Habilidad Especial|
|----------|----------|----------|----------|
|**c1**|27|5|1|
|**c2**|49|7|3|


Nota: Para presentar los resultados, no calcule las raíces cuadradas.En lugar de eso, deje expresada los distancias como $\sqrt{valor}$. Utilice una tabla como la siguiente:


|Ejemplo|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|$\sqrt{valor}$|$\sqrt{valor}$|(c1 o c2)|
|...|...|...|...|


### 7. Conceptos de Minería de Datos
 Responda las preguntas o indique el valor de verdad de  las siguientes afirmacione, y justifique sus respuestas. La justificación es necesaria en todos los casos para obtener puntaje.

a) El valor de la Ganancia de Información (Information Gain) de un atributo que toma siempre el mismo valor en todos los ejemplos es cero.

b)  Un atributo nominal puede tener 2 modas.

c) En un árbol de clasificación ¿a qué corresponden los nodos intermedios, los nodos hoja y las aristas?

d) Dada una regla, (A=Si,B=No) → C=Si, con soporte 0.3, ¿Puedo inferir el soporte de la regla (A=Si) → (B=No, C=Si) sin los datos?

e) Se tiene un problema de clasificación de 100 ejemplos con 3 atributos/columnas, la primera es la de la clase con 3 valores distintos, la segunda tiene valores nominales con 4 valores distintos y la tercera tiene valores numéricos con 5 valores distintos. 
               Si se entrena un modelo de Naive Bayes ¿cuántas distribuciones gaussianas se deberán estimar?

f) Las reglas de clasificación que se generan con OneR pueden ejecutarse en cualquier orden a diferencia de las generadas con el método PART.

g) Liste las etapas de un proceso de minería de datos según KDD. Indique cuál suele ser la etapa más costosa del proceso

h) Indique qué modelos vistos en la materia son interpretables y cuáles no lo son, e indique porqué los considera así

### 8. Perceptrón
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[2, 14, 41]* (para los atributos Vida, Fuerza, Habilidad Especial, respectivamente) y *sesgo=199*:

a) Asumiendo que Clase=Normal está codificado con un 0, y Clase=Mítico con un 1, ¿cuál es el valor máximo del atributo Vida  para que un ejemplo con Fuerza=7 y Habilidad Especial=1 pertenezca a la Clase=Mítico?

b) Asumiendo que Clase=Normal está codificado con un 0, y Clase=Mítico con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Vida vale 51, Fuerza vale 1 y Habilidad Especial vale 2?
