---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|17|155|Alta|No|
|2|17|153|Baja|No|
|3|17|168|Media|No|
|4|18|156|Media|Si|
|5|16|192|Alta|Si|
|6|16|148|Media|No|
|7|15|147|Baja|No|
|8|18|161|Baja|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 0, 1, 0, 2, 0, 0, 0]

Intervalos: [[147.0,162.0), [162.0,177.0), [177.0,192.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 0, 2, 1, 2, 0, 0, 2]

Intervalos: [[147,155), [155,161), [161,192]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/3.00

Valores normalizados: 0.67, 0.67, 0.67, 1.00, 0.33, 0.33, 0.00, 1.00

Normalización mu/std con transformación (x-16.75)/0.97

Valores normalizados: 0.26, 0.26, 0.26, 1.29, -0.77, -0.77, -1.81, 1.29

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.8112781244591328


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.74|0.59|
|Ganancia|0.07|0.22|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.76|0.06|
|16.5|0.8|0.02|
|17.5|0.74|0.07|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.12|0.25|0.50|2.00|
|Edad < 17 and Habilidad = Baja → Altura < 160|0.12|0.12|1.00|1.60|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Baja', 'Media', 'Media', 'Alta', 'Media', 'Baja', 'Baja']


Valores nuevos: [3, 1, 2, 2, 3, 2, 1, 1]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|17|155|3|No|
|2|17|153|1|No|
|3|17|168|2|No|
|4|18|156|2|Si|
|5|16|192|3|Si|
|6|16|148|2|No|
|7|15|147|1|No|
|8|18|161|1|No|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|5|170|1|
|2|5|226|1|
|3|171|0|2|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[6, 1, 53]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=359*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|6×17+1×155+53×3 =416|6×17+1×153+53×1 =308|6×17+1×168+53×2 =376|
|Salida|1 (416>=359)|0 (308<359)|1 (376>=359)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
