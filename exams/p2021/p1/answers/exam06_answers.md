---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|147|10|Alta|Deportivo|
|2|136|15|Baja|Utilitario|
|3|138|2|Alta|Deportivo|
|4|175|3|Baja|Utilitario|
|5|150|2|Media|Deportivo|
|6|140|6|Baja|Deportivo|
|7|152|7|Media|Deportivo|
|8|181|4|Baja|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 0, 0, 3, 1, 0, 1, 3]

Intervalos: [[136.0,147.25), [147.25,158.5), [158.5,169.75), [169.75,181.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 0, 0, 3, 2, 1, 2, 3]

Intervalos: [[136,140), [140,150), [150,175), [175,181]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-2.00)/13.00

Valores normalizados: 0.62, 1.00, 0.00, 0.08, 0.00, 0.31, 0.38, 0.15

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Alta → Clase = Utilitario|0.00|0.25|0.00|0.00|
|Clase = Deportivo → Antigüedad = Alta|0.25|0.62|0.40|1.60|
|Velocidad < 152 and Antigüedad = Alta → Cilindros < 6|0.12|0.25|0.50|1.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Media|Muchos|Alta|Deportivo|
|Baja|Muchos|Baja|Utilitario|
|Baja|Pocos|Alta|Deportivo|
|Alta|Pocos|Baja|Utilitario|
|Media|Pocos|Media|Deportivo|
|Baja|Muchos|Baja|Deportivo|
|Alta|Muchos|Media|Deportivo|
|Alta|Pocos|Baja|Utilitario|


Mejor atributo: Antigüedad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Deportivo|1.00|2|
|Velocidad = Baja → Clase = Deportivo|0.67|3|
|Velocidad = Alta → Clase = Utilitario|0.67|3|



|Reglas con Cilindros (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Deportivo|0.75|4|
|Cilindros = Pocos → Clase = Utilitario|0.50|4|



|Reglas con Antigüedad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|1.00|2|
|Antigüedad = Baja → Clase = Utilitario|0.75|4|
|Antigüedad = Alta → Clase = Deportivo|1.00|2|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Baja', 'Alta', 'Baja', 'Media', 'Baja', 'Media', 'Baja']


Valores nuevos: [3, 1, 3, 1, 2, 1, 2, 1]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|147|10|3|Deportivo|
|2|136|15|1|Utilitario|
|3|138|2|3|Deportivo|
|4|175|3|1|Utilitario|
|5|150|2|2|Deportivo|
|6|140|6|1|Deportivo|
|7|152|7|2|Deportivo|
|8|181|4|1|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|85|29|2|
|2|141|281|1|
|3|8|264|1|


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
