---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|152|15|Media|Utilitario|
|2|163|2|Baja|Deportivo|
|3|154|15|Media|Deportivo|
|4|119|7|Media|Deportivo|
|5|145|6|Alta|Deportivo|
|6|162|15|Media|Utilitario|
|7|153|15|Alta|Utilitario|
|8|161|14|Alta|Deportivo|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [3, 3, 3, 0, 2, 3, 3, 3]

Intervalos: [[119.0,130.0), [130.0,141.0), [141.0,152.0), [152.0,163.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 3, 2, 0, 0, 3, 1, 2]

Intervalos: [[119,152), [152,154), [154,162), [162,163]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-2.00)/13.00

Valores normalizados: 1.00, 0.00, 1.00, 0.38, 0.31, 1.00, 1.00, 0.92

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.25|0.50|0.50|1.33|
|Clase = Utilitario → Antigüedad = Media|0.25|0.38|0.67|1.33|
|Velocidad < 151 and Antigüedad = Media → Cilindros < 11|0.12|0.12|1.00|2.67|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Baja|Muchos|Media|Utilitario|
|Alta|Pocos|Baja|Deportivo|
|Media|Muchos|Media|Deportivo|
|Baja|Pocos|Media|Deportivo|
|Baja|Pocos|Alta|Deportivo|
|Alta|Muchos|Media|Utilitario|
|Media|Muchos|Alta|Utilitario|
|Alta|Pocos|Alta|Deportivo|


Mejor atributo: Cilindros


|Reglas con Velocidad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|0.50|2|
|Velocidad = Baja → Clase = Deportivo|0.67|3|
|Velocidad = Alta → Clase = Deportivo|0.67|3|



|Reglas con Cilindros (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.75|4|
|Cilindros = Pocos → Clase = Deportivo|1.00|4|



|Reglas con Antigüedad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.50|4|
|Antigüedad = Baja → Clase = Deportivo|1.00|1|
|Antigüedad = Alta → Clase = Deportivo|0.67|3|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Baja', 'Media', 'Media', 'Alta', 'Media', 'Alta', 'Alta']


Valores nuevos: [2, 1, 2, 2, 3, 2, 3, 3]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|152|15|2|Utilitario|
|2|163|2|1|Deportivo|
|3|154|15|2|Deportivo|
|4|119|7|2|Deportivo|
|5|145|6|3|Deportivo|
|6|162|15|2|Utilitario|
|7|153|15|3|Utilitario|
|8|161|14|3|Deportivo|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|1|81|1|
|2|266|174|2|
|3|5|49|1|


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
