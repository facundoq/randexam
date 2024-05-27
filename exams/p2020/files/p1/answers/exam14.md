---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|18|146|Alta|Si|
|2|17|208|Baja|No|
|3|16|161|Baja|No|
|4|16|155|Alta|Si|
|5|17|208|Media|No|
|6|17|199|Media|Si|
|7|15|207|Alta|No|
|8|18|188|Media|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 2, 0, 0, 2, 2, 2, 2]

Intervalos: [[146.0,166.67), [166.67,187.33), [187.33,208.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 2, 0, 0, 2, 1, 2, 1]

Intervalos: [[146,188), [188,207), [207,208]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/3.00

Valores normalizados: 1.00, 0.67, 0.33, 0.33, 0.67, 0.67, 0.00, 1.00

Normalización mu/std con transformación (x-16.75)/0.97

Valores normalizados: 1.29, 0.26, -0.77, -0.77, 0.26, 0.26, -1.81, 1.29

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.954434002924965


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.86|0.69|
|Ganancia|0.09|0.27|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.86|0.09|
|16.5|0.95|0.0|
|17.5|0.94|0.02|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.25|0.38|0.67|1.78|
|Edad < 17 and Habilidad = Baja → Altura < 184|0.12|0.12|1.00|2.67|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Baja', 'Baja', 'Alta', 'Media', 'Media', 'Alta', 'Media']


Valores nuevos: [3, 1, 1, 3, 2, 2, 3, 2]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|18|146|3|Si|
|2|17|208|1|No|
|3|16|161|1|No|
|4|16|155|3|Si|
|5|17|208|2|No|
|6|17|199|2|Si|
|7|15|207|3|No|
|8|18|188|2|No|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|1772|3846|1|
|2|401|1|2|
|3|729|2211|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[6, 1, 46]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=382*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|6×18+1×146+46×3 =392|6×17+1×208+46×1 =356|6×16+1×161+46×1 =303|
|Salida|1 (392>=382)|0 (356<382)|0 (303<382)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
