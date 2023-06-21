---
title: Minería de Datos usando Sistemas Inteligentes - Tema 2 (Respuestas)
author:  Fecha 2 - 23 de Junio de 2023 

date: 
geometry: margin=1.6cm
---



### 1. Normalización de atributos (Puntos: 1)
 Normalización rango con transformación (x-27.00)/44.00

Valores normalizados: 1.00, 0.64, 0.55, 0.00, 0.43, 0.41, 0.50, 0.34

Normalización mu/std con transformación (x-48.25)/11.61

Valores normalizados: 1.96, 0.58, 0.24, -1.83, -0.19, -0.28, 0.06, -0.54

### 2. Modelo OneR (Puntos: 1)
 
|Días |Llanto|Leche|Clase|
|----------|----------|----------|----------|
|Alto|Leve|Materna|Cólicos|
|Alto|Grave|Fórmula|Otro|
|Alto|Leve|Fórmula|Cólicos|
|Bajo|Grave|Mixta|Cólicos|
|Medio|Leve|Fórmula|Otro|
|Bajo|Grave|Fórmula|Otro|
|Medio|Grave|Fórmula|Cólicos|
|Bajo|Leve|Fórmula|Cólicos|


Mejor atributo: Días 


|Reglas con Días  (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Días  = Bajo → Clase = Cólicos|0.67|3|
|Días  = Alto → Clase = Cólicos|0.67|3|
|Días  = Medio → Clase = Cólicos|0.50|2|



|Reglas con Llanto (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Llanto = Leve → Clase = Cólicos|0.75|4|
|Llanto = Grave → Clase = Cólicos|0.50|4|



|Reglas con Leche (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Leche = Materna → Clase = Cólicos|1.00|1|
|Leche = Mixta → Clase = Cólicos|1.00|1|
|Leche = Fórmula → Clase = Cólicos|0.50|6|


### 3. Cuartiles (Puntos: 1)
 Valores ordenados de  Días :

[27.0, 42.0, 45.0, 46.0, 49.0, 51.0, 55.0, 71.0]

Índices de los cuartiles:

2.25, 4.5, 6.75

Cuartiles:

q1=42.75, q2=47.5, q3=54.0

### 4. Métricas de Reglas (Puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Leche = Fórmula → Clase = Cólicos|0.375|0.750|0.500|0.800|
|Clase = Otro → Leche = Fórmula|0.375|0.375|1.000|1.333|
|Días  < 48 and Leche = Fórmula → Llanto < 6|0.250|0.375|0.667|1.333|


### 5. Agrupamiento de datos - Cálculo de centroides (Puntos: 1)
 
| |Días |Llanto|Leche|Cluster Asignado|
|----------|----------|----------|----------|
|1|47.5|5.5|3.0|
|2|43.5|6.5|3.0|


### 6. Conceptos de Minería de Datos (Puntos: 2)
 a) Falso, no necesariamente, puede indicar que hay valores anómalos.

b) No, ya que también debería saber cuántos valores hay en cada atributo nominal.

c) Verdadero, ya que la ganancia de información (GI) es GI = Entropía - Entropía(Atributo)

d) No, genera itemsets

e) A la clase 0, ya que a mayor valor de A, menor valor de la entrada neta.

f) Verdadero, ya que calcula distancias entre los centroides y los ejemplos de cada cluster.

g) Lineal si, media/varianza también pero menos

h) Falso, es al revés, ya que todo árbol puede expresarse como un conjunto de reglas pero no viceversa.

### 7. Ganancia de Información (Puntos: 2)
 Entropías calculadas con logaritmo con base 2

Entropía general: 0.954434002924965


|Atributo|Llanto|Leche|
|----------|----------|----------|
|Entropía|0.76|0.75|
|Ganancia|0.20|0.20|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|3.0|0.86|0.09|
|5.0|0.91|0.05|
|6.5|0.95|0.0|
|7.5|0.94|0.02|
|8.5|0.76|0.2|


### 8. Perceptrón (Puntos: 1)
 a) Asumiendo que Clase=Cólicos está codificado con un 0, y Clase=Otro con un 1, ¿cuál es el valor máximo del atributo Días   para que un ejemplo con Llanto=2 y Leche=1 pertenezca a la Clase=Otro?

Recordamos que w=1, 9, 19 y b=147

Dados esos valores, y asumiendo que $a_0$, $a_1$ y $a_2$ son los valores para los atributos Días , Llanto, Leche, para que el modelo esté entre generar 0 o 1 debe cumplirse:

$a_0 . w0 + a_1 . w_1 + a_2 . w_2 = b$

$a_0 . w0 = b - a_1 . w_1 - a_2 . w_2$

$a_0  = (b - a_1 . w_1 - a_2 . w_2)/w_0$

$a_0  = (147 - 2 . 9 - 1 19)/1$

$a_0 = 110.0$

Como buscamos que esté en clase Otro, y el signo de $w_0$ es positivo, necesitamos que $a_0$ tenga como valor máximo 110.0.

b) Asumiendo que Clase=Cólicos está codificado con un 0, y Clase=Otro con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Días  vale 49, Llanto vale 7 y Leche vale 3?

La salida neta es 1×49+9×7+19×3 =169, y por ende la salida es 1 (169>=147), con clase Otro
