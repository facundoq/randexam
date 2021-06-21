---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|17|199|Alta|Si|
|2|16|165|Alta|Si|
|3|16|176|Baja|No|
|4|15|152|Baja|No|
|5|19|118|Media|Si|
|6|17|183|Alta|No|
|7|15|187|Alta|No|
|8|19|155|Baja|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 1, 2, 1, 0, 2, 2, 1]

Intervalos: [[118.0,145.0), [145.0,172.0), [172.0,199.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 1, 1, 0, 0, 2, 2, 0]

Intervalos: [[118,165), [165,183), [183,199]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.50, 0.25, 0.25, 0.00, 1.00, 0.50, 0.00, 1.00

Normalización mu/std con transformación (x-16.75)/1.48

Valores normalizados: 0.17, -0.51, -0.51, -1.18, 1.52, 0.17, -1.18, 1.52

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.954434002924965


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.75|0.50|
|Ganancia|0.20|0.45|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.75|0.2|
|16.5|0.91|0.05|
|18.0|0.94|0.02|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.25|0.50|0.50|1.33|
|Edad < 17 and Habilidad = Baja → Altura < 167|0.12|0.25|0.50|1.00|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Alta', 'Baja', 'Baja', 'Media', 'Alta', 'Alta', 'Baja']


Valores nuevos: [3, 3, 1, 1, 2, 3, 3, 1]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|17|199|3|Si|
|2|16|165|3|Si|
|3|16|176|1|No|
|4|15|152|1|No|
|5|19|118|2|Si|
|6|17|183|3|No|
|7|15|187|3|No|
|8|19|155|1|No|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|1161|145|2|
|2|4|486|1|
|3|121|123|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[12, 2, 93]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=732*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|12×17+2×199+93×3 =881|12×16+2×165+93×3 =801|12×16+2×176+93×1 =637|
|Salida|1 (881>=732)|1 (801>=732)|0 (637<732)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
