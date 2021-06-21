---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|169|Baja|No|
|2|15|146|Media|No|
|3|17|180|Baja|Si|
|4|16|166|Media|No|
|5|18|185|Media|No|
|6|19|186|Alta|No|
|7|16|213|Alta|Si|
|8|15|196|Alta|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 0, 1, 0, 1, 1, 2, 2]

Intervalos: [[146.0,168.33), [168.33,190.67), [190.67,213.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 0, 1, 0, 1, 2, 2, 2]

Intervalos: [[146,180), [180,186), [186,213]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.25, 0.00, 0.50, 0.25, 0.75, 1.00, 0.25, 0.00

Normalización mu/std con transformación (x-16.50)/1.32

Valores normalizados: -0.38, -1.13, 0.38, -0.38, 1.13, 1.89, -0.38, -1.13

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.8112781244591328


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.69|0.59|
|Ganancia|0.12|0.22|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.69|0.12|
|16.5|0.8|0.02|
|17.5|0.69|0.12|
|18.5|0.76|0.06|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.12|0.38|0.33|1.33|
|Edad < 16 and Habilidad = Baja → Altura < 180|0.00|0.00|1.00|inf|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Media', 'Baja', 'Media', 'Media', 'Alta', 'Alta', 'Alta']


Valores nuevos: [1, 2, 1, 2, 2, 3, 3, 3]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|169|1|No|
|2|15|146|2|No|
|3|17|180|1|Si|
|4|16|166|2|No|
|5|18|185|2|No|
|6|19|186|3|No|
|7|16|213|3|Si|
|8|15|196|3|No|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|121|731|1|
|2|1158|2504|1|
|3|1|257|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[6, 1, 46]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=376*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|6×16+1×169+46×1 =311|6×15+1×146+46×2 =328|6×17+1×180+46×1 =328|
|Salida|0 (311<376)|0 (328<376)|0 (328<376)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
