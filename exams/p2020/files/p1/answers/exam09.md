---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|173|Alta|No|
|2|16|161|Baja|No|
|3|17|137|Alta|No|
|4|17|179|Alta|Si|
|5|17|151|Media|No|
|6|15|171|Baja|Si|
|7|17|184|Baja|Si|
|8|16|172|Alta|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 1, 0, 2, 0, 2, 2, 2]

Intervalos: [[137.0,152.67), [152.67,168.33), [168.33,184.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 0, 0, 2, 0, 1, 2, 1]

Intervalos: [[137,171), [171,173), [173,184]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/2.00

Valores normalizados: 0.00, 0.50, 1.00, 1.00, 1.00, 0.00, 1.00, 0.50

Normalización mu/std con transformación (x-16.25)/0.83

Valores normalizados: -1.51, -0.30, 0.90, 0.90, 0.90, -1.51, 0.90, -0.30

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.954434002924965


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.91|0.75|
|Ganancia|0.05|0.20|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.94|0.02|
|16.5|0.91|0.05|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.12|0.50|0.25|0.67|
|Edad < 16 and Habilidad = Baja → Altura < 166|0.00|0.12|0.00|0.00|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Baja', 'Alta', 'Alta', 'Media', 'Baja', 'Baja', 'Alta']


Valores nuevos: [3, 1, 3, 3, 2, 1, 1, 3]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|173|3|No|
|2|16|161|1|No|
|3|17|137|3|No|
|4|17|179|3|Si|
|5|17|151|2|No|
|6|15|171|1|Si|
|7|17|184|1|Si|
|8|16|172|3|No|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|9|41|1|
|2|100|326|1|
|3|1161|1765|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[12, 2, 93]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=724*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|12×15+2×173+93×3 =805|12×16+2×161+93×1 =607|12×17+2×137+93×3 =757|
|Salida|1 (805>=724)|0 (607<724)|1 (757>=724)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
