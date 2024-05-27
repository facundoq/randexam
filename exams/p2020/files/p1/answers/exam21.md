---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|160|Media|No|
|2|15|208|Alta|No|
|3|18|188|Media|Si|
|4|15|171|Media|Si|
|5|15|145|Baja|Si|
|6|17|186|Baja|No|
|7|16|149|Media|No|
|8|15|139|Baja|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 2, 2, 1, 0, 2, 0, 0]

Intervalos: [[139.0,162.0), [162.0,185.0), [185.0,208.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 2, 2, 1, 0, 2, 0, 0]

Intervalos: [[139,160), [160,186), [186,208]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/3.00

Valores normalizados: 0.33, 0.00, 1.00, 0.00, 0.00, 0.67, 0.33, 0.00

Normalización mu/std con transformación (x-15.88)/1.05

Valores normalizados: 0.12, -0.83, 2.02, -0.83, -0.83, 1.07, 0.12, -0.83

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.954434002924965


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.76|0.84|
|Ganancia|0.20|0.11|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.91|0.05|
|16.5|0.94|0.02|
|17.5|0.76|0.2|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.00|0.12|0.00|0.00|
|Edad < 16 and Habilidad = Baja → Altura < 168|0.25|0.25|1.00|2.00|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Alta', 'Media', 'Media', 'Baja', 'Baja', 'Media', 'Baja']


Valores nuevos: [2, 3, 2, 2, 1, 1, 2, 1]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|160|2|No|
|2|15|208|3|No|
|3|18|188|2|Si|
|4|15|171|2|Si|
|5|15|145|1|Si|
|6|17|186|1|No|
|7|16|149|2|No|
|8|15|139|1|No|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|2|784|1|
|2|2308|402|2|
|3|794|4|2|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[12, 2, 113]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=724*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|12×16+2×160+113×2 =738|12×15+2×208+113×3 =935|12×18+2×188+113×2 =818|
|Salida|1 (738>=724)|1 (935>=724)|1 (818>=724)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
