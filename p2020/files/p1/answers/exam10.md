---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|19|192|Media|Si|
|2|18|145|Alta|No|
|3|15|178|Baja|No|
|4|15|156|Media|Si|
|5|18|152|Alta|No|
|6|19|158|Alta|Si|
|7|15|163|Media|No|
|8|17|171|Media|Si|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 0, 2, 0, 0, 0, 1, 1]

Intervalos: [[145.0,160.67), [160.67,176.33), [176.33,192.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 0, 2, 0, 0, 1, 1, 2]

Intervalos: [[145,158), [158,171), [171,192]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 1.00, 0.75, 0.00, 0.00, 0.75, 1.00, 0.00, 0.50

Normalización mu/std con transformación (x-17.00)/1.66

Valores normalizados: 1.21, 0.60, -1.21, -1.21, 0.60, 1.21, -1.21, 0.00

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 1.0


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.69|0.75|
|Ganancia|0.31|0.25|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|16.0|0.95|0.05|
|17.5|1.0|0.0|
|18.5|0.69|0.31|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.12|0.38|0.33|0.67|
|Edad < 17 and Habilidad = Baja → Altura < 164|0.00|0.12|0.00|0.00|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Alta', 'Baja', 'Media', 'Alta', 'Alta', 'Media', 'Media']


Valores nuevos: [2, 3, 1, 2, 3, 3, 2, 2]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|19|192|2|Si|
|2|18|145|3|No|
|3|15|178|1|No|
|4|15|156|2|Si|
|5|18|152|3|No|
|6|19|158|3|Si|
|7|15|163|2|No|
|8|17|171|2|Si|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|1173|197|2|
|2|182|1090|1|
|3|400|10|2|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[12, 2, 88]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=730*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|12×19+2×192+88×2 =788|12×18+2×145+88×3 =770|12×15+2×178+88×1 =624|
|Salida|1 (788>=730)|1 (770>=730)|0 (624<730)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
