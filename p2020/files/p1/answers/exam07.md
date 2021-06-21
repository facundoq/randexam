---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|17|137|Baja|Si|
|2|15|165|Alta|No|
|3|17|152|Media|Si|
|4|15|177|Alta|No|
|5|15|159|Alta|Si|
|6|18|146|Baja|No|
|7|17|169|Alta|No|
|8|19|178|Baja|Si|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 2, 1, 2, 1, 0, 2, 2]

Intervalos: [[137.0,150.67), [150.67,164.33), [164.33,178.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 1, 0, 2, 1, 0, 2, 2]

Intervalos: [[137,159), [159,169), [169,178]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.50, 0.00, 0.50, 0.00, 0.00, 0.75, 0.50, 1.00

Normalización mu/std con transformación (x-16.62)/1.41

Valores normalizados: 0.27, -1.15, 0.27, -1.15, -1.15, 0.98, 0.27, 1.69

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 1.0


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.86|0.75|
|Ganancia|0.14|0.25|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|16.0|0.95|0.05|
|17.5|1.0|0.0|
|18.5|0.86|0.14|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.12|0.50|0.25|0.50|
|Edad < 17 and Habilidad = Baja → Altura < 160|0.00|0.00|1.00|inf|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Alta', 'Media', 'Alta', 'Alta', 'Baja', 'Alta', 'Baja']


Valores nuevos: [1, 3, 2, 3, 3, 1, 3, 1]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|17|137|1|Si|
|2|15|165|3|No|
|3|17|152|2|Si|
|4|15|177|3|No|
|5|15|159|3|Si|
|6|18|146|1|No|
|7|17|169|3|No|
|8|19|178|1|Si|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|488|1601|1|
|2|40|149|1|
|3|54|625|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[6, 1, 46]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=357*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|6×17+1×137+46×1 =285|6×15+1×165+46×3 =393|6×17+1×152+46×2 =346|
|Salida|0 (285<357)|1 (393>=357)|0 (346<357)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
