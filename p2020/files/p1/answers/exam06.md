---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|149|Media|Si|
|2|15|141|Baja|Si|
|3|19|135|Alta|Si|
|4|18|209|Baja|No|
|5|15|159|Baja|Si|
|6|16|161|Baja|Si|
|7|18|144|Baja|Si|
|8|15|185|Alta|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 0, 0, 2, 0, 1, 0, 2]

Intervalos: [[135.0,159.67), [159.67,184.33), [184.33,209.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 0, 0, 2, 1, 2, 0, 2]

Intervalos: [[135,149), [149,161), [161,209]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.25, 0.00, 1.00, 0.75, 0.00, 0.25, 0.75, 0.00

Normalización mu/std con transformación (x-16.50)/1.50

Valores normalizados: -0.33, -1.00, 1.67, 1.00, -1.00, -0.33, 1.00, -1.00

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.8112781244591328


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.76|0.70|
|Ganancia|0.06|0.11|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.8|0.02|
|17.0|0.8|0.02|
|18.5|0.76|0.06|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.12|0.25|0.50|0.67|
|Edad < 16 and Habilidad = Baja → Altura < 160|0.25|0.25|1.00|1.60|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Baja', 'Alta', 'Baja', 'Baja', 'Baja', 'Baja', 'Alta']


Valores nuevos: [2, 1, 3, 1, 1, 1, 1, 3]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|149|2|Si|
|2|15|141|1|Si|
|3|19|135|3|Si|
|4|18|209|1|No|
|5|15|159|1|Si|
|6|16|161|1|Si|
|7|18|144|1|Si|
|8|15|185|3|No|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|2|1300|1|
|2|64|1946|1|
|3|216|2502|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[6, 1, 62]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=360*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|6×16+1×149+62×2 =369|6×15+1×141+62×1 =293|6×19+1×135+62×3 =435|
|Salida|1 (369>=360)|0 (293<360)|1 (435>=360)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
