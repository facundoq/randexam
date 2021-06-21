---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|149|2|Alta|Deportivo|
|2|138|6|Media|Utilitario|
|3|169|9|Baja|Deportivo|
|4|179|10|Media|Deportivo|
|5|122|10|Alta|Deportivo|
|6|168|4|Baja|Deportivo|
|7|174|15|Media|Utilitario|
|8|155|3|Alta|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 1, 3, 3, 0, 3, 3, 2]

Intervalos: [[122.0,136.25), [136.25,150.5), [150.5,164.75), [164.75,179.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 0, 2, 3, 0, 2, 3, 1]

Intervalos: [[122,149), [149,168), [168,174), [174,179]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-2.00)/13.00

Valores normalizados: 0.00, 0.31, 0.54, 0.62, 0.62, 0.15, 1.00, 0.08

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.25|0.38|0.67|1.78|
|Clase = Utilitario → Antigüedad = Alta|0.12|0.38|0.33|0.89|
|Velocidad < 157 and Antigüedad = Alta → Cilindros < 7|0.25|0.38|0.67|1.33|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Baja|Pocos|Alta|Deportivo|
|Baja|Pocos|Media|Utilitario|
|Alta|Muchos|Baja|Deportivo|
|Alta|Muchos|Media|Deportivo|
|Baja|Muchos|Alta|Deportivo|
|Media|Pocos|Baja|Deportivo|
|Alta|Muchos|Media|Utilitario|
|Media|Pocos|Alta|Utilitario|


Mejor atributo: Antigüedad


|Reglas con Velocidad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|0.50|2|
|Velocidad = Baja → Clase = Deportivo|0.67|3|
|Velocidad = Alta → Clase = Deportivo|0.67|3|



|Reglas con Cilindros (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Deportivo|0.75|4|
|Cilindros = Pocos → Clase = Utilitario|0.50|4|



|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.67|3|
|Antigüedad = Baja → Clase = Deportivo|1.00|2|
|Antigüedad = Alta → Clase = Deportivo|0.67|3|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Media', 'Baja', 'Media', 'Alta', 'Baja', 'Media', 'Alta']


Valores nuevos: [3, 2, 1, 2, 3, 1, 2, 3]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|149|2|3|Deportivo|
|2|138|6|2|Utilitario|
|3|169|9|1|Deportivo|
|4|179|10|2|Deportivo|
|5|122|10|3|Deportivo|
|6|168|4|1|Deportivo|
|7|174|15|2|Utilitario|
|8|155|3|3|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|20|465|1|
|2|122|977|1|
|3|409|2|2|


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
