---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|148|Media|No|
|2|15|191|Media|Si|
|3|19|161|Alta|No|
|4|15|194|Baja|No|
|5|15|174|Baja|Si|
|6|16|189|Alta|No|
|7|19|177|Media|No|
|8|19|184|Baja|No|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 2, 0, 2, 1, 2, 1, 2]

Intervalos: [[148.0,163.33), [163.33,178.67), [178.67,194.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 2, 0, 2, 0, 2, 1, 1]

Intervalos: [[148,177), [177,189), [189,194]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-15.00)/4.00

Valores normalizados: 0.00, 0.00, 1.00, 0.00, 0.00, 0.25, 1.00, 1.00

Normalización mu/std con transformación (x-16.62)/1.87

Valores normalizados: -0.87, -0.87, 1.27, -0.87, -0.87, -0.33, 1.27, 1.27

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 0.8112781244591328


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.50|0.69|
|Ganancia|0.31|0.12|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|15.5|0.5|0.31|
|17.5|0.61|0.2|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.00|0.25|0.00|0.00|
|Edad < 17 and Habilidad = Baja → Altura < 177|0.12|0.25|0.50|1.33|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Media', 'Alta', 'Baja', 'Baja', 'Alta', 'Media', 'Baja']


Valores nuevos: [2, 2, 3, 1, 1, 3, 2, 1]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|15|148|2|No|
|2|15|191|2|Si|
|3|19|161|3|No|
|4|15|194|1|No|
|5|15|174|1|Si|
|6|16|189|3|No|
|7|19|177|2|No|
|8|19|184|1|No|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|842|1865|1|
|2|197|16|2|
|3|276|901|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[12, 2, 106]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=752*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|12×15+2×148+106×2 =688|12×15+2×191+106×2 =774|12×19+2×161+106×3 =868|
|Salida|0 (688<752)|1 (774>=752)|1 (868>=752)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
