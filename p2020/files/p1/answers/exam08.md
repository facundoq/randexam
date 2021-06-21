---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|171|Baja|No|
|2|19|176|Media|Si|
|3|19|157|Media|Si|
|4|15|162|Media|No|
|5|19|156|Alta|No|
|6|17|162|Media|No|
|7|16|153|Alta|Si|
|8|18|135|Alta|Si|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 2, 1, 1, 1, 1, 1, 0]

Intervalos: [[135.0,148.67), [148.67,162.33), [162.33,176.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 2, 1, 2, 0, 2, 0, 0]

Intervalos: [[135,157), [157,162), [162,176]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.25, 1.00, 1.00, 0.00, 1.00, 0.50, 0.25, 0.75

Normalización mu/std con transformación (x-17.38)/1.49

Valores normalizados: -0.92, 1.09, 1.09, -1.59, 1.09, -0.25, -0.92, 0.42

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 1.0


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.81|0.84|
|Ganancia|0.19|0.16|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.86|0.14|
|16.5|0.95|0.05|
|17.5|0.81|0.19|
|18.5|0.95|0.05|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.25|0.38|0.67|1.33|
|Edad < 17 and Habilidad = Baja → Altura < 159|0.00|0.12|0.00|0.00|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Media', 'Media', 'Media', 'Alta', 'Media', 'Alta', 'Alta']


Valores nuevos: [1, 2, 2, 2, 3, 2, 3, 3]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|171|1|No|
|2|19|176|2|Si|
|3|19|157|2|Si|
|4|15|162|2|No|
|5|19|156|3|No|
|6|17|162|2|No|
|7|16|153|3|Si|
|8|18|135|3|Si|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|196|10|2|
|2|371|25|2|
|3|10|196|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[12, 2, 88]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=724*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|12×16+2×171+88×1 =622|12×19+2×176+88×2 =756|12×19+2×157+88×2 =718|
|Salida|0 (622<724)|1 (756>=724)|0 (718<724)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
