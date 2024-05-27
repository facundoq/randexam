---
title: Minería de Datos usando Sistemas Inteligentes
author: Tercera Fecha - 15 de Julio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|17|148|Baja|Si|
|2|19|151|Alta|No|
|3|19|181|Alta|Si|
|4|18|215|Media|No|
|5|19|170|Media|No|
|6|18|147|Baja|No|
|7|18|180|Alta|Si|
|8|18|158|Media|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 0, 1, 2, 1, 0, 1, 0]

Intervalos: [[147.0,169.67), [169.67,192.33), [192.33,215.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 0, 2, 2, 1, 0, 2, 1]

Intervalos: [[147,158), [158,180), [180,215]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-17.00)/2.00

Valores normalizados: 0.00, 1.00, 1.00, 0.50, 1.00, 0.50, 0.50, 0.50

Normalización mu/std con transformación (x-18.25)/0.66

Valores normalizados: -1.89, 1.13, 1.13, -0.38, 1.13, -0.38, -0.38, -0.38

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.954434002924965


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.76|0.59|
|Ganancia|0.20|0.36|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|17.5|0.76|0.2|
|18.5|0.95|0.0|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.25|0.38|0.67|1.78|
|Edad < 18 and Habilidad = Baja → Altura < 169|0.12|0.12|1.00|2.00|


### 5. Modelo OneR (puntos: 1)
 
|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|
|Baja|Baja|Baja|Si|
|Alta|Baja|Alta|No|
|Alta|Alta|Alta|Si|
|Media|Alta|Media|No|
|Alta|Alta|Media|No|
|Media|Baja|Baja|No|
|Media|Alta|Alta|Si|
|Media|Baja|Media|No|


Mejor atributo: Edad


|Reglas con Edad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Edad = Alta → Clase = No|0.67|3|
|Edad = Media → Clase = No|0.75|4|
|Edad = Baja → Clase = Si|1.00|1|



|Reglas con Altura (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Altura = Alta → Clase = Si|0.50|4|
|Altura = Baja → Clase = No|0.75|4|



|Reglas con Habilidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.67|3|
|Habilidad = Media → Clase = No|1.00|3|
|Habilidad = Baja → Clase = Si|0.50|2|


### 6. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Alta', 'Alta', 'Media', 'Media', 'Baja', 'Alta', 'Media']


Valores nuevos: [1, 3, 3, 2, 2, 1, 3, 2]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|17|148|1|Si|
|2|19|151|3|No|
|3|19|181|3|Si|
|4|18|215|2|No|
|5|19|170|2|No|
|6|18|147|1|No|
|7|18|180|3|Si|
|8|18|158|2|No|


### 7. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|101|1094|1|
|2|54|901|1|
|3|534|1|2|


b) Falso, 1 indica que el clustering es bueno (máxima cohesión y separación), y -1 que es malo (mínima cohesión y separación). 

### 8. Perceptrón (puntos: 1)
 a) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cuál es el valor máximo del atributo Edad  para que un ejemplo con Altura=158 y Habilidad=1 pertenezca a la Clase=No?

Recordamos que w=10, 2, 93 y b=717

Dados esos valores, y asumiendo que $a_0$, $a_1$ y $a_2$ son los valores para los atributos Edad, Altura, Habilidad, para que el modelo esté entre generar 0 o 1 debe cumplirse:

$a_0 . w0 + a_1 . w_1 + a_2 . w_2 = b$

$a_0 . w0 = b - a_1 . w_1 - a_2 . w_2$

$a_0  = (b - a_1 . w_1 - a_2 . w_2)/w_0$

$a_0  = (717 - 158 . 2 - 1 93)/10$

$a_0 = 30.8$

Como buscamos que esté en clase No, y el signo de $w_0$ es positivo, necesitamos que $a_0$ tenga como valor máximo 30.8.

b) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Edad vale 18, Altura vale 215 y Habilidad vale 1?

La salida neta es 10×18+2×215+93×1 =703, y por ende la salida es 0 (703<717), con clase No

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
