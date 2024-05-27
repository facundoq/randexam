---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|153|Alta|No|
|2|19|156|Media|Si|
|3|16|160|Media|No|
|4|15|170|Baja|No|
|5|15|162|Baja|No|
|6|16|142|Alta|Si|
|7|18|157|Media|No|
|8|15|125|Media|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 2, 2, 2, 2, 1, 2, 0]

Intervalos: [[125.0,140.0), [140.0,155.0), [155.0,170.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 1, 2, 2, 2, 0, 1, 0]

Intervalos: [[125,156), [156,160), [160,170]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.00, 1.00, 0.25, 0.00, 0.00, 0.25, 0.75, 0.00

Normalización mu/std con transformación (x-16.12)/1.45

Valores normalizados: -0.77, 1.98, -0.09, -0.77, -0.77, -0.09, 1.29, -0.77

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.8112781244591328


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.50|0.66|
|Ganancia|0.31|0.16|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.5|0.31|
|17.0|0.74|0.07|
|18.5|0.52|0.29|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.12|0.25|0.50|2.00|
|Edad < 16 and Habilidad = Baja → Altura < 153|0.00|0.25|0.00|0.00|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Media', 'Media', 'Baja', 'Baja', 'Alta', 'Media', 'Media']


Valores nuevos: [3, 2, 2, 1, 1, 3, 2, 2]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|153|3|No|
|2|19|156|2|Si|
|3|16|160|2|No|
|4|15|170|1|No|
|5|15|162|1|No|
|6|16|142|3|Si|
|7|18|157|2|No|
|8|15|125|2|No|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|13|83|1|
|2|17|45|1|
|3|18|4|2|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[12, 2, 100]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=699*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|12×15+2×153+100×3 =786|12×19+2×156+100×2 =740|12×16+2×160+100×2 =712|
|Salida|1 (786>=699)|1 (740>=699)|1 (712>=699)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
