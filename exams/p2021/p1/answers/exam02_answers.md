---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|154|2|Alta|Deportivo|
|2|146|8|Alta|Deportivo|
|3|171|8|Alta|Deportivo|
|4|119|10|Baja|Utilitario|
|5|145|9|Alta|Deportivo|
|6|144|7|Baja|Deportivo|
|7|167|14|Media|Utilitario|
|8|133|2|Media|Deportivo|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 2, 3, 0, 2, 1, 3, 1]

Intervalos: [[119.0,132.0), [132.0,145.0), [145.0,158.0), [158.0,171.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 2, 3, 0, 1, 1, 3, 0]

Intervalos: [[119,144), [144,146), [146,167), [167,171]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-2.00)/12.00

Valores normalizados: 0.00, 0.50, 0.50, 0.67, 0.58, 0.42, 1.00, 0.00

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|0.12|0.25|0.50|0.67|
|Clase = Utilitario → Antigüedad = Alta|0.00|0.25|0.00|0.00|
|Velocidad < 147 and Antigüedad = Baja → Cilindros < 8|0.12|0.25|0.50|1.33|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Alta|Pocos|Alta|Deportivo|
|Media|Muchos|Alta|Deportivo|
|Alta|Muchos|Alta|Deportivo|
|Baja|Muchos|Baja|Utilitario|
|Media|Muchos|Alta|Deportivo|
|Baja|Pocos|Baja|Deportivo|
|Alta|Muchos|Media|Utilitario|
|Baja|Pocos|Media|Deportivo|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Deportivo|1.00|2|
|Velocidad = Baja → Clase = Deportivo|0.67|3|
|Velocidad = Alta → Clase = Deportivo|0.67|3|



|Reglas con Cilindros (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Deportivo|0.60|5|
|Cilindros = Pocos → Clase = Deportivo|1.00|3|



|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.50|2|
|Antigüedad = Baja → Clase = Utilitario|0.50|2|
|Antigüedad = Alta → Clase = Deportivo|1.00|4|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Alta', 'Alta', 'Baja', 'Alta', 'Baja', 'Media', 'Media']


Valores nuevos: [3, 3, 3, 1, 3, 1, 2, 2]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|154|2|3|Deportivo|
|2|146|8|3|Deportivo|
|3|171|8|3|Deportivo|
|4|119|10|1|Utilitario|
|5|145|9|3|Deportivo|
|6|144|7|1|Deportivo|
|7|167|14|2|Utilitario|
|8|133|2|2|Deportivo|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|136|68|2|
|2|4|72|1|
|3|729|297|2|


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
