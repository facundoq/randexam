---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|19|183|Baja|Si|
|2|16|178|Media|No|
|3|17|154|Alta|Si|
|4|15|180|Alta|No|
|5|16|156|Alta|No|
|6|18|170|Alta|No|
|7|17|157|Media|No|
|8|16|183|Alta|Si|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 2, 0, 2, 0, 1, 0, 2]

Intervalos: [[154.0,163.67), [163.67,173.33), [173.33,183.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 1, 0, 2, 0, 1, 0, 2]

Intervalos: [[154,170), [170,180), [180,183]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 1.00, 0.25, 0.50, 0.00, 0.25, 0.75, 0.50, 0.25

Normalización mu/std con transformación (x-16.75)/1.20

Valores normalizados: 1.88, -0.63, 0.21, -1.46, -0.63, 1.04, 0.21, -0.63

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.954434002924965


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.76|0.61|
|Ganancia|0.20|0.35|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.86|0.09|
|16.5|0.91|0.05|
|17.5|0.94|0.02|
|18.5|0.76|0.2|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.25|0.62|0.40|1.07|
|Edad < 17 and Habilidad = Baja → Altura < 170|0.00|0.00|1.00|inf|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Media', 'Alta', 'Alta', 'Alta', 'Alta', 'Media', 'Alta']


Valores nuevos: [1, 2, 3, 3, 3, 3, 2, 3]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|19|183|1|Si|
|2|16|178|2|No|
|3|17|154|3|Si|
|4|15|180|3|No|
|5|16|156|3|No|
|6|18|170|3|No|
|7|17|157|2|No|
|8|16|183|3|Si|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|178|5|2|
|2|65|26|2|
|3|261|842|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[6, 1, 40]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=370*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|6×19+1×183+40×1 =337|6×16+1×178+40×2 =354|6×17+1×154+40×3 =376|
|Salida|0 (337<370)|0 (354<370)|1 (376>=370)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
