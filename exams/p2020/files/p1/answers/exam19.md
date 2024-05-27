---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|217|Baja|No|
|2|17|188|Alta|No|
|3|19|151|Alta|Si|
|4|19|192|Baja|Si|
|5|18|143|Baja|No|
|6|19|160|Alta|No|
|7|18|168|Media|Si|
|8|15|204|Alta|Si|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 1, 0, 1, 0, 0, 1, 2]

Intervalos: [[143.0,167.67), [167.67,192.33), [192.33,217.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 1, 0, 2, 0, 0, 1, 2]

Intervalos: [[143,168), [168,192), [192,217]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.25, 0.50, 1.00, 1.00, 0.75, 1.00, 0.75, 0.00

Normalización mu/std con transformación (x-17.62)/1.41

Valores normalizados: -1.15, -0.44, 0.98, 0.98, 0.27, 0.98, 0.27, -1.86

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 1.0


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.86|0.84|
|Ganancia|0.14|0.16|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.86|0.14|
|16.5|1.0|0.0|
|17.5|0.95|0.05|
|18.5|0.95|0.05|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.25|0.50|0.50|1.00|
|Edad < 18 and Habilidad = Baja → Altura < 178|0.00|0.12|0.00|0.00|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Alta', 'Alta', 'Baja', 'Baja', 'Alta', 'Media', 'Alta']


Valores nuevos: [1, 3, 3, 1, 1, 3, 2, 3]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|217|1|No|
|2|17|188|3|No|
|3|19|151|3|Si|
|4|19|192|1|Si|
|5|18|143|1|No|
|6|19|160|3|No|
|7|18|168|2|Si|
|8|15|204|3|Si|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|2402|179|2|
|2|404|261|2|
|3|297|2810|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[6, 1, 46]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=381*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|6×16+1×217+46×1 =359|6×17+1×188+46×3 =428|6×19+1×151+46×3 =403|
|Salida|0 (359<381)|1 (428>=381)|1 (403>=381)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
