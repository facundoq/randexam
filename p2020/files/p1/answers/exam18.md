---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|17|181|Media|No|
|2|17|165|Baja|Si|
|3|17|177|Alta|Si|
|4|18|148|Alta|No|
|5|18|140|Baja|Si|
|6|19|178|Baja|Si|
|7|16|173|Baja|Si|
|8|17|182|Baja|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 1, 2, 0, 0, 2, 2, 2]

Intervalos: [[140.0,154.0), [154.0,168.0), [168.0,182.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 0, 1, 0, 0, 2, 1, 2]

Intervalos: [[140,173), [173,178), [178,182]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-16.00)/3.00

Valores normalizados: 0.33, 0.33, 0.33, 0.67, 0.67, 1.00, 0.00, 0.33

Normalización mu/std con transformación (x-17.38)/0.86

Valores normalizados: -0.44, -0.44, -0.44, 0.73, 0.73, 1.90, -1.60, -0.44

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.954434002924965


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.86|0.70|
|Ganancia|0.09|0.25|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|16.5|0.86|0.09|
|17.5|0.95|0.0|
|18.5|0.86|0.09|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.12|0.25|0.50|0.80|
|Edad < 17 and Habilidad = Baja → Altura < 168|0.00|0.12|0.00|0.00|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Baja', 'Alta', 'Alta', 'Baja', 'Baja', 'Baja', 'Baja']


Valores nuevos: [2, 1, 3, 3, 1, 1, 1, 1]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|17|181|2|No|
|2|17|165|1|Si|
|3|17|177|3|Si|
|4|18|148|3|No|
|5|18|140|1|Si|
|6|19|178|1|Si|
|7|16|173|1|Si|
|8|17|182|1|No|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|65|1|2|
|2|64|258|1|
|3|20|18|2|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[12, 2, 124]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=746*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|12×17+2×181+124×2 =814|12×17+2×165+124×1 =658|12×17+2×177+124×3 =930|
|Salida|1 (814>=746)|0 (658<746)|1 (930>=746)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
