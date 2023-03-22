---
title: Minería de Datos usando Sistemas Inteligentes
author:  Practica 3 - 2023

date: 
geometry: margin=1.8cm
---



### 1. Clasificador Bayesiano
 Dado el modelo de Naive Bayes siguiente, indicar la clase de los ejemplos de la tabla. Incluir todos los cálculos intermedios 


| | |
|----------|----------|
|Clase F|P(c=F) = 0.4|
|Temperatura|N~(5100.0,2409.7026095903757)|
|Habitable|C~({'No': 0.75, 'Si': 0.25})|
|Luminosidad|N~(11.75,8.80814017448254)|
|Clase K|P(c=K) = 0.6|
|Temperatura|N~(2866.6666666666665,1348.5794995722968)|
|Habitable|C~({'No': 0.5, 'Si': 0.5})|
|Luminosidad|N~(3.3333333333333335,1.632993161855452)|


**Datos**


|Temperatura|Habitable|Luminosidad|
|----------|----------|----------|
|1900|No|1|
|2300|No|2|
|5500|No|5|
|6200|No|22|
|1500|No|6|
|3000|Si|4|
|6600|Si|3|
|6100|No|16|
|2500|Si|3|
|2000|Si|5|


### 2. Entrenar Clasificador Bayesiano
 Dado el conjunto de datos, generar un modelo de Naive Bayes sin corrección de Laplace.

**Datos**


|Temperatura|Habitable|Luminosidad|Clase|
|----------|----------|----------|----------|
|1900|No|1|K|
|2300|No|2|K|
|5500|No|5|K|
|6200|No|22|F|
|1500|No|6|F|
|3000|Si|4|K|
|6600|Si|3|F|
|6100|No|16|F|
|2500|Si|3|K|
|2000|Si|5|K|


### 3. Clasificador Bayesiano
 Dado el modelo de Naive Bayes siguiente, indicar la clase de los ejemplos de la tabla. Incluir todos los cálculos intermedios 


| | |
|----------|----------|
|Clase F|P(c=F) = 0.4|
|Temperatura|N~(5100.0,2409.7026095903757)|
|Habitable|C~({'No': 0.75, 'Si': 0.25})|
|Luminosidad|N~(11.75,8.80814017448254)|
|Clase K|P(c=K) = 0.6|
|Temperatura|N~(2866.6666666666665,1348.5794995722968)|
|Habitable|C~({'No': 0.5, 'Si': 0.5})|
|Luminosidad|N~(3.3333333333333335,1.632993161855452)|


**Datos**


|Temperatura|Habitable|Luminosidad|
|----------|----------|----------|
|1900|No|1|
|2300|No|2|
|5500|No|5|
|6200|No|22|
|1500|No|6|
|3000|Si|4|
|6600|Si|3|
|6100|No|16|
|2500|Si|3|
|2000|Si|5|


### 4. Entrenar Clasificador Bayesiano
 Dado el conjunto de datos, generar un modelo de Naive Bayes sin corrección de Laplace.

**Datos**


|Temperatura|Habitable|Luminosidad|Clase|
|----------|----------|----------|----------|
|1900|No|1|K|
|2300|No|2|K|
|5500|No|5|K|
|6200|No|22|F|
|1500|No|6|F|
|3000|Si|4|K|
|6600|Si|3|F|
|6100|No|16|F|
|2500|Si|3|K|
|2000|Si|5|K|
|20000|No|35|K|


### 5. Clasificador Bayesiano
 Dado el modelo de Naive Bayes siguiente, indicar la clase de los ejemplos de la tabla. Incluir todos los cálculos intermedios 


| | |
|----------|----------|
|Clase Ma|P(c=Ma) = 0.5|
|Color|C~({'Amarillo': 0.8, 'Mezcla': 0.0, 'Rojo': 0.2})|
|Esfericidad|N~(0.5,0.3)|
|Clase Pe|P(c=Pe) = 0.5|
|Color|C~({'Amarillo': 0.1, 'Mezcla': 0.5, 'Rojo': 0.4})|
|Esfericidad|N~(0.3,0.8)|


**Datos**


|Color|Esfericidad|
|----------|----------|
|Amarillo|0.6|
|Mezcla|0.8|


### 6. Clasificador Bayesiano
 Dado el modelo de Naive Bayes siguiente, indicar la clase de los ejemplos de la tabla. Incluir todos los cálculos intermedios 


| | |
|----------|----------|
|Clase Ma|P(c=Ma) = 0.01|
|Color|C~({'Amarillo': 0.8, 'Mezcla': 0.0, 'Rojo': 0.2})|
|Esfericidad|N~(0.5,0.3)|
|Clase Pe|P(c=Pe) = 0.99|
|Color|C~({'Amarillo': 0.1, 'Mezcla': 0.5, 'Rojo': 0.4})|
|Esfericidad|N~(0.3,0.8)|


**Datos**


|Color|Esfericidad|
|----------|----------|
|Amarillo|0.6|
|Mezcla|0.8|

