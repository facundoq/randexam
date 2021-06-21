---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|18|177|Alta|Si|
|2|18|148|Baja|No|
|3|16|175|Media|Si|
|4|18|196|Baja|No|
|5|15|156|Baja|Si|
|6|19|167|Media|Si|
|7|15|161|Media|No|
|8|17|206|Baja|Si|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 0, 1, 2, 0, 0, 0, 2]

Intervalos: [[148.0,167.33), [167.33,186.67), [186.67,206.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 0, 1, 2, 0, 1, 0, 2]

Intervalos: [[148,167), [167,177), [177,206]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.75, 0.75, 0.25, 0.75, 0.00, 1.00, 0.00, 0.50

Normalización mu/std con transformación (x-17.00)/1.41

Valores normalizados: 0.71, 0.71, -0.71, 0.71, -1.41, 1.41, -1.41, 0.00

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.954434002924965


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.86|0.84|
|Ganancia|0.09|0.11|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.94|0.02|
|16.5|0.95|0.0|
|17.5|0.91|0.05|
|18.5|0.86|0.09|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.12|0.12|1.00|1.60|
|Edad < 17 and Habilidad = Baja → Altura < 173|0.12|0.12|1.00|2.00|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Baja', 'Media', 'Baja', 'Baja', 'Media', 'Media', 'Baja']


Valores nuevos: [3, 1, 2, 1, 1, 2, 2, 1]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|18|177|3|Si|
|2|18|148|1|No|
|3|16|175|2|Si|
|4|18|196|1|No|
|5|15|156|1|Si|
|6|19|167|2|Si|
|7|15|161|2|No|
|8|17|206|1|Si|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|108|362|1|
|2|365|2305|1|
|3|65|445|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[6, 1, 62]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=376*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|6×18+1×177+62×3 =471|6×18+1×148+62×1 =318|6×16+1×175+62×2 =395|
|Salida|1 (471>=376)|0 (318<376)|1 (395>=376)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
