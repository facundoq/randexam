---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|215|Alta|No|
|2|17|140|Alta|Si|
|3|17|170|Baja|Si|
|4|16|166|Baja|No|
|5|18|200|Baja|Si|
|6|16|199|Baja|Si|
|7|15|173|Alta|No|
|8|19|177|Media|Si|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 0, 1, 1, 2, 2, 1, 1]

Intervalos: [[140.0,165.0), [165.0,190.0), [190.0,215.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 0, 0, 0, 2, 2, 1, 1]

Intervalos: [[140,173), [173,199), [199,215]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.00, 0.50, 0.50, 0.25, 0.75, 0.25, 0.00, 1.00

Normalización mu/std con transformación (x-16.62)/1.32

Valores normalizados: -1.23, 0.28, 0.28, -0.47, 1.04, -0.47, -1.23, 1.80

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.954434002924965


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.41|0.75|
|Ganancia|0.55|0.20|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.49|0.47|
|16.5|0.41|0.55|
|17.5|0.75|0.2|
|18.5|0.86|0.09|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.12|0.38|0.33|0.53|
|Edad < 17 and Habilidad = Baja → Altura < 180|0.12|0.25|0.50|0.80|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Alta', 'Baja', 'Baja', 'Baja', 'Baja', 'Alta', 'Media']


Valores nuevos: [3, 3, 1, 1, 1, 1, 3, 2]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|215|3|No|
|2|17|140|3|Si|
|3|17|170|1|Si|
|4|16|166|1|No|
|5|18|200|1|Si|
|6|16|199|1|Si|
|7|15|173|3|No|
|8|19|177|2|Si|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|1769|230|2|
|2|1094|3601|1|
|3|10|901|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[6, 1, 53]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=379*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|6×15+1×215+53×3 =464|6×17+1×140+53×3 =401|6×17+1×170+53×1 =325|
|Salida|1 (464>=379)|1 (401>=379)|0 (325<379)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
