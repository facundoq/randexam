---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|151|14|Media|Deportivo|
|2|166|11|Alta|Deportivo|
|3|167|11|Baja|Utilitario|
|4|152|7|Media|Deportivo|
|5|144|9|Media|Deportivo|
|6|140|14|Baja|Utilitario|
|7|156|2|Alta|Deportivo|
|8|151|3|Media|Deportivo|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 3, 3, 1, 0, 0, 2, 1]

Intervalos: [[140.0,146.75), [146.75,153.5), [153.5,160.25), [160.25,167.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 3, 3, 2, 0, 0, 2, 1]

Intervalos: [[140,151), [151,152), [152,166), [166,167]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-2.00)/12.00

Valores normalizados: 1.00, 0.75, 0.75, 0.42, 0.58, 1.00, 0.00, 0.08

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.00|0.50|0.00|0.00|
|Clase = Utilitario → Antigüedad = Alta|0.00|0.25|0.00|0.00|
|Velocidad < 153 and Antigüedad = Baja → Cilindros < 9|0.00|0.12|0.00|0.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Media|Muchos|Media|Deportivo|
|Alta|Muchos|Alta|Deportivo|
|Alta|Muchos|Baja|Utilitario|
|Media|Pocos|Media|Deportivo|
|Baja|Pocos|Media|Deportivo|
|Baja|Muchos|Baja|Utilitario|
|Alta|Pocos|Alta|Deportivo|
|Media|Pocos|Media|Deportivo|


Mejor atributo: Antigüedad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Deportivo|1.00|3|
|Velocidad = Baja → Clase = Utilitario|0.50|2|
|Velocidad = Alta → Clase = Deportivo|0.67|3|



|Reglas con Cilindros (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.50|4|
|Cilindros = Pocos → Clase = Deportivo|1.00|4|



|Reglas con Antigüedad (accuracy=1.0)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|1.00|4|
|Antigüedad = Baja → Clase = Utilitario|1.00|2|
|Antigüedad = Alta → Clase = Deportivo|1.00|2|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Alta', 'Baja', 'Media', 'Media', 'Baja', 'Alta', 'Media']


Valores nuevos: [2, 3, 1, 2, 2, 1, 3, 2]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|151|14|2|Deportivo|
|2|166|11|3|Deportivo|
|3|167|11|1|Utilitario|
|4|152|7|2|Deportivo|
|5|144|9|2|Deportivo|
|6|140|14|1|Utilitario|
|7|156|2|3|Deportivo|
|8|151|3|2|Deportivo|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|26|25|2|
|2|233|110|2|
|3|260|131|2|


### 7. Conceptos de Agrupamientos (puntos: 1)
 a) Falso, ambos consideran esas distancias.

b) Verdadero, ya que calcula distancias entre los centroides y los ejemplos de cada cluster.

c) Falso, como el indice se define como (b(i)-a(i))/max(b(i),a(i)), donde b es la distancia inter cluster promedio y a es la intracluster, entonces si vale 1 quiere decir que la distancia intercluster es grande y la intracluster es baja

d) Falso, como el Silhouette depende también de la separación entre clusters, puede que decremente o que aumente si se tienen muchos clusters pequeños pero cercanos entre sí. 

### 8. Matriz de Correlación (puntos: 1)
 a) Falso, si bien la correlación es casi 0, pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2

b) Verdadero,  la correlación es positiva y fuerte

c) Falso, no hay correlación (|x|<0.5)

d) Verdadero, la correlación es débil y negativa ya que 0.5 < |x| < 0.8.

e) Falso, justo la mitad está correlacionada y la mitad no.

### 9. Conceptos de Minería de Datos (puntos: 1)
 a) VERDADERO. Vimos en clase como hacerlo

b)  Verdadero. Si sólo tiene 1 valor, no separa los ejemplos por lo
que su entropía coincide con la entroía de conjunto original. Luego la
ganancia de información será la resta de 2 valores iguales.

c) FALSO. En realidad debe ser CUALITATIVO, es decir, ordinal o nominal.

d) FALSO. La cantidad de valores del atributo será finita por lo que se ordenan los valores distintos (no importa que tenga decimales) y se calcula como vimos en clase.

e) VERDADERO. Esto ocurre cuando hay valores repetidos.

f) VERDADERO. Si dos de sus valores ocurren con la misma frecuencia y se trata del valor con más apariciones, ambos serán valores de MODA.

g) Verdadero. Las reglas de asociación son un modelo descriptivo.
