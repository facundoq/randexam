---
title: Minería de Datos usando Sistemas Inteligentes - Tema 2 (Respuestas)
author:  Primera Fecha - 9 de Junio de 2023 - Promoción

date: 
geometry: margin=1.6cm
---



### 1. Discretización de atributos (Puntos: 1)
 Resultado de la discretización por rango:

Valores: ['Bajo', 'Alto', 'Bajo', 'Alto', 'Bajo', 'Bajo', 'Alto', 'Bajo']

Intervalos: [[24.0,46.5), [46.5,69.0]]

Resultado de la discretización por frecuencia:

Valores: ['Alto', 'Alto', 'Bajo', 'Alto', 'Bajo', 'Bajo', 'Alto', 'Bajo']

Intervalos: [[24,44), [44,69]]

### 2. Modelo OneR (Puntos: 1)
 
|Visión |Dolor|Diabetes|Clase|
|----------|----------|----------|----------|
|Medio|Leve|Tipo 1|Normal|
|Alto|Grave|Tipo 1|Retinopatía|
|Bajo|Leve|Gestacional|Normal|
|Alto|Leve|Gestacional|Normal|
|Bajo|Grave|Gestacional|Retinopatía|
|Medio|Grave|Tipo 2|Retinopatía|
|Alto|Grave|Tipo 2|Normal|
|Bajo|Leve|Tipo 2|Retinopatía|


Mejor atributo: Dolor


|Reglas con Visión  (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Visión  = Alto → Clase = Normal|0.67|3|
|Visión  = Bajo → Clase = Retinopatía|0.67|3|
|Visión  = Medio → Clase = Normal|0.50|2|



|Reglas con Dolor (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Dolor = Grave → Clase = Retinopatía|0.75|4|
|Dolor = Leve → Clase = Normal|0.75|4|



|Reglas con Diabetes (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Diabetes = Gestacional → Clase = Normal|0.67|3|
|Diabetes = Tipo 1 → Clase = Normal|0.50|2|
|Diabetes = Tipo 2 → Clase = Retinopatía|0.67|3|


### 3. Métricas de Reglas (Puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Diabetes = Tipo 1 → Clase = Retinopatía|0.125|0.250|0.500|1.000|
|Clase = Retinopatía → Diabetes = Tipo 1|0.125|0.500|0.250|1.000|
|Visión  < 43 and Diabetes = Tipo 2 → Dolor < 5|0.125|0.250|0.500|1.333|


### 4. Agrupamiento de datos - Cálculo de asignaciones (Puntos: 1)
 
| |d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|97|89|2|
|2|197|9|2|
|3|121|641|1|


### 5. Agrupamiento de datos - Cálculo de centroides (Puntos: 1)
 
| |Visión |Dolor|Diabetes|Cluster Asignado|
|----------|----------|----------|----------|
|1|42.0|8.0|2.5|
|2|37.0|5.0|2.0|


### 6. Matriz de Correlación (Puntos: 1)
 a) Falso, si bien la correlación es casi 0, pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, de forma cuadrática

b) Verdadero,  la correlación es positiva y fuerte

c) Falso, la correlación es positiva pero débil (|x|<0.8)

d) Verdadero, la correlación es débil y negativa ya que 0.5 < |x| < 0.8.

e) Falso, es posible que tener alto riesgo cardiovascular y fumar estén correlacionados de forma intensa, y también tener Cáncer y fumar, pero no tener riesgo cardiovascular y tener Cáncer.

### 7. Conceptos de Minería de Datos (Puntos: 2)
 a) VERDADERO. Vimos en clase como hacerlo

b) El mismo

c) Verdadero. Las reglas de asociación son un modelo descriptivo.

d) FALSO. En realidad debe ser CUALITATIVO, es decir, ordinal o nominal.

e) Verdadero

f) Falso, como el indice se define como (b(i)-a(i))/max(b(i),a(i)), donde b es la distancia inter cluster promedio y a es la intracluster, entonces si vale 1 quiere decir que la distancia intercluster es grande y la intracluster es baja

g) 6, A->(B,C) B->(A,C) C->(A,B), idem con 2 items en el antecedente

h) VERDADERO. Esto ocurre cuando hay valores repetidos.

### 8. Ganancia de Información (Puntos: 2)
 Entropías calculadas con logaritmo con base 2

Entropía general: 0.3010299956639812


|Atributo|Diabetes|Dolor|
|----------|----------|----------|
|Entropía|0.24|0.28|
|Ganancia|0.06|0.02|



|Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|3.0|0.29|0.01|
|5.5|0.24|0.06|
|6.5|0.29|0.01|
|8.0|0.3|0.0|

