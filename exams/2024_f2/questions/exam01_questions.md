---
title: Minería de Datos usando Sistemas Inteligentes - Tema 2
author:  Fecha 2 - 28 de Junio de 2024 

date: 
geometry: margin=1.6cm
---


|Nombres&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Apellidos&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|DNI/N° Legajo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|#Hojas&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
|----------|----------|----------|----------|
|||||


**Tabla de datos**


| |Tamaño|Anticuerpos|Síntomas|Clase|
|----------|----------|----------|----------|----------|
|1|1|40|Leves|Benigno|
|2|4|60|Leves|Benigno|
|3|3|21|Ninguno|Benigno|
|4|1|61|Graves|Maligno|
|5|2|17|Ninguno|Maligno|
|6|3|45|Ninguno|Benigno|
|7|2|43|Ninguno|Benigno|
|8|2|92|Leves|Maligno|


### 1. Discretización de atributos
 Discretice el atributo Anticuerpos  por a) frecuencia y b) rango en los valores ['Negativo', 'Leve', 'Alto']. En ambos casos, indique los intervalos resultantes. Realice un gráfico de barras para visualizar la frecuencia de los valores resultantes.

 Nota: La discretización es solo para este ejercicio; utilizar los datos originales en el resto de los ejercicios.

### 2. Modelo OneR
 Dada la siguiente discretización del conjunto de datos original, aplique el algoritmo OneR para encontrar el mejor atributo y las reglas asociadas para clasificar los ejemplos según el atributo Clase. 


|Tamaño|Anticuerpos|Síntomas|Clase|
|----------|----------|----------|----------|
|Bajo|Negativo|Leves|Benigno|
|Alto|Alto|Leves|Benigno|
|Alto|Negativo|Ninguno|Benigno|
|Bajo|Alto|Graves|Maligno|
|Alto|Negativo|Ninguno|Maligno|
|Alto|Leve|Ninguno|Benigno|
|Alto|Leve|Ninguno|Benigno|
|Alto|Alto|Leves|Maligno|


Mostrar el accuracy de cada atributo, y las reglas finales del OneR:


||Tamaño|Anticuerpos|Síntomas|
|----------|----------|----------|----------|
|Accuracy||||



|Reglas con [atributo]|
|----------|
|...|


### 3. Métricas de Reglas
 Calcule el soporte, cobertura, confianza, e interés de las siguientes reglas:


|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Síntomas = Graves → Clase = Maligno|||||
|Clase = Benigno → Síntomas = Ninguno|||||
|Tamaño < 2 and Síntomas = Leves → Anticuerpos < 47|||||


Presentar los resultados en forma de tabla, e incluir los cálculos realizados en la hoja.

### 4. Agrupamiento de datos - Cálculo de centroides
 Dado el siguiente conjunto de ejemplos numerizado, calcule los valores de los 2 centroides numerados desde 0 hasta 1 usando la asignación provista. No utilizar la clase en este ejercicio. Este ejercicio es independiente del resto del examen. Utilice una tabla con 2 filas y tantas columnas como atributos haya para presentar los centroides resultantes.


| |Tamaño|Anticuerpos|Síntomas|Cluster Asignado|
|----------|----------|----------|----------|----------|
|1|2|17|1|1|
|2|3|45|1|1|
|3|2|43|1|0|
|4|2|92|2|0|


### 5. Conceptos de Minería de Datos
 Responda las preguntas o indique el valor de verdad de  las siguientes afirmaciones, y justifique sus respuestas. La justificación es necesaria en todos los casos para obtener puntaje.

a. No es posible calcular la Tasa de Ganancia (Gain Ratio) de un atributo numérico continuo (con decimales).

b. Se tiene un problema de clasificación de 100 ejemplos con 3 columnas, una es la de la clase con 4 valores distintos, otra es nominal con 5 valores,
               y la otra es de un atributo numérico con 10 valores distintos. 
               Si se entrena un modelo de Naive Bayes ¿cuántas distribuciones gaussianas se deberán estimar?

c. ¿Cuál de las normalizaciones vistas es más sensible a los valores anómalos/extremos?

d. Dada una regla, (A=Si,B=No) → C=Si, con soporte 0.3, ¿Puedo inferir el soporte de la regla (A=Si) → (B=No, C=Si) sin los datos?

### 6. Ganancia de Información
 Utilizando los datos originales, calcule la entropía general del conjunto de datos en base al atributo de clase. Luego, calcule la entropía y ganancia de información para los atributos Tamaño y Síntomas. Tenga en cuenta que para los atributos numéricos deberá utilizar la variante del algoritmo que busca la mejor discretización probando todos los puntos de corte posibles. Utilice la siguiente tabla para presentar los resultados:


|Atributo|Tamaño|Síntomas|
|----------|----------|----------|
|Entropía| | |
|Ganancia de Información| | |


En base a estos valores, indique cuál de los 2 atributos se elegiría para generar la raíz de un árbol de decisión.
Utilice dos decimales para los cálculos. 
Utilice logaritmo con base 2 para todos los cálculos (obligatorio).

Logaritmos de base 2


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


### 7. Perceptrón
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[22, 1, 31]* (para los atributos Tamaño, Anticuerpos, Síntomas, respectivamente) y *sesgo=147*:

b) Asumiendo que Clase=Benigno está codificado con un 0, y Clase=Maligno con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Tamaño vale 2, Anticuerpos vale 60 y Síntomas vale 1?

a) Asumiendo que Clase=Benigno está codificado con un 0, y Clase=Maligno con un 1, ¿cuál es el valor máximo del atributo Tamaño  para que un ejemplo con Anticuerpos=60 y Síntomas=2 pertenezca a la Clase=Maligno?
