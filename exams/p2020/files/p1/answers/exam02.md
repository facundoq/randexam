---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|18|167|Alta|Si|
|2|17|178|Media|No|
|3|19|172|Alta|Si|
|4|19|199|Media|No|
|5|19|185|Media|Si|
|6|19|172|Baja|Si|
|7|18|178|Alta|Si|
|8|19|176|Media|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 1, 0, 2, 1, 0, 1, 0]

Intervalos: [[167.0,177.67), [177.67,188.33), [188.33,199.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 2, 0, 2, 2, 0, 2, 1]

Intervalos: [[167,176), [176,178), [178,199]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-17.00)/2.00

Valores normalizados: 0.50, 0.00, 1.00, 1.00, 1.00, 1.00, 0.50, 1.00

Normalización mu/std con transformación (x-18.50)/0.71

Valores normalizados: -0.71, -2.12, 0.71, 0.71, 0.71, 0.71, -0.71, 0.71

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.954434002924965


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.76|0.41|
|Ganancia|0.20|0.55|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|17.5|0.76|0.2|
|18.5|0.95|0.0|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.38|0.38|1.00|1.60|
|Edad < 18 and Habilidad = Baja → Altura < 178|0.00|0.00|1.00|inf|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Media', 'Alta', 'Media', 'Media', 'Baja', 'Alta', 'Media']


Valores nuevos: [3, 2, 3, 2, 2, 1, 3, 2]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|18|167|3|Si|
|2|17|178|2|No|
|3|19|172|3|Si|
|4|19|199|2|No|
|5|19|185|2|Si|
|6|19|172|1|Si|
|7|18|178|3|Si|
|8|19|176|2|No|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|85|326|1|
|2|6|53|1|
|3|21|170|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[5, 1, 44]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=369*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|5×18+1×167+44×3 =389|5×17+1×178+44×2 =351|5×19+1×172+44×3 =399|
|Salida|1 (389>=369)|0 (351<369)|1 (399>=369)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
