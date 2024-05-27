---
title: Minería de Datos usando Sistemas Inteligentes
author: Tercera Fecha - 15 de Julio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|163|Baja|No|
|2|16|185|Alta|Si|
|3|16|132|Baja|No|
|4|15|204|Media|Si|
|5|19|199|Baja|No|
|6|17|163|Alta|No|
|7|17|182|Alta|Si|
|8|16|170|Baja|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 2, 0, 2, 2, 1, 2, 1]

Intervalos: [[132.0,156.0), [156.0,180.0), [180.0,204.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 2, 0, 2, 2, 0, 1, 1]

Intervalos: [[132,170), [170,185), [185,204]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.25, 0.25, 0.25, 0.00, 1.00, 0.50, 0.50, 0.25

Normalización mu/std con transformación (x-16.50)/1.12

Valores normalizados: -0.45, -0.45, -0.45, -1.34, 2.24, 0.45, 0.45, -0.45

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.954434002924965


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.76|0.34|
|Ganancia|0.20|0.61|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.76|0.2|
|16.5|0.95|0.0|
|18.0|0.86|0.09|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.25|0.38|0.67|1.78|
|Edad < 16 and Habilidad = Baja → Altura < 175|0.00|0.00|1.00|inf|


### 5. Modelo OneR (puntos: 1)
 
|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|
|Media|Baja|Baja|No|
|Media|Alta|Alta|Si|
|Media|Baja|Baja|No|
|Baja|Alta|Media|Si|
|Alta|Alta|Baja|No|
|Alta|Baja|Alta|No|
|Alta|Alta|Alta|Si|
|Media|Baja|Baja|No|


Mejor atributo: Altura


|Reglas con Edad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Edad = Alta → Clase = No|0.67|3|
|Edad = Media → Clase = No|0.75|4|
|Edad = Baja → Clase = Si|1.00|1|



|Reglas con Altura (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Altura = Alta → Clase = Si|0.75|4|
|Altura = Baja → Clase = No|1.00|4|



|Reglas con Habilidad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.67|3|
|Habilidad = Media → Clase = Si|1.00|1|
|Habilidad = Baja → Clase = No|1.00|4|


### 6. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Alta', 'Baja', 'Media', 'Baja', 'Alta', 'Alta', 'Baja']


Valores nuevos: [1, 3, 1, 2, 1, 3, 3, 1]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|163|1|No|
|2|16|185|3|Si|
|3|16|132|1|No|
|4|15|204|2|Si|
|5|19|199|1|No|
|6|17|163|3|No|
|7|17|182|3|Si|
|8|16|170|1|No|


### 7. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|49|1298|1|
|2|229|198|2|
|3|1444|4491|1|


b) Falso, 1 indica que el clustering es bueno (máxima cohesión y separación), y -1 que es malo (mínima cohesión y separación). 

### 8. Perceptrón (puntos: 1)
 a) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cuál es el valor máximo del atributo Edad  para que un ejemplo con Altura=185 y Habilidad=3 pertenezca a la Clase=No?

Recordamos que w=12, 2, 106 y b=746

Dados esos valores, y asumiendo que $a_0$, $a_1$ y $a_2$ son los valores para los atributos Edad, Altura, Habilidad, para que el modelo esté entre generar 0 o 1 debe cumplirse:

$a_0 . w0 + a_1 . w_1 + a_2 . w_2 = b$

$a_0 . w0 = b - a_1 . w_1 - a_2 . w_2$

$a_0  = (b - a_1 . w_1 - a_2 . w_2)/w_0$

$a_0  = (746 - 185 . 2 - 3 106)/12$

$a_0 = 4.833333333333333$

Como buscamos que esté en clase No, y el signo de $w_0$ es positivo, necesitamos que $a_0$ tenga como valor máximo 4.833333333333333.

b) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Edad vale 16, Altura vale 185 y Habilidad vale 1?

La salida neta es 12×16+2×185+106×1 =668, y por ende la salida es 0 (668<746), con clase No

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
