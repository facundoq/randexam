---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|182|Media|Si|
|2|15|137|Media|Si|
|3|17|147|Media|Si|
|4|15|171|Baja|No|
|5|15|155|Alta|Si|
|6|16|200|Baja|Si|
|7|15|144|Alta|Si|
|8|17|175|Media|Si|


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
|Edad < 16 and Habilidad = Baja → Altura < 164|||||


### 5. Numerización de datos
 Numerizar el atributo Habilidad del conjunto de datos, con la estrategia de generar un valor entero por cada valor numérico. Comenzar con el valor 1, y respetar el orden natural de dicho atributo. Mostrar los valores resultantes.

### 6. Agrupamiento de datos
 a) Utilizando la numerización de datos generada anteriormente, y dados los centroides **c1** y **c2**, calcule la distancia euclídea de los {n_samples} primeros ejemplos hacia estos centroides, y a cuál de ellos estarían asignados. No utilizar la clase en este ejercicio.


|Centroide|Edad|Altura|Habilidad|
|----------|----------|----------|----------|
|**c1**|15|155|1|
|**c2**|16|182|2|


b) ¿Es preciso conocer la posición de los centros para calcular el índice Silhouette del agrupamiento? Explique.

Nota: Para presentar los resultados, no calcule las raíces cuadradas. En lugar de eso, deje expresada los distancias como $\sqrt{valor}$. Utilice una tabla como la siguiente:


|Ejemplo|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|$\sqrt{valor}$|$\sqrt{valor}$|(c1 o c2)|
|...|...|...|...|


### 7. Perceptrón
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[6, 1, 50]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=357*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.

Para presentar los resultados, utilice una tabla como la siguiente:


||Ejemplo 1|Ejemplo 2|...|
|----------|----------|----------|----------|
|Neta|||...|
|Salida|||...|


### 8. Matriz de Correlación
 Dada la siguiente matriz de correlación, indique la verdad (V) o falsedad (F) de las afirmaciones:


| |Ambiente|Temperatura|Humedad|Viento|Juega|
|----------|----------|----------|----------|----------|----------|
|Ambiente|1|0.28|0.11|0|-0.18|
|Temperatura|0.28|1|0.75|-0.21|-0.11|
|Humedad|0.11|0.75|1|-0.12|-0.52|
|Viento|0|-0.21|-0.12|1|-0.26|
|Juega|-0.18|-0.11|-0.52|-0.26|1|


a) Los atributos Ambiente y Viento son independientes.
b) Es posible que si sube la Humedad, también suba el valor del atributo Juega.
c) Los atributos Humedad y Temperatura están correlacionados linealmente, y la correlación es **fuerte**.
d) La mayoría de los pares de atributos no están correlacionados linealmente.
