---
title: Minería de Datos usando Sistemas Inteligentes
author: Primer Parcial - 17 de Junio de 2020
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|18|205|Media|Si|
|2|17|178|Alta|No|
|3|18|189|Media|No|
|4|17|214|Alta|Si|
|5|19|207|Baja|No|
|6|16|150|Baja|No|
|7|19|189|Alta|Si|
|8|17|166|Baja|Si|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 1, 1, 2, 2, 0, 1, 0]

Intervalos: [[150.0,171.33), [171.33,192.67), [192.67,214.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 0, 1, 2, 2, 0, 1, 0]

Intervalos: [[150,189), [189,205), [205,214]]

### 2. Normalización de atributos (puntos: 1)
 Normalización min/max con transformación (x-16.00)/3.00

Valores normalizados: 0.67, 0.33, 0.67, 0.33, 1.00, 0.00, 1.00, 0.33

Normalización mu/std con transformación (x-17.62)/0.99

Valores normalizados: 0.38, -0.63, 0.38, -0.63, 1.39, -1.64, 1.39, -0.63

### 3. Ganancia de Información (puntos: 1)
 Entropía general: 1.0


|Atributo|Edad|Habilidad|
|----------|----------|----------|
|Entropía|0.86|0.94|
|Ganancia|0.14|0.06|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|16.5|0.86|0.14|
|17.5|1.0|0.0|
|18.5|1.0|0.0|


### 4. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad = Alta → Clase = Si|0.25|0.38|0.67|1.33|
|Edad < 18 and Habilidad = Baja → Altura < 187|0.25|0.25|1.00|2.67|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Alta', 'Media', 'Alta', 'Baja', 'Baja', 'Alta', 'Baja']


Valores nuevos: [2, 3, 2, 3, 1, 1, 3, 1]



|Fila|Edad|Altura|Habilidad|Clase|
|----------|----------|----------|----------|----------|
|1|18|205|2|Si|
|2|17|178|3|No|
|3|18|189|2|No|
|4|17|214|3|Si|
|5|19|207|1|No|
|6|16|150|1|No|
|7|19|189|3|Si|
|8|17|166|1|Si|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|258|4|2|
|2|125|843|1|
|3|2|324|1|


### 7. Perceptrón (puntos: 1)
 Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w=[12, 2, 100]* (para los atributos Edad, Altura, Habilidad, respectivamente) y *sesgo=786*, calcular la entrada neta y la salida final (0 o 1) de los 3 primeros ejemplos de la tabla de datos. 

 Nota: El cálculo de la entrada neta no incluye el sesgo o bias.


||Ejemplo 1|Ejemplo 2|Ejemplo 3|
|----------|----------|----------|----------|
|Neta|12×18+2×205+100×2 =826|12×17+2×178+100×3 =860|12×18+2×189+100×2 =794|
|Salida|1 (826>=786)|1 (860>=786)|1 (794>=786)|


### 8. Matriz de Correlación (puntos: 1)
 F,F,F,V

a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Falso,  la correlación es negativa

c) Falso, la correlación es débil (0.5<x<0.8)

d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.
