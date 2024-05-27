---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|169|14|Baja|Utilitario|
|2|145|5|Media|Deportivo|
|3|160|14|Baja|Deportivo|
|4|145|11|Alta|Deportivo|
|5|130|10|Media|Deportivo|
|6|154|3|Alta|Utilitario|
|7|157|11|Media|Utilitario|
|8|169|10|Alta|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [3, 1, 3, 1, 0, 2, 2, 3]

Intervalos: [[130.0,139.75), [139.75,149.5), [149.5,159.25), [159.25,169.0]]

Resultado de la discretización por frecuencia:

Valores: [3, 1, 2, 1, 0, 1, 2, 3]

Intervalos: [[130,145), [145,157), [157,169), [169,169]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-3.00)/11.00

Valores normalizados: 1.00, 0.18, 1.00, 0.73, 0.64, 0.00, 0.73, 0.64

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Alta → Clase = Deportivo|0.12|0.38|0.33|0.67|
|Clase = Utilitario → Antigüedad = Media|0.12|0.50|0.25|0.67|
|Velocidad < 154 and Antigüedad = Baja → Cilindros < 10|0.00|0.00|1.00|inf|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Alta|Muchos|Baja|Utilitario|
|Baja|Pocos|Media|Deportivo|
|Alta|Muchos|Baja|Deportivo|
|Baja|Muchos|Alta|Deportivo|
|Baja|Pocos|Media|Deportivo|
|Media|Pocos|Alta|Utilitario|
|Media|Muchos|Media|Utilitario|
|Alta|Pocos|Alta|Utilitario|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|1.00|2|
|Velocidad = Baja → Clase = Deportivo|1.00|3|
|Velocidad = Alta → Clase = Utilitario|0.67|3|



|Reglas con Cilindros (accuracy=0.5)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.50|4|
|Cilindros = Pocos → Clase = Utilitario|0.50|4|



|Reglas con Antigüedad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|0.67|3|
|Antigüedad = Baja → Clase = Utilitario|0.50|2|
|Antigüedad = Alta → Clase = Utilitario|0.67|3|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Media', 'Baja', 'Alta', 'Media', 'Alta', 'Media', 'Alta']


Valores nuevos: [1, 2, 1, 3, 2, 3, 2, 3]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|169|14|1|Utilitario|
|2|145|5|2|Deportivo|
|3|160|14|1|Deportivo|
|4|145|11|3|Deportivo|
|5|130|10|2|Deportivo|
|6|154|3|3|Utilitario|
|7|157|11|2|Utilitario|
|8|169|10|3|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|592|85|2|
|2|26|307|1|
|3|241|4|2|


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
