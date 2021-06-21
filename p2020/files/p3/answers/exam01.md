---
title: Minería de Datos usando Sistemas Inteligentes
author: Tercera Fecha - 15 de Julio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|161|Baja|Si|
|2|17|168|Baja|No|
|3|17|127|Alta|Si|
|4|19|202|Baja|Si|
|5|18|134|Alta|No|
|6|19|153|Media|No|
|7|19|180|Media|Si|
|8|15|145|Media|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 1, 0, 2, 0, 1, 2, 0]

Intervalos: [[127.0,152.0), [152.0,177.0), [177.0,202.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 2, 0, 2, 0, 1, 2, 0]

Intervalos: [[127,153), [153,168), [168,202]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.00, 0.50, 0.50, 1.00, 0.75, 1.00, 1.00, 0.00

Normalización mu/std con transformación (x-17.38)/1.58

Valores normalizados: -1.51, -0.24, -0.24, 1.03, 0.40, 1.03, 1.03, -1.51

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 1.0


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.95|0.94|
|Ganancia|0.05|0.06|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|16.0|1.0|0.0|
|17.5|1.0|0.0|
|18.5|0.95|0.05|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.12|0.25|0.50|1.00|
|Edad < 17 and Habilidad = Baja → Altura < 159|0.00|0.12|0.00|0.00|


### 5. Modelo OneR (puntos: 1)
 
|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|
|Baja|Alta|Baja|Si|
|Media|Alta|Baja|No|
|Media|Baja|Alta|Si|
|Alta|Alta|Baja|Si|
|Media|Baja|Alta|No|
|Alta|Baja|Media|No|
|Alta|Alta|Media|Si|
|Baja|Baja|Media|No|


Mejor atributo: Altura


|Reglas con Edad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Edad = Alta → Clase = Si|0.67|3|
|Edad = Media → Clase = No|0.67|3|
|Edad = Baja → Clase = Si|0.50|2|



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
 Valores originales: ['Baja', 'Baja', 'Alta', 'Baja', 'Alta', 'Media', 'Media', 'Media']


Valores nuevos: [1, 1, 3, 1, 3, 2, 2, 2]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|161|1|Si|
|2|17|168|1|No|
|3|17|127|3|Si|
|4|19|202|1|Si|
|5|18|134|3|No|
|6|19|153|2|No|
|7|19|180|2|Si|
|8|15|145|2|No|


### 7. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|68|378|1|
|2|225|149|2|
|3|680|2814|1|


b) Falso, 1 indica que el clustering es bueno (máxima cohesión y separación), y -1 que es malo (mínima cohesión y separación). 

### 8. Perceptrón (puntos: 1)
 a) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cuál es el valor máximo del atributo Edad  para que un ejemplo con Altura=180 y Habilidad=3 pertenezca a la Clase=No?

Recordamos que w=12, 2, 106 y b=724

Dados esos valores, y asumiendo que $a_0$, $a_1$ y $a_2$ son los valores para los atributos Edad, Altura, Habilidad, para que el modelo esté entre generar 0 o 1 debe cumplirse:

$a_0 . w0 + a_1 . w_1 + a_2 . w_2 = b$

$a_0 . w0 = b - a_1 . w_1 - a_2 . w_2$

$a_0  = (b - a_1 . w_1 - a_2 . w_2)/w_0$

$a_0  = (724 - 180 . 2 - 3 106)/12$

$a_0 = 3.8333333333333335$

Como buscamos que esté en clase No, y el signo de $w_0$ es positivo, necesitamos que $a_0$ tenga como valor máximo 3.8333333333333335.

b) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Edad vale 19, Altura vale 202 y Habilidad vale 1?

La salida neta es 12×19+2×202+106×1 =738, y por ende la salida es 1 (738>=724), con clase Si

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
