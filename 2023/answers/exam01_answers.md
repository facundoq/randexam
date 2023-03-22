---
title: Minería de Datos usando Sistemas Inteligentes (Respuestas)
author:  Practica 3 - 2023

date: 
geometry: margin=1.8cm
---



### 1. Clasificador Bayesiano (Puntos: 1)
 **Pregunta**:

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


**Respuesta**

Resultado

**Datos**


|p(c=F)|p(c=K)|Predicción|
|----------|----------|----------|
|4.4229284883168014e-07|6.041799620040265e-06|K|
|6.206375359632625e-07|1.4222477260277748e-05|K|
|1.654191897644237e-06|1.9138976182336706e-06|K|
|1.0298783058189661e-06|4.320332519203556e-35|F|
|5.955259875414304e-07|3.419873894484431e-06|K|
|3.4829472311365333e-07|1.9850278692089363e-05|K|
|3.7717333882714527e-07|4.60123004019154e-07|K|
|1.8371413365215523e-06|1.0539089635472503e-19|F|
|2.557903435846975e-07|2.046350932097581e-05|K|
|2.4438277309606356e-07|1.0476190843733399e-05|K|



| | | | | |
|----------|----------|----------|----------|----------|
|Clase F|||||
|Ejemplo 0|P(c=F)=0.40|p(x \| c=F)=1.11e-06|p(c=F \| x)=4.42e-07|
|Ejemplo 1|P(c=F)=0.40|p(x \| c=F)=1.55e-06|p(c=F \| x)=6.21e-07|
|Ejemplo 2|P(c=F)=0.40|p(x \| c=F)=4.14e-06|p(c=F \| x)=1.65e-06|
|Ejemplo 3|P(c=F)=0.40|p(x \| c=F)=2.57e-06|p(c=F \| x)=1.03e-06|
|Ejemplo 4|P(c=F)=0.40|p(x \| c=F)=1.49e-06|p(c=F \| x)=5.96e-07|
|Ejemplo 5|P(c=F)=0.40|p(x \| c=F)=8.71e-07|p(c=F \| x)=3.48e-07|
|Ejemplo 6|P(c=F)=0.40|p(x \| c=F)=9.43e-07|p(c=F \| x)=3.77e-07|
|Ejemplo 7|P(c=F)=0.40|p(x \| c=F)=4.59e-06|p(c=F \| x)=1.84e-06|
|Ejemplo 8|P(c=F)=0.40|p(x \| c=F)=6.39e-07|p(c=F \| x)=2.56e-07|
|Ejemplo 9|P(c=F)=0.40|p(x \| c=F)=6.11e-07|p(c=F \| x)=2.44e-07|
|Clase K|||||
|Ejemplo 0|P(c=K)=0.60|p(x \| c=K)=1.01e-05|p(c=K \| x)=6.04e-06|
|Ejemplo 1|P(c=K)=0.60|p(x \| c=K)=2.37e-05|p(c=K \| x)=1.42e-05|
|Ejemplo 2|P(c=K)=0.60|p(x \| c=K)=3.19e-06|p(c=K \| x)=1.91e-06|
|Ejemplo 3|P(c=K)=0.60|p(x \| c=K)=7.20e-35|p(c=K \| x)=4.32e-35|
|Ejemplo 4|P(c=K)=0.60|p(x \| c=K)=5.70e-06|p(c=K \| x)=3.42e-06|
|Ejemplo 5|P(c=K)=0.60|p(x \| c=K)=3.31e-05|p(c=K \| x)=1.99e-05|
|Ejemplo 6|P(c=K)=0.60|p(x \| c=K)=7.67e-07|p(c=K \| x)=4.60e-07|
|Ejemplo 7|P(c=K)=0.60|p(x \| c=K)=1.76e-19|p(c=K \| x)=1.05e-19|
|Ejemplo 8|P(c=K)=0.60|p(x \| c=K)=3.41e-05|p(c=K \| x)=2.05e-05|
|Ejemplo 9|P(c=K)=0.60|p(x \| c=K)=1.75e-05|p(c=K \| x)=1.05e-05|


### 2. Entrenar Clasificador Bayesiano (Puntos: 1)
 **Pregunta**:

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


**Respuesta**


|NB estrellas|Accuracy 0.80|
|----------|----------|
|Clase F|P(c=F) = 0.4|
|Temperatura|N~(5100.0,2409.7026095903757)|
|Habitable|C~({'No': 0.75, 'Si': 0.25})|
|Luminosidad|N~(11.75,8.80814017448254)|
|Clase K|P(c=K) = 0.6|
|Temperatura|N~(2866.6666666666665,1348.5794995722968)|
|Habitable|C~({'No': 0.5, 'Si': 0.5})|
|Luminosidad|N~(3.3333333333333335,1.632993161855452)|


### 3. Clasificador Bayesiano (Puntos: 1)
 **Pregunta**:

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


**Respuesta**

Resultado

**Datos**


|p(c=F)|p(c=K)|Predicción|
|----------|----------|----------|
|4.4229284883168014e-07|6.041799620040265e-06|K|
|6.206375359632625e-07|1.4222477260277748e-05|K|
|1.654191897644237e-06|1.9138976182336706e-06|K|
|1.0298783058189661e-06|4.320332519203556e-35|F|
|5.955259875414304e-07|3.419873894484431e-06|K|
|3.4829472311365333e-07|1.9850278692089363e-05|K|
|3.7717333882714527e-07|4.60123004019154e-07|K|
|1.8371413365215523e-06|1.0539089635472503e-19|F|
|2.557903435846975e-07|2.046350932097581e-05|K|
|2.4438277309606356e-07|1.0476190843733399e-05|K|



| | | | | |
|----------|----------|----------|----------|----------|
|Clase F|||||
|Ejemplo 0|P(c=F)=0.40|p(x \| c=F)=1.11e-06|p(c=F \| x)=4.42e-07|
|Ejemplo 1|P(c=F)=0.40|p(x \| c=F)=1.55e-06|p(c=F \| x)=6.21e-07|
|Ejemplo 2|P(c=F)=0.40|p(x \| c=F)=4.14e-06|p(c=F \| x)=1.65e-06|
|Ejemplo 3|P(c=F)=0.40|p(x \| c=F)=2.57e-06|p(c=F \| x)=1.03e-06|
|Ejemplo 4|P(c=F)=0.40|p(x \| c=F)=1.49e-06|p(c=F \| x)=5.96e-07|
|Ejemplo 5|P(c=F)=0.40|p(x \| c=F)=8.71e-07|p(c=F \| x)=3.48e-07|
|Ejemplo 6|P(c=F)=0.40|p(x \| c=F)=9.43e-07|p(c=F \| x)=3.77e-07|
|Ejemplo 7|P(c=F)=0.40|p(x \| c=F)=4.59e-06|p(c=F \| x)=1.84e-06|
|Ejemplo 8|P(c=F)=0.40|p(x \| c=F)=6.39e-07|p(c=F \| x)=2.56e-07|
|Ejemplo 9|P(c=F)=0.40|p(x \| c=F)=6.11e-07|p(c=F \| x)=2.44e-07|
|Clase K|||||
|Ejemplo 0|P(c=K)=0.60|p(x \| c=K)=1.01e-05|p(c=K \| x)=6.04e-06|
|Ejemplo 1|P(c=K)=0.60|p(x \| c=K)=2.37e-05|p(c=K \| x)=1.42e-05|
|Ejemplo 2|P(c=K)=0.60|p(x \| c=K)=3.19e-06|p(c=K \| x)=1.91e-06|
|Ejemplo 3|P(c=K)=0.60|p(x \| c=K)=7.20e-35|p(c=K \| x)=4.32e-35|
|Ejemplo 4|P(c=K)=0.60|p(x \| c=K)=5.70e-06|p(c=K \| x)=3.42e-06|
|Ejemplo 5|P(c=K)=0.60|p(x \| c=K)=3.31e-05|p(c=K \| x)=1.99e-05|
|Ejemplo 6|P(c=K)=0.60|p(x \| c=K)=7.67e-07|p(c=K \| x)=4.60e-07|
|Ejemplo 7|P(c=K)=0.60|p(x \| c=K)=1.76e-19|p(c=K \| x)=1.05e-19|
|Ejemplo 8|P(c=K)=0.60|p(x \| c=K)=3.41e-05|p(c=K \| x)=2.05e-05|
|Ejemplo 9|P(c=K)=0.60|p(x \| c=K)=1.75e-05|p(c=K \| x)=1.05e-05|


### 4. Entrenar Clasificador Bayesiano (Puntos: 1)
 **Pregunta**:

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


**Respuesta**


|NB estrellas|Accuracy 0.73|
|----------|----------|
|Clase F|P(c=F) = 0.36363636363636365|
|Temperatura|N~(5100.0,2409.7026095903757)|
|Habitable|C~({'No': 0.75, 'Si': 0.25})|
|Luminosidad|N~(11.75,8.80814017448254)|
|Clase K|P(c=K) = 0.6363636363636364|
|Temperatura|N~(5314.285714285715,6591.769760195556)|
|Habitable|C~({'No': 0.5714285714285714, 'Si': 0.42857142857142855})|
|Luminosidad|N~(7.857142857142857,12.061351104921474)|


### 5. Clasificador Bayesiano (Puntos: 1)
 **Pregunta**:

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


**Respuesta**

Resultado

**Datos**


|p(c=Ma)|p(c=Pe)|Predicción|
|----------|----------|----------|
|0.503177636923991|0.02324094336686056|Ma|
|0.0|0.10255030267199221|Pe|



| | | | | |
|----------|----------|----------|----------|----------|
|Clase Ma|||||
|Ejemplo 0|P(c=Ma)=0.50|p(x \| c=Ma)=1.01e+00|p(c=Ma \| x)=5.03e-01|
|Ejemplo 1|P(c=Ma)=0.50|p(x \| c=Ma)=0.00e+00|p(c=Ma \| x)=0.00e+00|
|Clase Pe|||||
|Ejemplo 0|P(c=Pe)=0.50|p(x \| c=Pe)=4.65e-02|p(c=Pe \| x)=2.32e-02|
|Ejemplo 1|P(c=Pe)=0.50|p(x \| c=Pe)=2.05e-01|p(c=Pe \| x)=1.03e-01|


### 6. Clasificador Bayesiano (Puntos: 1)
 **Pregunta**:

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


**Respuesta**

Resultado

**Datos**


|p(c=Ma)|p(c=Pe)|Predicción|
|----------|----------|----------|
|0.01006355273847982|0.046017067866383904|Pe|
|0.0|0.20304959929054456|Pe|



| | | | | |
|----------|----------|----------|----------|----------|
|Clase Ma|||||
|Ejemplo 0|P(c=Ma)=0.01|p(x \| c=Ma)=1.01e+00|p(c=Ma \| x)=1.01e-02|
|Ejemplo 1|P(c=Ma)=0.01|p(x \| c=Ma)=0.00e+00|p(c=Ma \| x)=0.00e+00|
|Clase Pe|||||
|Ejemplo 0|P(c=Pe)=0.99|p(x \| c=Pe)=4.65e-02|p(c=Pe \| x)=4.60e-02|
|Ejemplo 1|P(c=Pe)=0.99|p(x \| c=Pe)=2.05e-01|p(c=Pe \| x)=2.03e-01|

