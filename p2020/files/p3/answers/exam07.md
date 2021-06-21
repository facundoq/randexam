---
title: Minería de Datos usando Sistemas Inteligentes
author: Tercera Fecha - 15 de Julio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|153|Baja|Si|
|2|15|171|Alta|No|
|3|18|190|Media|No|
|4|16|162|Alta|Si|
|5|18|162|Media|Si|
|6|19|168|Alta|Si|
|7|18|178|Alta|Si|
|8|15|195|Alta|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 1, 2, 0, 0, 1, 1, 2]

Intervalos: [[153.0,167.0), [167.0,181.0), [181.0,195.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 1, 2, 0, 0, 1, 2, 2]

Intervalos: [[153,168), [168,178), [178,195]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.25, 0.00, 0.75, 0.25, 0.75, 1.00, 0.75, 0.00

Normalización mu/std con transformación (x-16.88)/1.45

Valores normalizados: -0.60, -1.29, 0.77, -0.60, 0.77, 1.46, 0.77, -1.29

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.954434002924965


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.49|0.86|
|Ganancia|0.47|0.10|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.49|0.47|
|17.0|0.91|0.05|
|18.5|0.86|0.09|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.38|0.62|0.60|0.96|
|Edad < 17 and Habilidad = Baja → Altura < 172|0.12|0.12|1.00|1.60|


### 5. Modelo OneR (puntos: 1)
 
|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|
|Media|Baja|Baja|Si|
|Baja|Alta|Alta|No|
|Alta|Alta|Media|No|
|Media|Baja|Alta|Si|
|Alta|Baja|Media|Si|
|Alta|Baja|Alta|Si|
|Alta|Alta|Alta|Si|
|Baja|Alta|Alta|No|


Mejor atributo: Edad


|Reglas con Edad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Edad = Alta → Clase = Si|0.75|4|
|Edad = Media → Clase = Si|1.00|2|
|Edad = Baja → Clase = No|1.00|2|



|Reglas con Altura (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Altura = Alta → Clase = No|0.75|4|
|Altura = Baja → Clase = Si|1.00|4|



|Reglas con Habilidad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.60|5|
|Habilidad = Media → Clase = Si|0.50|2|
|Habilidad = Baja → Clase = Si|1.00|1|


### 6. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Alta', 'Media', 'Alta', 'Media', 'Alta', 'Alta', 'Alta']


Valores nuevos: [1, 3, 2, 3, 2, 3, 3, 3]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|153|1|Si|
|2|15|171|3|No|
|3|18|190|2|No|
|4|16|162|3|Si|
|5|18|162|2|Si|
|6|19|168|3|Si|
|7|18|178|3|Si|
|8|15|195|3|No|


### 7. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|225|1374|1|
|2|14|371|1|
|3|489|0|2|


b) Falso, 1 indica que el clustering es bueno (máxima cohesión y separación), y -1 que es malo (mínima cohesión y separación). 

### 8. Perceptrón (puntos: 1)
 a) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cuál es el valor máximo del atributo Edad  para que un ejemplo con Altura=171 y Habilidad=3 pertenezca a la Clase=No?

Recordamos que w=12, 2, 80 y b=747

Dados esos valores, y asumiendo que $a_0$, $a_1$ y $a_2$ son los valores para los atributos Edad, Altura, Habilidad, para que el modelo esté entre generar 0 o 1 debe cumplirse:

$a_0 . w0 + a_1 . w_1 + a_2 . w_2 = b$

$a_0 . w0 = b - a_1 . w_1 - a_2 . w_2$

$a_0  = (b - a_1 . w_1 - a_2 . w_2)/w_0$

$a_0  = (747 - 171 . 2 - 3 80)/12$

$a_0 = 13.75$

Como buscamos que esté en clase No, y el signo de $w_0$ es positivo, necesitamos que $a_0$ tenga como valor máximo 13.75.

b) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Edad vale 19, Altura vale 162 y Habilidad vale 1?

La salida neta es 12×19+2×162+80×1 =632, y por ende la salida es 0 (632<747), con clase No

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
