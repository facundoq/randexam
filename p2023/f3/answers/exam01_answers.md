---
title: Minería de Datos usando Sistemas Inteligentes - Tema 2 (Respuestas)
author:  Fecha 3 - 7 de Julio de 2023 

date: 
geometry: margin=1.6cm
---



### 1. Normalización de atributos (Puntos: 1)
 Normalización rango con transformación (x-8.00)/45.00

Valores normalizados: 0.73, 0.91, 0.27, 1.00, 0.51, 0.00, 0.42, 0.96

Normalización mu/std con transformación (x-35.00)/15.19

Valores normalizados: 0.39, 0.92, -0.99, 1.18, -0.26, -1.78, -0.53, 1.05

### 2. Discretización de atributos (Puntos: 1)
 Resultado de la discretización por rango:

Valores: ['Robusto', 'Robusto', 'Débil', 'Robusto', 'Normal', 'Débil', 'Normal', 'Robusto']

Intervalos: [[8.0,23.0), [23.0,38.0), [38.0,53.0]]

Resultado de la discretización por frecuencia:

Valores: ['Normal', 'Robusto', 'Débil', 'Robusto', 'Normal', 'Débil', 'Débil', 'Robusto']

Intervalos: [[8,31), [31,49), [49,53]]

### 3. Modelo OneR (Puntos: 1)
 
|Vida|Fuerza|Habilidad Especial|Clase|
|----------|----------|----------|----------|
|Media|Leve|Rapidez|Mítico|
|Alta|Grave|Rapidez|Mítico|
|Baja|Leve|Salto|Mítico|
|Alta|Grave|Defensa|Normal|
|Media|Leve|Salto|Normal|
|Baja|Grave|Salto|Mítico|
|Baja|Grave|Salto|Mítico|
|Alta|Grave|Rapidez|Mítico|


Mejor atributo: Habilidad Especial


|Reglas con Vida (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Vida = Baja → Clase = Mítico|1.00|3|
|Vida = Media → Clase = Normal|0.50|2|
|Vida = Alta → Clase = Mítico|0.67|3|



|Reglas con Fuerza (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Fuerza = Leve → Clase = Mítico|0.67|3|
|Fuerza = Grave → Clase = Mítico|0.80|5|



|Reglas con Habilidad Especial (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Habilidad Especial = Defensa → Clase = Normal|1.00|1|
|Habilidad Especial = Rapidez → Clase = Mítico|1.00|3|
|Habilidad Especial = Salto → Clase = Mítico|0.75|4|


### 4. Cuartiles (Puntos: 1)
 Valores ordenados de  Vida:

[8.0, 20.0, 27.0, 31.0, 41.0, 49.0, 51.0, 53.0]

Índices de los cuartiles:

2.25, 4.5, 6.75

Cuartiles:

q1=21.75, q2=36.0, q3=50.5

### 5. Métricas de Reglas (Puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Habilidad Especial = Salto → Clase = Normal|0.125|0.500|0.250|1.000|
|Clase = Normal → Habilidad Especial = Salto|0.125|0.250|0.500|1.000|
|Vida < 35 and Habilidad Especial = Rapidez → Fuerza < 4|0.000|0.000|1.000|inf|


### 6. Agrupamiento de datos - Cálculo de asignaciones (Puntos: 1.5)
 
| |d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|198|74|2|
|2|489|1|2|
|3|58|870|1|


### 7. Conceptos de Minería de Datos (Puntos: 2)
 a)  Verdadero. Si sólo tiene 1 valor, no separa los ejemplos por lo
que su entropía coincide con la entroía de conjunto original. Luego la
ganancia de información será la resta de 2 valores iguales.

b) VERDADERO. Si dos de sus valores ocurren con la misma frecuencia y se trata del valor con más apariciones, ambos serán valores de MODA.

c) Los nodos intermedios corresponden a atributos, las aristas a valores de esos atributos, y los nodos hoja a decisiones o predicciones de la clase

d) No se puede; se podría inferir la de (A=Si,B=No) ← C=Si ya que es la misma, pero para la del enunciado se requieren los datos.  

e) Se estima una gaussiana para cada clase y atributo numérico, o sea, 3x1 = 3 gaussianas.

f) V

g) Recopilación de datos, preprocesamiento, extracción de características, modelado, evaluación, interpretación, despliegue. La más costosa suele ser la recopilación de datos.

h) 

### 8. Perceptrón (Puntos: 1.5)
 a) Asumiendo que Clase=Normal está codificado con un 0, y Clase=Mítico con un 1, ¿cuál es el valor máximo del atributo Vida  para que un ejemplo con Fuerza=7 y Habilidad Especial=1 pertenezca a la Clase=Mítico?

Recordamos que w=2, 14, 41 y b=199

Dados esos valores, y asumiendo que $a_0$, $a_1$ y $a_2$ son los valores para los atributos Vida, Fuerza, Habilidad Especial, para que el modelo esté entre generar 0 o 1 debe cumplirse:

$a_0 . w0 + a_1 . w_1 + a_2 . w_2 = b$

$a_0 . w0 = b - a_1 . w_1 - a_2 . w_2$

$a_0  = (b - a_1 . w_1 - a_2 . w_2)/w_0$

$a_0  = (199 - 7 . 14 - 1 41)/2$

$a_0 = 30.0$

Como buscamos que esté en clase Mítico, y el signo de $w_0$ es positivo, necesitamos que $a_0$ tenga como valor máximo 30.0.

b) Asumiendo que Clase=Normal está codificado con un 0, y Clase=Mítico con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Vida vale 51, Fuerza vale 1 y Habilidad Especial vale 2?

La salida neta es 2×51+14×1+41×2 =198, y por ende la salida es 0 (198<199), con clase Normal
