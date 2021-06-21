---
title: Minería de Datos usando Sistemas Inteligentes
author: Tercera Fecha - 15 de Julio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|157|Baja|No|
|2|16|180|Alta|Si|
|3|18|174|Baja|No|
|4|18|132|Media|Si|
|5|19|161|Alta|Si|
|6|15|167|Media|Si|
|7|17|169|Media|Si|
|8|16|176|Media|Si|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 2, 2, 0, 1, 2, 2, 2]

Intervalos: [[132.0,148.0), [148.0,164.0), [164.0,180.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 2, 2, 0, 0, 1, 1, 2]

Intervalos: [[132,167), [167,174), [174,180]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.00, 0.25, 0.75, 0.75, 1.00, 0.00, 0.50, 0.25

Normalización mu/std con transformación (x-16.75)/1.39

Valores normalizados: -1.26, -0.54, 0.90, 0.90, 1.62, -1.26, 0.18, -0.54

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.8112781244591328


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.74|0.00|
|Ganancia|0.07|0.81|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.74|0.07|
|16.5|0.81|0.0|
|17.5|0.8|0.02|
|18.5|0.76|0.06|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.25|0.25|1.00|1.33|
|Edad < 17 and Habilidad = Baja → Altura < 164|0.12|0.12|1.00|2.67|


### 5. Modelo OneR (puntos: 1)
 
|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|
|Baja|Baja|Baja|No|
|Media|Alta|Alta|Si|
|Alta|Alta|Baja|No|
|Alta|Baja|Media|Si|
|Alta|Baja|Alta|Si|
|Baja|Baja|Media|Si|
|Media|Alta|Media|Si|
|Media|Alta|Media|Si|


Mejor atributo: Habilidad


|Reglas con Edad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Edad = Alta → Clase = Si|0.67|3|
|Edad = Media → Clase = Si|1.00|3|
|Edad = Baja → Clase = Si|0.50|2|



|Reglas con Altura (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Altura = Alta → Clase = Si|0.75|4|
|Altura = Baja → Clase = Si|0.75|4|



|Reglas con Habilidad (accuracy=1.0)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Habilidad = Alta → Clase = Si|1.00|2|
|Habilidad = Media → Clase = Si|1.00|4|
|Habilidad = Baja → Clase = No|1.00|2|


### 6. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Alta', 'Baja', 'Media', 'Alta', 'Media', 'Media', 'Media']


Valores nuevos: [1, 3, 1, 2, 3, 2, 2, 2]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|157|1|No|
|2|16|180|3|Si|
|3|18|174|1|No|
|4|18|132|2|Si|
|5|19|161|3|Si|
|6|15|167|2|Si|
|7|17|169|2|Si|
|8|16|176|2|Si|


### 7. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|101|371|1|
|2|173|21|2|
|3|53|5|2|


b) Falso, 1 indica que el clustering es bueno (máxima cohesión y separación), y -1 que es malo (mínima cohesión y separación). 

### 8. Perceptrón (puntos: 1)
 a) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cuál es el valor máximo del atributo Edad  para que un ejemplo con Altura=169 y Habilidad=2 pertenezca a la Clase=No?

Recordamos que w=6, 1, 50 y b=365

Dados esos valores, y asumiendo que $a_0$, $a_1$ y $a_2$ son los valores para los atributos Edad, Altura, Habilidad, para que el modelo esté entre generar 0 o 1 debe cumplirse:

$a_0 . w0 + a_1 . w_1 + a_2 . w_2 = b$

$a_0 . w0 = b - a_1 . w_1 - a_2 . w_2$

$a_0  = (b - a_1 . w_1 - a_2 . w_2)/w_0$

$a_0  = (365 - 169 . 1 - 2 50)/6$

$a_0 = 16.0$

Como buscamos que esté en clase No, y el signo de $w_0$ es positivo, necesitamos que $a_0$ tenga como valor máximo 16.0.

b) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Edad vale 15, Altura vale 169 y Habilidad vale 3?

La salida neta es 6×15+1×169+50×3 =409, y por ende la salida es 1 (409>=365), con clase Si

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
