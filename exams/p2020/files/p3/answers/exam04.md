---
title: Minería de Datos usando Sistemas Inteligentes
author: Tercera Fecha - 15 de Julio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|17|163|Media|No|
|2|16|165|Alta|Si|
|3|15|157|Baja|Si|
|4|15|146|Baja|Si|
|5|17|141|Media|Si|
|6|16|166|Alta|Si|
|7|19|164|Alta|Si|
|8|18|214|Alta|Si|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 0, 0, 0, 0, 1, 0, 2]

Intervalos: [[141.0,165.33), [165.33,189.67), [189.67,214.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 2, 0, 0, 0, 2, 1, 2]

Intervalos: [[141,163), [163,165), [165,214]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.50, 0.25, 0.00, 0.00, 0.50, 0.25, 1.00, 0.75

Normalización mu/std con transformación (x-16.62)/1.32

Valores normalizados: 0.28, -0.47, -1.23, -1.23, 0.28, -0.47, 1.80, 1.04

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.5435644431995964


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.41|0.25|
|Ganancia|0.14|0.29|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.49|0.06|
|16.5|0.41|0.14|
|17.5|0.49|0.06|
|18.5|0.52|0.03|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.50|0.50|1.00|1.14|
|Edad < 17 and Habilidad = Baja → Altura < 164|0.25|0.25|1.00|2.00|


### 5. Modelo OneR (puntos: 1)
 
|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|
|Alta|Baja|Media|No|
|Media|Alta|Alta|Si|
|Baja|Baja|Baja|Si|
|Baja|Baja|Baja|Si|
|Alta|Baja|Media|Si|
|Media|Alta|Alta|Si|
|Alta|Alta|Alta|Si|
|Alta|Alta|Alta|Si|


Mejor atributo: Edad


|Reglas con Edad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Edad = Alta → Clase = Si|0.75|4|
|Edad = Media → Clase = Si|1.00|2|
|Edad = Baja → Clase = Si|1.00|2|



|Reglas con Altura (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Altura = Alta → Clase = Si|1.00|4|
|Altura = Baja → Clase = Si|0.75|4|



|Reglas con Habilidad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Habilidad = Alta → Clase = Si|1.00|4|
|Habilidad = Media → Clase = Si|0.50|2|
|Habilidad = Baja → Clase = Si|1.00|2|


### 6. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Alta', 'Baja', 'Baja', 'Media', 'Alta', 'Alta', 'Alta']


Valores nuevos: [2, 3, 1, 1, 2, 3, 3, 3]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|17|163|2|No|
|2|16|165|3|Si|
|3|15|157|1|Si|
|4|15|146|1|Si|
|5|17|141|2|Si|
|6|16|166|3|Si|
|7|19|164|3|Si|
|8|18|214|3|Si|


### 7. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|2|9|1|
|2|8|3|2|
|3|37|86|1|


b) Falso, 1 indica que el clustering es bueno (máxima cohesión y separación), y -1 que es malo (mínima cohesión y separación). 

### 8. Perceptrón (puntos: 1)
 a) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cuál es el valor máximo del atributo Edad  para que un ejemplo con Altura=163 y Habilidad=2 pertenezca a la Clase=No?

Recordamos que w=6, 1, 44 y b=363

Dados esos valores, y asumiendo que $a_0$, $a_1$ y $a_2$ son los valores para los atributos Edad, Altura, Habilidad, para que el modelo esté entre generar 0 o 1 debe cumplirse:

$a_0 . w0 + a_1 . w_1 + a_2 . w_2 = b$

$a_0 . w0 = b - a_1 . w_1 - a_2 . w_2$

$a_0  = (b - a_1 . w_1 - a_2 . w_2)/w_0$

$a_0  = (363 - 163 . 1 - 2 44)/6$

$a_0 = 18.666666666666668$

Como buscamos que esté en clase No, y el signo de $w_0$ es positivo, necesitamos que $a_0$ tenga como valor máximo 18.666666666666668.

b) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Edad vale 16, Altura vale 141 y Habilidad vale 3?

La salida neta es 6×16+1×141+44×3 =369, y por ende la salida es 1 (369>=363), con clase Si

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
