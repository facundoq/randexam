---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|19|152|Media|No|
|2|18|130|Media|No|
|3|15|163|Media|Si|
|4|18|173|Alta|No|
|5|16|194|Baja|Si|
|6|17|194|Baja|Si|
|7|17|162|Baja|No|
|8|18|163|Baja|Si|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 0, 1, 2, 2, 2, 1, 1]

Intervalos: [[130.0,151.33), [151.33,172.67), [172.67,194.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 0, 1, 2, 2, 2, 0, 1]

Intervalos: [[130,163), [163,173), [173,194]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 1.00, 0.75, 0.00, 0.75, 0.25, 0.50, 0.50, 0.75

Normalización mu/std con transformación (x-17.25)/1.20

Valores normalizados: 1.46, 0.63, -1.88, 0.63, -1.04, -0.21, -0.21, 0.63

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 1.0


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.69|0.75|
|Ganancia|0.31|0.25|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.86|0.14|
|16.5|0.69|0.31|
|17.5|0.81|0.19|
|18.5|0.86|0.14|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.00|0.12|0.00|0.00|
|Edad < 17 and Habilidad = Baja → Altura < 166|0.00|0.12|0.00|0.00|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Media', 'Media', 'Alta', 'Baja', 'Baja', 'Baja', 'Baja']


Valores nuevos: [2, 2, 2, 3, 1, 1, 1, 1]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|19|152|2|No|
|2|18|130|2|No|
|3|15|163|2|Si|
|4|18|173|3|No|
|5|16|194|1|Si|
|6|17|194|1|Si|
|7|17|162|1|No|
|8|18|163|1|Si|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|126|1765|1|
|2|1091|4096|1|
|3|5|970|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[6, 1, 62]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=370*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|6×19+1×152+62×2 =390|6×18+1×130+62×2 =362|6×15+1×163+62×2 =377|
|Salida|1 (390>=370)|0 (362<370)|1 (377>=370)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
