---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|142|6|Media|Utilitario|
|2|145|11|Baja|Deportivo|
|3|149|3|Baja|Deportivo|
|4|129|14|Baja|Utilitario|
|5|137|7|Media|Utilitario|
|6|160|5|Media|Deportivo|
|7|159|15|Alta|Deportivo|
|8|143|14|Baja|Deportivo|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 2, 2, 0, 1, 3, 3, 1]

Intervalos: [[129.0,136.75), [136.75,144.5), [144.5,152.25), [152.25,160.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 2, 2, 0, 0, 3, 3, 1]

Intervalos: [[129,142), [142,145), [145,159), [159,160]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-3.00)/12.00

Valores normalizados: 0.25, 0.67, 0.00, 0.92, 0.33, 0.17, 1.00, 0.92

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Baja → Clase = Utilitario|0.12|0.50|0.25|0.67|
|Clase = Utilitario → Antigüedad = Alta|0.00|0.38|0.00|0.00|
|Velocidad < 146 and Antigüedad = Baja → Cilindros < 9|0.00|0.38|0.00|0.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Baja|Pocos|Media|Utilitario|
|Media|Muchos|Baja|Deportivo|
|Alta|Pocos|Baja|Deportivo|
|Baja|Muchos|Baja|Utilitario|
|Baja|Pocos|Media|Utilitario|
|Alta|Pocos|Media|Deportivo|
|Alta|Muchos|Alta|Deportivo|
|Media|Muchos|Baja|Deportivo|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=1.0)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Deportivo|1.00|2|
|Velocidad = Baja → Clase = Utilitario|1.00|3|
|Velocidad = Alta → Clase = Deportivo|1.00|3|



|Reglas con Cilindros (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Deportivo|0.75|4|
|Cilindros = Pocos → Clase = Utilitario|0.50|4|



|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.67|3|
|Antigüedad = Baja → Clase = Deportivo|0.75|4|
|Antigüedad = Alta → Clase = Deportivo|1.00|1|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Baja', 'Baja', 'Baja', 'Media', 'Media', 'Alta', 'Baja']


Valores nuevos: [2, 1, 1, 1, 2, 2, 3, 1]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|142|6|2|Utilitario|
|2|145|11|1|Deportivo|
|3|149|3|1|Deportivo|
|4|129|14|1|Utilitario|
|5|137|7|2|Utilitario|
|6|160|5|2|Deportivo|
|7|159|15|3|Deportivo|
|8|143|14|1|Deportivo|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|2|114|1|
|2|25|25|1|
|3|65|121|1|


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
