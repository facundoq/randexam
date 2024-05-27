---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|18|162|Baja|Si|
|2|16|165|Media|Si|
|3|16|191|Baja|No|
|4|17|183|Media|Si|
|5|16|182|Alta|Si|
|6|18|137|Baja|Si|
|7|16|169|Media|No|
|8|19|155|Media|Si|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 1, 2, 2, 2, 0, 1, 1]

Intervalos: [[137.0,155.0), [155.0,173.0), [173.0,191.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 1, 2, 2, 2, 0, 1, 0]

Intervalos: [[137,165), [165,182), [182,191]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-16.00)/3.00

Valores normalizados: 0.67, 0.00, 0.00, 0.33, 0.00, 0.67, 0.00, 1.00

Normalización mu/std con transformación (x-17.00)/1.12

Valores normalizados: 0.89, -0.89, -0.89, 0.00, -0.89, 0.89, -0.89, 1.79

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.8112781244591328


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.50|0.75|
|Ganancia|0.31|0.06|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|16.5|0.5|0.31|
|17.5|0.61|0.2|
|18.5|0.76|0.06|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.12|0.12|1.00|1.33|
|Edad < 17 and Habilidad = Baja → Altura < 168|0.00|0.12|0.00|0.00|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Media', 'Baja', 'Media', 'Alta', 'Baja', 'Media', 'Media']


Valores nuevos: [1, 2, 1, 2, 3, 1, 2, 2]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|18|162|1|Si|
|2|16|165|2|Si|
|3|16|191|1|No|
|4|17|183|2|Si|
|5|16|182|3|Si|
|6|18|137|1|Si|
|7|16|169|2|No|
|8|19|155|2|Si|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|13|442|1|
|2|1|328|1|
|3|676|69|2|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[12, 2, 113]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=737*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|12×18+2×162+113×1 =653|12×16+2×165+113×2 =748|12×16+2×191+113×1 =687|
|Salida|0 (653<737)|1 (748>=737)|0 (687<737)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
