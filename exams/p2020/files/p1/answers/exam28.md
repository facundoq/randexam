---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|19|169|Alta|Si|
|2|18|177|Media|Si|
|3|18|215|Media|Si|
|4|16|169|Media|No|
|5|19|150|Baja|No|
|6|18|163|Alta|Si|
|7|18|160|Baja|No|
|8|15|179|Alta|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 1, 2, 0, 0, 0, 0, 1]

Intervalos: [[150.0,171.67), [171.67,193.33), [193.33,215.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 2, 2, 1, 0, 0, 0, 2]

Intervalos: [[150,169), [169,177), [177,215]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 1.00, 0.75, 0.75, 0.25, 1.00, 0.75, 0.75, 0.00

Normalización mu/std con transformación (x-17.62)/1.32

Valores normalizados: 1.04, 0.28, 0.28, -1.23, 1.04, 0.28, 0.28, -1.99

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 1.0


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.69|0.69|
|Ganancia|0.31|0.31|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.86|0.14|
|17.0|0.69|0.31|
|18.5|1.0|0.0|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.25|0.38|0.67|1.33|
|Edad < 18 and Habilidad = Baja → Altura < 173|0.00|0.00|1.00|inf|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Media', 'Media', 'Media', 'Baja', 'Alta', 'Baja', 'Alta']


Valores nuevos: [3, 2, 2, 2, 1, 3, 1, 3]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|19|169|3|Si|
|2|18|177|2|Si|
|3|18|215|2|Si|
|4|16|169|2|No|
|5|19|150|1|No|
|6|18|163|3|Si|
|7|18|160|1|No|
|8|15|179|3|No|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|5|102|1|
|2|65|4|2|
|3|2117|1296|2|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[12, 2, 93]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=754*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|12×19+2×169+93×3 =845|12×18+2×177+93×2 =756|12×18+2×215+93×2 =832|
|Salida|1 (845>=754)|1 (756>=754)|1 (832>=754)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
