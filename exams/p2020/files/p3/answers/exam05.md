---
title: Minería de Datos usando Sistemas Inteligentes
author: Tercera Fecha - 15 de Julio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|121|Media|No|
|2|19|172|Alta|Si|
|3|17|177|Media|Si|
|4|18|197|Baja|Si|
|5|17|180|Baja|Si|
|6|18|153|Baja|No|
|7|18|170|Alta|No|
|8|16|180|Media|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 2, 2, 2, 2, 1, 1, 2]

Intervalos: [[121.0,146.33), [146.33,171.67), [171.67,197.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 1, 1, 2, 2, 0, 0, 2]

Intervalos: [[121,172), [172,180), [180,197]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.00, 1.00, 0.50, 0.75, 0.50, 0.75, 0.75, 0.25

Normalización mu/std con transformación (x-17.25)/1.20

Valores normalizados: -1.88, 1.46, -0.21, 0.63, -0.21, 0.63, 0.63, -1.04

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 1.0


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.69|0.94|
|Ganancia|0.31|0.06|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.86|0.14|
|16.5|0.69|0.31|
|17.5|1.0|0.0|
|18.5|0.86|0.14|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.12|0.25|0.50|1.00|
|Edad < 17 and Habilidad = Baja → Altura < 169|0.00|0.00|1.00|inf|


### 5. Modelo OneR (puntos: 1)
 
|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|
|Baja|Baja|Media|No|
|Alta|Baja|Alta|Si|
|Media|Alta|Media|Si|
|Alta|Alta|Baja|Si|
|Media|Alta|Baja|Si|
|Alta|Baja|Baja|No|
|Alta|Baja|Alta|No|
|Baja|Alta|Media|No|


Mejor atributo: Edad


|Reglas con Edad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Edad = Alta → Clase = Si|0.50|4|
|Edad = Media → Clase = Si|1.00|2|
|Edad = Baja → Clase = No|1.00|2|



|Reglas con Altura (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Altura = Alta → Clase = Si|0.75|4|
|Altura = Baja → Clase = No|0.75|4|



|Reglas con Habilidad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.50|2|
|Habilidad = Media → Clase = No|0.67|3|
|Habilidad = Baja → Clase = Si|0.67|3|


### 6. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Alta', 'Media', 'Baja', 'Baja', 'Baja', 'Alta', 'Media']


Valores nuevos: [2, 3, 2, 1, 1, 1, 3, 2]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|121|2|No|
|2|19|172|3|Si|
|3|17|177|2|Si|
|4|18|197|1|Si|
|5|17|180|1|Si|
|6|18|153|1|No|
|7|18|170|3|No|
|8|16|180|2|No|


### 7. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|2606|3490|1|
|2|8|66|1|
|3|26|10|2|


b) Falso, 1 indica que el clustering es bueno (máxima cohesión y separación), y -1 que es malo (mínima cohesión y separación). 

### 8. Perceptrón (puntos: 1)
 a) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cuál es el valor máximo del atributo Edad  para que un ejemplo con Altura=121 y Habilidad=2 pertenezca a la Clase=No?

Recordamos que w=12, 2, 106 y b=743

Dados esos valores, y asumiendo que $a_0$, $a_1$ y $a_2$ son los valores para los atributos Edad, Altura, Habilidad, para que el modelo esté entre generar 0 o 1 debe cumplirse:

$a_0 . w0 + a_1 . w_1 + a_2 . w_2 = b$

$a_0 . w0 = b - a_1 . w_1 - a_2 . w_2$

$a_0  = (b - a_1 . w_1 - a_2 . w_2)/w_0$

$a_0  = (743 - 121 . 2 - 2 106)/12$

$a_0 = 24.083333333333332$

Como buscamos que esté en clase No, y el signo de $w_0$ es positivo, necesitamos que $a_0$ tenga como valor máximo 24.083333333333332.

b) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Edad vale 17, Altura vale 121 y Habilidad vale 2?

La salida neta es 12×17+2×121+106×2 =658, y por ende la salida es 0 (658<743), con clase No

### 9. Preguntas conceptuales (puntos: 1)
 1) Lineal si, media/varianza también pero menos

2) Los nodos intermedios corresponden a atributos, las aristas a valores de esos atributos, y los nodos hoja a decisiones o predicciones de la clase

3) 6, A->(B,C) B->(A,C) C->(A,B), idem con 2 items en el antecedente

4) No, genera itemsets

5) No, genera itemsets

6) Si, justamente generan itemsets

7) El mismo

8) Alta cohesión intra cluster y alta separación intercluster.

9)  A la clase 0, ya que a mayor valor de A, menor valor de la entrada neta.
