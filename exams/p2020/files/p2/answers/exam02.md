---
title: Minería de Datos usando Sistemas Inteligentes
author: Segunda Fecha - 1 de Julio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|202|Alta|Si|
|2|17|157|Baja|No|
|3|18|159|Media|No|
|4|16|148|Baja|No|
|5|15|187|Media|No|
|6|19|123|Baja|No|
|7|17|204|Alta|Si|
|8|19|154|Baja|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 1, 1, 0, 2, 0, 2, 1]

Intervalos: [[123.0,150.0), [150.0,177.0), [177.0,204.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 1, 1, 0, 2, 0, 2, 0]

Intervalos: [[123,157), [157,187), [187,204]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.25, 0.50, 0.75, 0.25, 0.00, 1.00, 0.50, 1.00

Normalización mu/std con transformación (x-17.12)/1.36

Valores normalizados: -0.83, -0.09, 0.64, -0.83, -1.56, 1.38, -0.09, 1.38

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.8112781244591328


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.61|0.00|
|Ganancia|0.20|0.81|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.76|0.06|
|16.5|0.8|0.02|
|17.5|0.61|0.2|
|18.5|0.69|0.12|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.25|0.25|1.00|4.00|
|Edad < 17 and Habilidad = Baja → Altura < 167|0.12|0.12|1.00|1.60|


### 5. Modelo OneR (puntos: 1)
 
|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|
|Baja|Alta|Alta|Si|
|Media|Baja|Baja|No|
|Alta|Alta|Media|No|
|Baja|Baja|Baja|No|
|Baja|Alta|Media|No|
|Alta|Baja|Baja|No|
|Media|Alta|Alta|Si|
|Alta|Baja|Baja|No|


Mejor atributo: Habilidad


|Reglas con Edad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Edad = Baja → Clase = No|0.67|3|
|Edad = Media → Clase = No|0.50|2|
|Edad = Alta → Clase = No|1.00|3|



|Reglas con Altura (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Altura = Alta → Clase = No|0.50|4|
|Altura = Baja → Clase = No|1.00|4|



|Reglas con Habilidad (accuracy=1.0)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Habilidad = Alta → Clase = Si|1.00|2|
|Habilidad = Media → Clase = No|1.00|2|
|Habilidad = Baja → Clase = No|1.00|4|


### 6. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Baja', 'Media', 'Baja', 'Media', 'Baja', 'Alta', 'Baja']


Valores nuevos: [3, 1, 2, 1, 2, 1, 3, 1]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|202|3|Si|
|2|17|157|1|No|
|3|18|159|2|No|
|4|16|148|1|No|
|5|15|187|2|No|
|6|19|123|1|No|
|7|17|204|3|Si|
|8|19|154|1|No|


### 7. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|2029|5|2|
|2|1|2027|1|
|3|9|1849|1|


a) La afirmación es verdadera porque el Silhouette calcula para cada ejemplo su distancia promedio con los de su grupo y con los del grupo más cercano con esto obtiene el índice de cada ejmplo y finalmente los promedia. Por otro lado, DB compara agrupamientos y se espera que la cantidad de grupos sea considerablemente menor a la de ejemplos. Si esto último no ocurre, podría darse que DB fuera más costoso computacionalmente hablando pero este escenario no tiene mucho sentido en un contexto donde se busca construir un modelo descriptivo.

### 8. Perceptrón (puntos: 1)
 a) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cuál es el valor máximo del atributo Edad  para que un ejemplo con Altura=202 y Habilidad=3 pertenezca a la Clase=No?

Recordamos que w=6, 1, 56 y b=367

Dados esos valores, y asumiendo que $a_0$, $a_1$ y $a_2$ son los valores para los atributos Edad, Altura, Habilidad, para que el modelo esté entre generar 0 o 1 debe cumplirse:

$a_0 . w0 + a_1 . w_1 + a_2 . w_2 = b$

$a_0 . w0 = b - a_1 . w_1 - a_2 . w_2$

$a_0  = (b - a_1 . w_1 - a_2 . w_2)/w_0$

$a_0  = (367 - 202 . 1 - 3 56)/6$

$a_0 = -0.5$

Como buscamos que esté en clase No, y el signo de $w_0$ es positivo, necesitamos que $a_0$ tenga como valor máximo -0.5.

b) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Edad vale 16, Altura vale 204 y Habilidad vale 3?

La salida neta es 6×16+1×204+56×3 =468, y por ende la salida es 1 (468>=367), con clase Si

### 9. Verdadero o Falso (puntos: 1)
 V,F,V,V,V,V,F
