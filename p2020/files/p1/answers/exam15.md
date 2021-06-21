---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|18|152|Baja|No|
|2|18|208|Baja|No|
|3|17|164|Alta|Si|
|4|16|186|Alta|No|
|5|15|188|Baja|Si|
|6|16|166|Alta|Si|
|7|15|182|Media|Si|
|8|15|188|Media|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 2, 0, 1, 1, 0, 1, 1]

Intervalos: [[152.0,170.67), [170.67,189.33), [189.33,208.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 2, 0, 1, 2, 0, 1, 2]

Intervalos: [[152,182), [182,188), [188,208]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/3.00

Valores normalizados: 1.00, 1.00, 0.67, 0.33, 0.00, 0.33, 0.00, 0.00

Normalización mu/std con transformación (x-16.25)/1.20

Valores normalizados: 1.46, 1.46, 0.63, -0.21, -1.04, -0.21, -1.04, -1.04

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 1.0


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.69|0.94|
|Ganancia|0.31|0.06|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.95|0.05|
|16.5|0.95|0.05|
|17.5|0.69|0.31|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.25|0.38|0.67|1.33|
|Edad < 16 and Habilidad = Baja → Altura < 179|0.00|0.12|0.00|0.00|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Baja', 'Alta', 'Alta', 'Baja', 'Alta', 'Media', 'Media']


Valores nuevos: [1, 1, 3, 3, 1, 3, 2, 2]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|18|152|1|No|
|2|18|208|1|No|
|3|17|164|3|Si|
|4|16|186|3|No|
|5|15|188|1|Si|
|6|16|166|3|Si|
|7|15|182|2|Si|
|8|15|188|2|No|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|909|1298|1|
|2|685|402|2|
|3|332|577|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[12, 2, 100]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=753*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|12×18+2×152+100×1 =620|12×18+2×208+100×1 =732|12×17+2×164+100×3 =832|
|Salida|0 (620<753)|0 (732<753)|1 (832>=753)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
