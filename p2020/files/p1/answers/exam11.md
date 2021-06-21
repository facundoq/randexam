---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|146|Alta|Si|
|2|16|188|Baja|No|
|3|18|179|Media|Si|
|4|16|139|Baja|Si|
|5|19|199|Alta|Si|
|6|16|207|Baja|Si|
|7|17|193|Media|Si|
|8|15|166|Media|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 2, 1, 0, 2, 2, 2, 1]

Intervalos: [[139.0,161.67), [161.67,184.33), [184.33,207.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 1, 1, 0, 2, 2, 2, 0]

Intervalos: [[139,179), [179,193), [193,207]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.25, 0.25, 0.75, 0.25, 1.00, 0.25, 0.50, 0.00

Normalización mu/std con transformación (x-16.62)/1.22

Valores normalizados: -0.51, -0.51, 1.13, -0.51, 1.95, -0.51, 0.31, -1.33

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.8112781244591328


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.52|0.69|
|Ganancia|0.29|0.12|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.52|0.29|
|16.5|0.61|0.2|
|17.5|0.69|0.12|
|18.5|0.76|0.06|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.25|0.25|1.00|1.33|
|Edad < 17 and Habilidad = Baja → Altura < 177|0.12|0.38|0.33|0.89|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Baja', 'Media', 'Baja', 'Alta', 'Baja', 'Media', 'Media']


Valores nuevos: [3, 1, 2, 1, 3, 1, 2, 2]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|16|146|3|Si|
|2|16|188|1|No|
|3|18|179|2|Si|
|4|16|139|1|Si|
|5|19|199|3|Si|
|6|16|207|1|Si|
|7|17|193|2|Si|
|8|15|166|2|No|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|1093|2811|1|
|2|81|123|1|
|3|5|401|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[6, 1, 53]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=376*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|6×16+1×146+53×3 =401|6×16+1×188+53×1 =337|6×18+1×179+53×2 =393|
|Salida|1 (401>=376)|0 (337<376)|1 (393>=376)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
