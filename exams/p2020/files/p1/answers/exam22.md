---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|193|Alta|No|
|2|16|176|Media|No|
|3|15|188|Alta|Si|
|4|15|176|Media|No|
|5|17|187|Baja|No|
|6|17|156|Alta|Si|
|7|15|149|Baja|No|
|8|17|183|Baja|Si|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 1, 2, 1, 2, 0, 0, 2]

Intervalos: [[149.0,163.67), [163.67,178.33), [178.33,193.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 1, 2, 1, 2, 0, 0, 1]

Intervalos: [[149,176), [176,187), [187,193]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/2.00

Valores normalizados: 0.00, 0.50, 0.00, 0.00, 1.00, 1.00, 0.00, 1.00

Normalización mu/std con transformación (x-15.88)/0.93

Valores normalizados: -0.94, 0.13, -0.94, -0.94, 1.21, 1.21, -0.94, 1.21

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.954434002924965


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.80|0.69|
|Ganancia|0.16|0.27|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.91|0.05|
|16.5|0.8|0.16|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.25|0.38|0.67|1.78|
|Edad < 16 and Habilidad = Baja → Altura < 176|0.12|0.12|1.00|4.00|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Media', 'Alta', 'Media', 'Baja', 'Alta', 'Baja', 'Baja']


Valores nuevos: [3, 2, 3, 2, 1, 3, 1, 1]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|193|3|No|
|2|16|176|2|No|
|3|15|188|3|Si|
|4|15|176|2|No|
|5|17|187|1|No|
|6|17|156|3|Si|
|7|15|149|1|No|
|8|17|183|1|Si|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|293|30|2|
|2|2|145|1|
|3|148|5|2|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[6, 1, 50]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=371*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|6×15+1×193+50×3 =433|6×16+1×176+50×2 =372|6×15+1×188+50×3 =428|
|Salida|1 (433>=371)|1 (372>=371)|1 (428>=371)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
