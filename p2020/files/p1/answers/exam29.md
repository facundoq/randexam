---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|139|Baja|No|
|2|15|171|Alta|No|
|3|19|173|Alta|Si|
|4|18|174|Alta|No|
|5|15|158|Alta|No|
|6|16|165|Alta|No|
|7|17|141|Alta|Si|
|8|15|160|Media|Si|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 2, 2, 2, 1, 2, 0, 1]

Intervalos: [[139.0,150.67), [150.67,162.33), [162.33,174.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 2, 2, 2, 0, 1, 0, 1]

Intervalos: [[139,160), [160,171), [171,174]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.00, 0.00, 1.00, 0.75, 0.00, 0.25, 0.50, 0.00

Normalización mu/std con transformación (x-16.25)/1.48

Valores normalizados: -0.85, -0.85, 1.86, 1.18, -0.85, -0.17, 0.51, -0.85

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.954434002924965


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.76|0.69|
|Ganancia|0.20|0.27|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.91|0.05|
|16.5|0.8|0.16|
|17.5|0.94|0.02|
|18.5|0.76|0.2|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.25|0.75|0.33|0.89|
|Edad < 16 and Habilidad = Baja → Altura < 160|0.12|0.12|1.00|2.67|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Alta', 'Alta', 'Alta', 'Alta', 'Alta', 'Alta', 'Media']


Valores nuevos: [1, 3, 3, 3, 3, 3, 3, 2]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|139|1|No|
|2|15|171|3|No|
|3|19|173|3|Si|
|4|18|174|3|No|
|5|15|158|3|No|
|6|16|165|3|No|
|7|17|141|3|Si|
|8|15|160|2|Si|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|441|1161|1|
|2|125|9|2|
|3|189|5|2|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[6, 1, 38]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=357*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|6×15+1×139+38×1 =267|6×15+1×171+38×3 =375|6×19+1×173+38×3 =401|
|Salida|0 (267<357)|1 (375>=357)|1 (401>=357)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
