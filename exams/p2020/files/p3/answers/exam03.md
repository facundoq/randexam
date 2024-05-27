---
title: Minería de Datos usando Sistemas Inteligentes
author: Tercera Fecha - 15 de Julio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|19|169|Media|No|
|2|17|193|Media|No|
|3|17|155|Alta|Si|
|4|18|170|Alta|No|
|5|19|152|Baja|No|
|6|15|166|Baja|Si|
|7|15|175|Alta|Si|
|8|17|150|Alta|Si|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 2, 0, 1, 0, 1, 1, 0]

Intervalos: [[150.0,164.33), [164.33,178.67), [178.67,193.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 2, 0, 2, 0, 1, 2, 0]

Intervalos: [[150,166), [166,170), [170,193]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 1.00, 0.50, 0.50, 0.75, 1.00, 0.00, 0.00, 0.50

Normalización mu/std con transformación (x-17.12)/1.45

Valores normalizados: 1.29, -0.09, -0.09, 0.60, 1.29, -1.46, -1.46, -0.09

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 1.0


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.45|0.66|
|Ganancia|0.55|0.34|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|16.0|0.69|0.31|
|17.5|0.45|0.55|
|18.5|0.69|0.31|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.38|0.50|0.75|1.50|
|Edad < 17 and Habilidad = Baja → Altura < 166|0.00|0.12|0.00|0.00|


### 5. Modelo OneR (puntos: 1)
 
|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|
|Alta|Alta|Media|No|
|Media|Alta|Media|No|
|Media|Baja|Alta|Si|
|Alta|Alta|Alta|No|
|Alta|Baja|Baja|No|
|Baja|Baja|Baja|Si|
|Baja|Alta|Alta|Si|
|Media|Baja|Alta|Si|


Mejor atributo: Edad


|Reglas con Edad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Edad = Alta → Clase = No|1.00|3|
|Edad = Media → Clase = Si|0.67|3|
|Edad = Baja → Clase = Si|1.00|2|



|Reglas con Altura (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Altura = Alta → Clase = No|0.75|4|
|Altura = Baja → Clase = Si|0.75|4|



|Reglas con Habilidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.75|4|
|Habilidad = Media → Clase = No|1.00|2|
|Habilidad = Baja → Clase = Si|0.50|2|


### 6. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Media', 'Alta', 'Alta', 'Baja', 'Baja', 'Alta', 'Alta']


Valores nuevos: [2, 2, 3, 3, 1, 1, 3, 3]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|19|169|2|No|
|2|17|193|2|No|
|3|17|155|3|Si|
|4|18|170|3|No|
|5|19|152|1|No|
|6|15|166|1|Si|
|7|15|175|3|Si|
|8|17|150|3|Si|


### 7. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|14|37|1|
|2|730|325|2|
|3|125|402|1|


b) Falso, 1 indica que el clustering es bueno (máxima cohesión y separación), y -1 que es malo (mínima cohesión y separación). 

### 8. Perceptrón (puntos: 1)
 a) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cuál es el valor máximo del atributo Edad  para que un ejemplo con Altura=152 y Habilidad=3 pertenezca a la Clase=No?

Recordamos que w=6, 1, 44 y b=368

Dados esos valores, y asumiendo que $a_0$, $a_1$ y $a_2$ son los valores para los atributos Edad, Altura, Habilidad, para que el modelo esté entre generar 0 o 1 debe cumplirse:

$a_0 . w0 + a_1 . w_1 + a_2 . w_2 = b$

$a_0 . w0 = b - a_1 . w_1 - a_2 . w_2$

$a_0  = (b - a_1 . w_1 - a_2 . w_2)/w_0$

$a_0  = (368 - 152 . 1 - 3 44)/6$

$a_0 = 14.0$

Como buscamos que esté en clase No, y el signo de $w_0$ es positivo, necesitamos que $a_0$ tenga como valor máximo 14.0.

b) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Edad vale 19, Altura vale 175 y Habilidad vale 2?

La salida neta es 6×19+1×175+44×2 =377, y por ende la salida es 1 (377>=368), con clase Si

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
