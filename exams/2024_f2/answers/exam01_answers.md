---
title: Minería de Datos usando Sistemas Inteligentes - Tema 2 (Respuestas)
author:  Fecha 2 - 28 de Junio de 2024 

date: 
geometry: margin=1.6cm
---



### 1. Discretización de atributos (Puntos: 1)
 Resultado de la discretización por rango:

Valores: ['Negativo', 'Leve', 'Negativo', 'Leve', 'Negativo', 'Leve', 'Leve', 'Alto']

Intervalos: [[17.0,42.0), [42.0,67.0), [67.0,92.0]]

Resultado de la discretización por frecuencia:

Valores: ['Negativo', 'Alto', 'Negativo', 'Alto', 'Negativo', 'Leve', 'Leve', 'Alto']

Intervalos: [[17,43), [43,60), [60,92]]

### 2. Modelo OneR (Puntos: 1)
 
|Tamaño|Anticuerpos|Síntomas|Clase|
|----------|----------|----------|----------|
|Bajo|Negativo|Leves|Benigno|
|Alto|Alto|Leves|Benigno|
|Alto|Negativo|Ninguno|Benigno|
|Bajo|Alto|Graves|Maligno|
|Alto|Negativo|Ninguno|Maligno|
|Alto|Leve|Ninguno|Benigno|
|Alto|Leve|Ninguno|Benigno|
|Alto|Alto|Leves|Maligno|


Mejor atributo: Anticuerpos


|Reglas con Tamaño (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Tamaño = Alto → Clase = Benigno|0.67|6|
|Tamaño = Bajo → Clase = Benigno|0.50|2|



|Reglas con Anticuerpos (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Anticuerpos = Negativo → Clase = Benigno|0.67|3|
|Anticuerpos = Leve → Clase = Benigno|1.00|2|
|Anticuerpos = Alto → Clase = Maligno|0.67|3|



|Reglas con Síntomas (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Síntomas = Ninguno → Clase = Benigno|0.75|4|
|Síntomas = Leves → Clase = Benigno|0.67|3|
|Síntomas = Graves → Clase = Maligno|1.00|1|


### 3. Métricas de Reglas (Puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Síntomas = Graves → Clase = Maligno|0.125|0.125|1.000|2.667|
|Clase = Benigno → Síntomas = Ninguno|0.375|0.625|0.600|1.200|
|Tamaño < 2 and Síntomas = Leves → Anticuerpos < 47|0.125|0.125|1.000|1.600|


### 4. Agrupamiento de datos - Cálculo de centroides (Puntos: 1)
 
| |Tamaño|Anticuerpos|Síntomas|Cluster Asignado|
|----------|----------|----------|----------|
|1|2.0|67.5|1.5|
|2|2.5|31.0|1.0|


### 5. Conceptos de Minería de Datos (Puntos: 2)
 a. No es posible calcular la Tasa de Ganancia (Gain Ratio) de un atributo numérico continuo (con decimales).
 RESPUESTA:
FALSO. La cantidad de valores del atributo será finita por lo que se ordenan los valores distintos (no importa que tenga decimales) y se calcula como vimos en clase.

b. Se tiene un problema de clasificación de 100 ejemplos con 3 columnas, una es la de la clase con 4 valores distintos, otra es nominal con 5 valores,
               y la otra es de un atributo numérico con 10 valores distintos. 
               Si se entrena un modelo de Naive Bayes ¿cuántas distribuciones gaussianas se deberán estimar?
 RESPUESTA:
Se estima una gaussiana para cada clase, o sea, 4 gaussianas.

c. ¿Cuál de las normalizaciones vistas es más sensible a los valores anómalos/extremos?
 RESPUESTA:
La lineal, ya que si hay un valor extremo afecta al máximo/mínimo directamente.

d. Dada una regla, (A=Si,B=No) → C=Si, con soporte 0.3, ¿Puedo inferir el soporte de la regla (A=Si) → (B=No, C=Si) sin los datos?
 RESPUESTA:
No se puede; se podría inferir la de (A=Si,B=No) ← C=Si ya que es la misma, pero para la del enunciado se requieren los datos.  

### 6. Ganancia de Información (Puntos: 2)
 Entropías calculadas con logaritmo con base 2

Entropía general: 0.954434002924965


|Atributo|Tamaño|Síntomas|
|----------|----------|----------|
|Entropía|0.61|0.75|
|Ganancia|0.35|0.20|



|Tamaño: Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|1.5|0.94|0.02|
|2.5|0.61|0.35|
|3.5|0.86|0.09|


### 7. Perceptrón (Puntos: 1.5)
 b) Asumiendo que Clase=Benigno está codificado con un 0, y Clase=Maligno con un 1, ¿cómo clasificaría el modelo a un ejemplo donde Tamaño vale 2, Anticuerpos vale 60 y Síntomas vale 1?

La salida neta es 22×2+1×60+31×1 =135, y por ende la salida es 0 (135<147), con clase Benigno

a) Asumiendo que Clase=Benigno está codificado con un 0, y Clase=Maligno con un 1, ¿cuál es el valor máximo del atributo Tamaño  para que un ejemplo con Anticuerpos=60 y Síntomas=2 pertenezca a la Clase=Maligno?

Recordamos que w=22, 1, 31 y b=147

Dados esos valores, y asumiendo que $a_0$, $a_1$ y $a_2$ son los valores para los atributos Tamaño, Anticuerpos, Síntomas, para que el modelo esté entre generar 0 o 1 debe cumplirse:

$a_0 . w0 + a_1 . w_1 + a_2 . w_2 = b$

$a_0 . w0 = b - a_1 . w_1 - a_2 . w_2$

$a_0  = (b - a_1 . w_1 - a_2 . w_2)/w_0$

$a_0  = (147 - 60 . 1 - 2 31)/22$

$a_0 = 1.1363636363636365$

Como buscamos que esté en clase Maligno, y el signo de $w_0$ es positivo, necesitamos que $a_0$ tenga como valor máximo 1.1363636363636365.
