---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|17|175|Alta|No|
|2|15|168|Baja|No|
|3|17|188|Alta|Si|
|4|18|176|Media|Si|
|5|18|185|Alta|No|
|6|18|160|Baja|No|
|7|17|151|Media|Si|
|8|16|161|Baja|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 1, 2, 2, 2, 0, 0, 0]

Intervalos: [[151.0,163.33), [163.33,175.67), [175.67,188.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 1, 2, 2, 2, 0, 0, 0]

Intervalos: [[151,168), [168,176), [176,188]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/3.00

Valores normalizados: 0.67, 0.00, 0.67, 1.00, 1.00, 1.00, 0.67, 0.33

Normalización mu/std con transformación (x-17.00)/1.00

Valores normalizados: 0.00, -2.00, 0.00, 1.00, 1.00, 1.00, 0.00, -1.00

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.954434002924965


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.75|0.34|
|Ganancia|0.20|0.61|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.86|0.09|
|16.5|0.75|0.2|
|17.5|0.95|0.0|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.12|0.38|0.33|0.89|
|Edad < 17 and Habilidad = Baja → Altura < 170|0.25|0.25|1.00|2.00|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Baja', 'Alta', 'Media', 'Alta', 'Baja', 'Media', 'Baja']


Valores nuevos: [3, 1, 3, 2, 3, 1, 2, 1]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|17|175|3|No|
|2|15|168|1|No|
|3|17|188|3|Si|
|4|18|176|2|Si|
|5|18|185|3|No|
|6|18|160|1|No|
|7|17|151|2|Si|
|8|16|161|1|No|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|53|102|1|
|2|4|299|1|
|3|404|11|2|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[6, 1, 50]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=372*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|6×17+1×175+50×3 =427|6×15+1×168+50×1 =308|6×17+1×188+50×3 =440|
|Salida|1 (427>=372)|0 (308<372)|1 (440>=372)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
