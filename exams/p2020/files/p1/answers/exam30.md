---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|17|159|Alta|No|
|2|18|178|Baja|No|
|3|17|146|Media|Si|
|4|19|185|Baja|Si|
|5|15|199|Media|No|
|6|19|128|Media|Si|
|7|19|178|Baja|Si|
|8|15|183|Media|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 2, 0, 2, 2, 0, 2, 2]

Intervalos: [[128.0,151.67), [151.67,175.33), [175.33,199.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 1, 0, 2, 2, 0, 1, 2]

Intervalos: [[128,178), [178,183), [183,199]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.50, 0.75, 0.50, 1.00, 0.00, 1.00, 1.00, 0.00

Normalización mu/std con transformación (x-17.38)/1.58

Valores normalizados: -0.24, 0.40, -0.24, 1.03, -1.51, 1.03, 1.03, -1.51

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 1.0


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.45|0.84|
|Ganancia|0.55|0.16|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|16.0|0.69|0.31|
|17.5|0.81|0.19|
|18.5|0.45|0.55|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.00|0.12|0.00|0.00|
|Edad < 17 and Habilidad = Baja → Altura < 170|0.00|0.00|1.00|inf|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Baja', 'Media', 'Baja', 'Media', 'Media', 'Baja', 'Media']


Valores nuevos: [3, 1, 2, 1, 2, 2, 1, 2]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|17|159|3|No|
|2|18|178|1|No|
|3|17|146|2|Si|
|4|19|185|1|Si|
|5|15|199|2|No|
|6|19|128|2|Si|
|7|19|178|1|Si|
|8|15|183|2|No|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|365|681|1|
|2|1|51|1|
|3|1025|1525|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[12, 2, 113]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=745*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|12×17+2×159+113×3 =861|12×18+2×178+113×1 =685|12×17+2×146+113×2 =722|
|Salida|1 (861>=745)|0 (685<745)|0 (722<745)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
