---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|143|15|Alta|Deportivo|
|2|162|7|Media|Utilitario|
|3|141|15|Alta|Utilitario|
|4|179|4|Media|Utilitario|
|5|130|9|Baja|Utilitario|
|6|123|10|Baja|Utilitario|
|7|125|10|Baja|Utilitario|
|8|136|3|Media|Deportivo|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 2, 1, 3, 0, 0, 0, 0]

Intervalos: [[123.0,137.0), [137.0,151.0), [151.0,165.0), [165.0,179.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 3, 2, 3, 1, 0, 0, 1]

Intervalos: [[123,130), [130,141), [141,162), [162,179]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-3.00)/12.00

Valores normalizados: 1.00, 0.33, 1.00, 0.08, 0.50, 0.58, 0.58, 0.00

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Alta → Clase = Deportivo|0.12|0.25|0.50|2.00|
|Clase = Utilitario → Antigüedad = Media|0.25|0.75|0.33|0.89|
|Velocidad < 142 and Antigüedad = Alta → Cilindros < 9|0.00|0.12|0.00|0.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Alta|Muchos|Alta|Deportivo|
|Alta|Pocos|Media|Utilitario|
|Media|Muchos|Alta|Utilitario|
|Alta|Pocos|Media|Utilitario|
|Baja|Pocos|Baja|Utilitario|
|Baja|Muchos|Baja|Utilitario|
|Baja|Muchos|Baja|Utilitario|
|Media|Pocos|Media|Deportivo|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|0.50|2|
|Velocidad = Baja → Clase = Utilitario|1.00|3|
|Velocidad = Alta → Clase = Utilitario|0.67|3|



|Reglas con Cilindros (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.75|4|
|Cilindros = Pocos → Clase = Utilitario|0.75|4|



|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.67|3|
|Antigüedad = Baja → Clase = Utilitario|1.00|3|
|Antigüedad = Alta → Clase = Utilitario|0.50|2|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Media', 'Alta', 'Media', 'Baja', 'Baja', 'Baja', 'Media']


Valores nuevos: [3, 2, 3, 2, 1, 1, 1, 2]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|143|15|3|Deportivo|
|2|162|7|2|Utilitario|
|3|141|15|3|Utilitario|
|4|179|4|2|Utilitario|
|5|130|9|1|Utilitario|
|6|123|10|1|Utilitario|
|7|125|10|1|Utilitario|
|8|136|3|2|Deportivo|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|205|1|2|
|2|1029|425|2|
|3|157|5|2|


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
