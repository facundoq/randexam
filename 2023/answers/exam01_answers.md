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
|Clase Ma|P(c=Ma) = 0.5|
|Color|C~({'Amarillo': 0.8, 'Mezcla': 0.0, 'Rojo': 0.2})|
|Esfericidad|N~(0.5,0.3)|
|Clase Pe|P(c=Pe) = 0.5|
|Color|C~({'Amarillo': 0.1, 'Mezcla': 0.6, 'Rojo': 0.3})|
|Esfericidad|N~(0.8,0.2)|


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
|0.503177636923991|0.060492681129785834|Ma|
|0.0|0.598413420602149|Pe|



| | | | | |
|----------|----------|----------|----------|----------|
|Clase Ma|||||
|Ejemplo 0|P(c=Ma)=0.50|p(x \| c=Ma)=1.01e+00|p(c=Ma \| x)=5.03e-01|
|Ejemplo 1|P(c=Ma)=0.50|p(x \| c=Ma)=0.00e+00|p(c=Ma \| x)=0.00e+00|
|Clase Pe|||||
|Ejemplo 0|P(c=Pe)=0.50|p(x \| c=Pe)=1.21e-01|p(c=Pe \| x)=6.05e-02|
|Ejemplo 1|P(c=Pe)=0.50|p(x \| c=Pe)=1.20e+00|p(c=Pe \| x)=5.98e-01|


### 2. Clasificador Bayesiano (Puntos: 1)
 **Pregunta**:

Dado el modelo de Naive Bayes siguiente, indicar la clase de los ejemplos de la tabla. Incluir todos los cálculos intermedios 


| | |
|----------|----------|
|Clase Ma|P(c=Ma) = 0.01|
|Color|C~({'Amarillo': 0.8, 'Mezcla': 0.0, 'Rojo': 0.2})|
|Esfericidad|N~(0.5,0.3)|
|Clase Pe|P(c=Pe) = 0.99|
|Color|C~({'Amarillo': 0.1, 'Mezcla': 0.6, 'Rojo': 0.3})|
|Esfericidad|N~(0.8,0.2)|


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
|0.01006355273847982|0.11977550863697595|Pe|
|0.0|1.184858572792255|Pe|



| | | | | |
|----------|----------|----------|----------|----------|
|Clase Ma|||||
|Ejemplo 0|P(c=Ma)=0.01|p(x \| c=Ma)=1.01e+00|p(c=Ma \| x)=1.01e-02|
|Ejemplo 1|P(c=Ma)=0.01|p(x \| c=Ma)=0.00e+00|p(c=Ma \| x)=0.00e+00|
|Clase Pe|||||
|Ejemplo 0|P(c=Pe)=0.99|p(x \| c=Pe)=1.21e-01|p(c=Pe \| x)=1.20e-01|
|Ejemplo 1|P(c=Pe)=0.99|p(x \| c=Pe)=1.20e+00|p(c=Pe \| x)=1.18e+00|

