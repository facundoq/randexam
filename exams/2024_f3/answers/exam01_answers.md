---
title: Minería de Datos usando Sistemas Inteligentes - Tema 2 (Respuestas)
author:  Fecha 3 - 12 de Julio de 2024 

date: 
geometry: margin=1.6cm
---



### 1. Normalización de atributos (Puntos: 1)
 Normalización rango con transformación (x-41.00)/50.00

Valores normalizados: 0.28, 0.90, 0.16, 0.00, 1.00, 0.64, 0.32, 0.30

Normalización mu/std con transformación (x-63.50)/17.89

Valores normalizados: -0.48, 1.26, -0.81, -1.26, 1.54, 0.53, -0.36, -0.42

### 2. Discretización de atributos (Puntos: 1)
 Resultado de la discretización por rango:

Valores: ['Poco', 'Alto', 'Poco', 'Poco', 'Alto', 'Medio', 'Poco', 'Poco']

Intervalos: [[41.0,57.67), [57.67,74.33), [74.33,91.0]]

Resultado de la discretización por frecuencia:

Valores: ['Poco', 'Alto', 'Poco', 'Poco', 'Alto', 'Alto', 'Medio', 'Medio']

Intervalos: [[41,56), [56,73), [73,91]]

### 3. Modelo OneR (Puntos: 1)
 
|Goles|Pases|Tipo|Clase|
|----------|----------|----------|----------|
|Pocos|Poco|Normal|Clasifica|
|Muchos|Alto|Normal|No Clasifica|
|Pocos|Poco|Novato|Clasifica|
|Muchos|Poco|Normal|No Clasifica|
|Muchos|Alto|Novato|Clasifica|
|Muchos|Alto|Preferido|No Clasifica|
|Muchos|Medio|Novato|Clasifica|
|Pocos|Medio|Novato|Clasifica|


Mejor atributo: Tipo


|Reglas con Goles (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Goles = Pocos → Clase = Clasifica|1.00|3|
|Goles = Muchos → Clase = No Clasifica|0.60|5|



|Reglas con Pases (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Pases = Alto → Clase = No Clasifica|0.67|3|
|Pases = Medio → Clase = Clasifica|1.00|2|
|Pases = Poco → Clase = Clasifica|0.67|3|



|Reglas con Tipo (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Tipo = Normal → Clase = No Clasifica|0.67|3|
|Tipo = Novato → Clase = Clasifica|1.00|4|
|Tipo = Preferido → Clase = No Clasifica|1.00|1|


### 4. Métricas de Reglas (Puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Tipo = Normal → Clase = Clasifica|0.125|0.375|0.333|0.533|
|Clase = No Clasifica → Tipo = Novato|0.000|0.375|0.000|0.000|
|Goles < 2 and Tipo = Novato → Pases < 64|0.250|0.250|1.000|1.600|


### 5. Agrupamiento de datos - Cálculo de asignaciones (Puntos: 1.5)
 
| |d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|2|965|1|
|2|905|0|2|
|3|49|1374|1|


### 6. Agrupamiento de datos - Cálculo de centroides (Puntos: 1)
 
| |Goles|Pases|Tipo|Cluster Asignado|
|----------|----------|----------|----------|
|1|2.0|56.5|1.0|
|2|3.5|82.0|2.0|


### 7. Conceptos de Minería de Datos (Puntos: 2)
 a. Es posible calcular la mediana de un atributo ordinal
 RESPUESTA:
VERDADERO. La mediana es el valor de la posición floor(N/2) aunque el atributo sea ordinal.

b. El valor de la Ganancia de Información (Information Gain) de un atributo que toma siempre el mismo valor en todos los ejemplos es cero.
 RESPUESTA:
 Verdadero. Si sólo tiene 1 valor, no separa los ejemplos por lo
que su entropía coincide con la entroía de conjunto original. Luego la
ganancia de información será la resta de 2 valores iguales.

c. No es posible calcular la Tasa de Ganancia (Gain Ratio) de un atributo numérico continuo (con decimales).
 RESPUESTA:
FALSO. La cantidad de valores del atributo será finita por lo que se ordenan los valores distintos (no importa que tenga decimales) y se calcula como vimos en clase.

d. Es posible que al representar el diagrama de barras de un atributo discretizado por frecuencia se observen barras con alturas diferentes.
 RESPUESTA:
Verdadero, las barras de altura diferente en la discretización por frecuencia ocurren cuando hay valores repetidos.

### 8. Ganancia de Información (Puntos: 2)
 Entropías calculadas con logaritmo con base 2

Entropía general: 0.954434002924965


|Atributo|Goles|Tipo|
|----------|----------|----------|
|Entropía|0.49|0.34|
|Ganancia|0.47|0.61|



|Goles: Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|2.0|0.61|0.35|
|3.5|0.49|0.47|

