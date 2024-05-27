---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|182|Media|Si|
|2|15|137|Media|Si|
|3|17|147|Media|Si|
|4|15|171|Baja|No|
|5|15|155|Alta|Si|
|6|16|200|Baja|Si|
|7|15|144|Alta|Si|
|8|17|175|Media|Si|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 0, 0, 1, 0, 2, 0, 1]

Intervalos: [[137.0,158.0), [158.0,179.0), [179.0,200.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 0, 0, 1, 1, 2, 0, 2]

Intervalos: [[137,155), [155,175), [175,200]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/2.00

Valores normalizados: 0.00, 0.00, 1.00, 0.00, 0.00, 0.50, 0.00, 1.00

Normalización mu/std con transformación (x-15.62)/0.86

Valores normalizados: -0.73, -0.73, 1.60, -0.73, -0.73, 0.44, -0.73, 1.60

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.5435644431995964


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.45|0.25|
|Ganancia|0.09|0.29|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.45|0.09|
|16.5|0.49|0.06|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.25|0.25|1.00|1.14|
|Edad < 16 and Habilidad = Baja → Altura < 164|0.00|0.12|0.00|0.00|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Media', 'Media', 'Baja', 'Alta', 'Baja', 'Alta', 'Media']


Valores nuevos: [2, 2, 2, 1, 3, 1, 3, 2]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|182|2|Si|
|2|15|137|2|Si|
|3|17|147|2|Si|
|4|15|171|1|No|
|5|15|155|3|Si|
|6|16|200|1|Si|
|7|15|144|3|Si|
|8|17|175|2|Si|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|730|1|2|
|2|325|2026|1|
|3|69|1226|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[6, 1, 50]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=357*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|6×15+1×182+50×2 =372|6×15+1×137+50×2 =327|6×17+1×147+50×2 =349|
|Salida|1 (372>=357)|0 (327<357)|0 (349<357)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
