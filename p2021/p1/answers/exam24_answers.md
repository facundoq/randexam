---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|148|13|Media|Utilitario|
|2|140|6|Alta|Utilitario|
|3|158|7|Alta|Utilitario|
|4|153|3|Alta|Utilitario|
|5|154|8|Baja|Deportivo|
|6|148|6|Alta|Deportivo|
|7|167|9|Alta|Utilitario|
|8|155|13|Alta|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 0, 2, 1, 2, 1, 3, 2]

Intervalos: [[140.0,146.75), [146.75,153.5), [153.5,160.25), [160.25,167.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 0, 3, 1, 2, 1, 3, 2]

Intervalos: [[140,148), [148,154), [154,158), [158,167]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-3.00)/10.00

Valores normalizados: 1.00, 0.30, 0.40, 0.00, 0.50, 0.30, 0.60, 1.00

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Alta → Clase = Utilitario|0.62|0.75|0.83|1.11|
|Clase = Deportivo → Antigüedad = Alta|0.12|0.25|0.50|0.67|
|Velocidad < 153 and Antigüedad = Alta → Cilindros < 8|0.25|0.25|1.00|2.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Baja|Muchos|Media|Utilitario|
|Baja|Pocos|Alta|Utilitario|
|Alta|Pocos|Alta|Utilitario|
|Media|Pocos|Alta|Utilitario|
|Media|Muchos|Baja|Deportivo|
|Baja|Pocos|Alta|Deportivo|
|Alta|Muchos|Alta|Utilitario|
|Alta|Muchos|Alta|Utilitario|


Mejor atributo: Antigüedad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|0.50|2|
|Velocidad = Baja → Clase = Utilitario|0.67|3|
|Velocidad = Alta → Clase = Utilitario|1.00|3|



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
 Valores originales: ['Media', 'Alta', 'Alta', 'Alta', 'Baja', 'Alta', 'Alta', 'Alta']


Valores nuevos: [2, 3, 3, 3, 1, 3, 3, 3]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|148|13|2|Utilitario|
|2|140|6|3|Utilitario|
|3|158|7|3|Utilitario|
|4|153|3|3|Utilitario|
|5|154|8|1|Deportivo|
|6|148|6|3|Deportivo|
|7|167|9|3|Utilitario|
|8|155|13|3|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|37|50|1|
|2|65|274|1|
|3|100|45|2|


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
