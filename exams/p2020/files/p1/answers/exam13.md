---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|18|170|Media|Si|
|2|16|205|Media|No|
|3|15|172|Baja|Si|
|4|17|178|Media|No|
|5|17|207|Alta|Si|
|6|17|143|Alta|Si|
|7|15|144|Media|Si|
|8|16|189|Alta|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 2, 1, 1, 2, 0, 0, 2]

Intervalos: [[143.0,164.33), [164.33,185.67), [185.67,207.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 2, 1, 1, 2, 0, 0, 2]

Intervalos: [[143,172), [172,189), [189,207]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/3.00

Valores normalizados: 1.00, 0.33, 0.00, 0.67, 0.67, 0.67, 0.00, 0.33

Normalización mu/std con transformación (x-16.38)/0.99

Valores normalizados: 1.64, -0.38, -1.39, 0.63, 0.63, 0.63, -1.39, -0.38

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.954434002924965


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.75|0.84|
|Ganancia|0.20|0.11|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.75|0.2|
|16.5|0.91|0.05|
|17.5|0.86|0.09|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.25|0.38|0.67|1.07|
|Edad < 16 and Habilidad = Baja → Altura < 176|0.12|0.12|1.00|2.00|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Media', 'Baja', 'Media', 'Alta', 'Alta', 'Media', 'Alta']


Valores nuevos: [2, 2, 1, 2, 3, 3, 2, 3]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|18|170|2|Si|
|2|16|205|2|No|
|3|15|172|1|Si|
|4|17|178|2|No|
|5|17|207|3|Si|
|6|17|143|3|Si|
|7|15|144|2|Si|
|8|16|189|3|No|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|9|1226|1|
|2|1090|1|2|
|3|1|1094|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[12, 2, 88]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=746*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|12×18+2×170+88×2 =732|12×16+2×205+88×2 =778|12×15+2×172+88×1 =612|
|Salida|0 (732<746)|1 (778>=746)|0 (612<746)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
