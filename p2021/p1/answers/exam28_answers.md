---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|159|4|Media|Utilitario|
|2|143|15|Alta|Utilitario|
|3|171|13|Baja|Utilitario|
|4|151|11|Alta|Deportivo|
|5|174|15|Alta|Deportivo|
|6|157|15|Alta|Utilitario|
|7|173|7|Media|Deportivo|
|8|151|14|Media|Deportivo|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 0, 3, 1, 3, 1, 3, 1]

Intervalos: [[143.0,150.75), [150.75,158.5), [158.5,166.25), [166.25,174.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 0, 2, 1, 3, 1, 3, 1]

Intervalos: [[143,151), [151,159), [159,173), [173,174]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-4.00)/11.00

Valores normalizados: 0.00, 1.00, 0.82, 0.64, 1.00, 1.00, 0.27, 0.91

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.12|0.38|0.33|0.67|
|Clase = Deportivo → Antigüedad = Alta|0.25|0.50|0.50|1.00|
|Velocidad < 160 and Antigüedad = Alta → Cilindros < 12|0.12|0.38|0.33|0.89|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Media|Pocos|Media|Utilitario|
|Baja|Muchos|Alta|Utilitario|
|Alta|Pocos|Baja|Utilitario|
|Baja|Pocos|Alta|Deportivo|
|Alta|Muchos|Alta|Deportivo|
|Media|Muchos|Alta|Utilitario|
|Alta|Pocos|Media|Deportivo|
|Baja|Muchos|Media|Deportivo|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|1.00|2|
|Velocidad = Baja → Clase = Deportivo|0.67|3|
|Velocidad = Alta → Clase = Deportivo|0.67|3|



|Reglas con Cilindros (accuracy=0.5)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.50|4|
|Cilindros = Pocos → Clase = Utilitario|0.50|4|



|Reglas con Antigüedad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|0.67|3|
|Antigüedad = Baja → Clase = Utilitario|1.00|1|
|Antigüedad = Alta → Clase = Utilitario|0.50|4|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Alta', 'Baja', 'Alta', 'Alta', 'Alta', 'Media', 'Media']


Valores nuevos: [2, 3, 1, 3, 3, 3, 2, 2]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|159|4|2|Utilitario|
|2|143|15|3|Utilitario|
|3|171|13|1|Utilitario|
|4|151|11|3|Deportivo|
|5|174|15|3|Deportivo|
|6|157|15|3|Utilitario|
|7|173|7|2|Deportivo|
|8|151|14|2|Deportivo|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|146|266|1|
|2|72|784|1|
|3|400|8|2|


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
