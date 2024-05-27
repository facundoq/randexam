---
title: Minería de Datos usando Sistemas Inteligentes - Tema 2 (Respuestas)
author:  Fecha 1 - 7 de Junio de 2024 

date: 
geometry: margin=1.6cm
---



### 1. Normalización de atributos (Puntos: 1)
 Normalización rango con transformación (x-41.00)/95.00

Valores normalizados: 0.47, 0.00, 0.33, 0.44, 0.40, 0.44, 1.00, 0.40

Normalización mu/std con transformación (x-82.38)/24.32

Valores normalizados: 0.15, -1.70, -0.43, 0.03, -0.14, 0.03, 2.20, -0.14

### 2. Modelo OneR (Puntos: 1)
 
|Peso|Altura|Color|Clase|
|----------|----------|----------|----------|
|Alto|Bajo|Tostado|Común|
|Bajo|Alto|Tostado|Común|
|Bajo|Bajo|Claro|Común|
|Alto|Alto|Oscuro|Raro|
|Medio|Bajo|Claro|Raro|
|Alto|Alto|Claro|Común|
|Alto|Alto|Claro|Común|
|Medio|Alto|Tostado|Común|


Mejor atributo: Color


|Reglas con Peso (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Peso = Medio → Clase = Raro|0.50|2|
|Peso = Alto → Clase = Común|0.75|4|
|Peso = Bajo → Clase = Común|1.00|2|



|Reglas con Altura (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Altura = Alto → Clase = Común|0.80|5|
|Altura = Bajo → Clase = Común|0.67|3|



|Reglas con Color (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Color = Oscuro → Clase = Raro|1.00|1|
|Color = Claro → Clase = Común|0.75|4|
|Color = Tostado → Clase = Común|1.00|3|


### 3. Métricas de Reglas (Puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Color = Oscuro → Clase = Raro|0.125|0.125|1.000|4.000|
|Clase = Común → Color = Claro|0.375|0.750|0.500|1.000|
|Peso < 82 and Color = Tostado → Altura < 61|0.000|0.250|0.000|0.000|


### 4. Agrupamiento de datos - Cálculo de asignaciones (Puntos: 1.5)
 
| |d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|59|410|1|
|2|1734|1765|1|
|3|533|1646|1|


### 5. Conceptos de Minería de Datos (Puntos: 2)
 a) FALSO. No debe ser solo ordinal, en realidad debe ser cualitativo, es decir, ordinal o nominal.

b) Falso. Las reglas de asociación son un modelo descriptivo, y no se utiliza la tasa de acierto como métrica.

c) Lineal si, media/varianza también pero menos

d) $3 \times 5=15$, ya que para cada clase (3) debemos almacenar la distribución de probabilidad de los valores (5)

e) Falso, es al revés, ya que todo árbol puede expresarse como un conjunto de reglas pero no viceversa.

f) No, las reglas se generan luego, los algoritmos generan itemsets frecuentes.

g) A la clase 0, ya que a mayor valor de A, menor valor de la entrada neta.

h) Como se sabe cuantos atributos hay y cuantos valores tiene cada uno, sabemos que en el peor de los casos, el arbol tendrá 6^3 nodos, ya que si el árbol llega al máximo de su complejidad, en cada nivel cada nodo se dividirá en 6 ramas .

### 6. Diagrama de Caja (Puntos: 1)
 Valores ordenados de  Peso:

[41.0, 72.0, 79.0, 79.0, 83.0, 83.0, 86.0, 136.0]

Índices de los cuartiles:

2.25, 4.5, 6.75

Cuartiles:

q1=73.75, q2=81.0, q3=85.25

IQR: 11.5

Atípicos Extremos bajos: (-inf, 39.25), valores: []

Atípicos Leves bajos: (39.25, 56.5), valores: [41.0]

Atípicos Leves altos: (102.5, 119.75), valores: []

Atípicos Extremos altos: (119.75, inf), valores: [136.0]

### 7. Ganancia de Información (Puntos: 2)
 Entropías calculadas con logaritmo con base 2

Entropía general: 0.8112781244591328


|Atributo|Altura|Color|
|----------|----------|----------|
|Entropía|0.52|0.41|
|Ganancia|0.29|0.41|


Entropía de cortes del atributo Altura


|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|39.0|0.52|0.29|
|50.5|0.74|0.07|
|61.5|0.8|0.02|
|64.0|0.8|0.02|
|72.5|0.74|0.07|
|80.5|0.52|0.29|

