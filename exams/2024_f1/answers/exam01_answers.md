---
title: Minería de Datos usando Sistemas Inteligentes - Tema 2 (Respuestas)
author:  Fecha 1 - 7 de Junio de 2024 

date: 
geometry: margin=1.6cm
---



### 1. Normalización de atributos (Puntos: 1)
 Normalización rango con transformación (x-8.00)/45.00

Valores normalizados: 0.73, 0.91, 0.27, 1.00, 0.51, 0.00, 0.42, 0.96

Normalización mu/std con transformación (x-35.00)/15.19

Valores normalizados: 0.39, 0.92, -0.99, 1.18, -0.26, -1.78, -0.53, 1.05

### 2. Discretización de atributos (Puntos: 1)
 Resultado de la discretización por rango:

Valores: ['Alto', 'Alto', 'Bajo', 'Alto', 'Medio', 'Bajo', 'Medio', 'Alto']

Intervalos: [[8.0,23.0), [23.0,38.0), [38.0,53.0]]

Resultado de la discretización por frecuencia:

Valores: ['Medio', 'Alto', 'Bajo', 'Alto', 'Medio', 'Bajo', 'Bajo', 'Alto']

Intervalos: [[8,31), [31,49), [49,53]]

### 3. Modelo OneR (Puntos: 1)
 
|Peso|Altura|Color|Clase|
|----------|----------|----------|----------|
|Medio|Bajo|Tostado|Común|
|Alto|Alto|Tostado|Raro|
|Bajo|Bajo|Claro|Común|
|Alto|Bajo|Tostado|Raro|
|Medio|Alto|Claro|Común|
|Bajo|Alto|Oscuro|Raro|
|Bajo|Alto|Claro|Común|
|Alto|Bajo|Claro|Común|


Mejor atributo: Color


|Reglas con Peso (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Peso = Bajo → Clase = Común|0.67|3|
|Peso = Medio → Clase = Común|1.00|2|
|Peso = Alto → Clase = Raro|0.67|3|



|Reglas con Altura (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Altura = Alto → Clase = Raro|0.50|4|
|Altura = Bajo → Clase = Común|0.75|4|



|Reglas con Color (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Color = Tostado → Clase = Raro|0.67|3|
|Color = Claro → Clase = Común|1.00|4|
|Color = Oscuro → Clase = Raro|1.00|1|


### 4. Cuartiles (Puntos: 1)
 Valores ordenados de  Peso:

[8.0, 20.0, 27.0, 31.0, 41.0, 49.0, 51.0, 53.0]

Índices de los cuartiles:

2.25, 4.5, 6.75

Cuartiles:

q1=21.75, q2=36.0, q3=50.5

### 5. Métricas de Reglas (Puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Color = Claro → Clase = Común|0.500|0.500|1.000|1.600|
|Clase = Raro → Color = Claro|0.000|0.375|0.000|0.000|
|Peso < 35 and Color = Claro → Altura < 48|0.250|0.375|0.667|1.067|


### 6. Agrupamiento de datos - Cálculo de asignaciones (Puntos: 1.5)
 
| |d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|206|3908|1|
|2|3966|0|2|
|3|245|6171|1|


### 7. Conceptos de Minería de Datos (Puntos: 2)
 a) FALSO. No debe ser solo ordinal, en realidad debe ser cualitativo, es decir, ordinal o nominal.

b) Falso. Las reglas de asociación son un modelo descriptivo, y no se utiliza la tasa de acierto como métrica.

c) Lineal si, media/varianza también pero menos

d) $3 \times 5=15$, ya que para cada clase (3) debemos almacenar la distribución de probabilidad de los valores (5)

e) Falso, es al revés, ya que todo árbol puede expresarse como un conjunto de reglas pero no viceversa.

f) No, ya que también debería saber cuántos valores hay en cada atributo nominal.

g) Si, justamente generan itemsets

h) A la clase 0, ya que a mayor valor de A, menor valor de la entrada neta.

### 8. Ganancia de Información (Puntos: 2)
 Entropías calculadas con logaritmo con base 2

Entropía general: 0.954434002924965


|Atributo|Altura|Color|
|----------|----------|----------|
|Entropía|0.76|0.34|
|Ganancia|0.20|0.61|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|11.5|0.76|0.2|
|25.5|0.94|0.02|
|32.5|0.95|0.0|
|35.0|0.91|0.05|
|51.5|0.8|0.16|
|80.0|0.94|0.02|
|95.5|0.86|0.09|

