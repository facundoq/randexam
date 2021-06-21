---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|157|9|Alta|Utilitario|
|2|152|5|Alta|Utilitario|
|3|151|7|Alta|Utilitario|
|4|159|12|Baja|Deportivo|
|5|153|3|Alta|Utilitario|
|6|160|4|Alta|Deportivo|
|7|145|6|Media|Utilitario|
|8|113|15|Alta|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [3, 3, 3, 3, 3, 3, 2, 0]

Intervalos: [[113.0,124.75), [124.75,136.5), [136.5,148.25), [148.25,160.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 1, 1, 3, 2, 3, 0, 0]

Intervalos: [[113,151), [151,153), [153,159), [159,160]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-3.00)/12.00

Valores normalizados: 0.50, 0.17, 0.33, 0.75, 0.00, 0.08, 0.25, 1.00

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|0.00|0.12|0.00|0.00|
|Clase = Utilitario → Antigüedad = Media|0.12|0.75|0.17|1.33|
|Velocidad < 149 and Antigüedad = Alta → Cilindros < 8|0.00|0.12|0.00|0.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Alta|Muchos|Alta|Utilitario|
|Media|Pocos|Alta|Utilitario|
|Baja|Muchos|Alta|Utilitario|
|Alta|Muchos|Baja|Deportivo|
|Media|Pocos|Alta|Utilitario|
|Alta|Pocos|Alta|Deportivo|
|Baja|Pocos|Media|Utilitario|
|Baja|Muchos|Alta|Utilitario|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|1.00|2|
|Velocidad = Baja → Clase = Utilitario|1.00|3|
|Velocidad = Alta → Clase = Deportivo|0.67|3|



|Reglas con Cilindros (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.75|4|
|Cilindros = Pocos → Clase = Utilitario|0.75|4|



|Reglas con Antigüedad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|1.00|1|
|Antigüedad = Baja → Clase = Deportivo|1.00|1|
|Antigüedad = Alta → Clase = Utilitario|0.83|6|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Alta', 'Alta', 'Baja', 'Alta', 'Alta', 'Media', 'Alta']


Valores nuevos: [3, 3, 3, 1, 3, 3, 2, 3]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|157|9|3|Utilitario|
|2|152|5|3|Utilitario|
|3|151|7|3|Utilitario|
|4|159|12|1|Deportivo|
|5|153|3|3|Utilitario|
|6|160|4|3|Deportivo|
|7|145|6|2|Utilitario|
|8|113|15|3|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|45|13|2|
|2|2|78|1|
|3|1|65|1|


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
