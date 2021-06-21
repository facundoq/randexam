---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|156|13|Media|Utilitario|
|2|161|14|Alta|Utilitario|
|3|135|8|Media|Utilitario|
|4|158|11|Media|Deportivo|
|5|180|2|Baja|Utilitario|
|6|127|12|Baja|Deportivo|
|7|137|3|Baja|Utilitario|
|8|136|13|Alta|Deportivo|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 2, 0, 2, 3, 0, 0, 0]

Intervalos: [[127.0,140.25), [140.25,153.5), [153.5,166.75), [166.75,180.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 3, 0, 2, 3, 0, 1, 1]

Intervalos: [[127,136), [136,156), [156,161), [161,180]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-2.00)/12.00

Valores normalizados: 0.92, 1.00, 0.50, 0.75, 0.00, 0.83, 0.08, 0.92

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|0.12|0.38|0.33|0.89|
|Clase = Utilitario → Antigüedad = Media|0.25|0.62|0.40|1.07|
|Velocidad < 149 and Antigüedad = Baja → Cilindros < 10|0.12|0.25|0.50|1.33|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Media|Muchos|Media|Utilitario|
|Alta|Muchos|Alta|Utilitario|
|Baja|Pocos|Media|Utilitario|
|Alta|Pocos|Media|Deportivo|
|Alta|Pocos|Baja|Utilitario|
|Baja|Muchos|Baja|Deportivo|
|Media|Pocos|Baja|Utilitario|
|Baja|Muchos|Alta|Deportivo|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|1.00|2|
|Velocidad = Baja → Clase = Deportivo|0.67|3|
|Velocidad = Alta → Clase = Utilitario|0.67|3|



|Reglas con Cilindros (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.50|4|
|Cilindros = Pocos → Clase = Utilitario|0.75|4|



|Reglas con Antigüedad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.67|3|
|Antigüedad = Baja → Clase = Utilitario|0.67|3|
|Antigüedad = Alta → Clase = Utilitario|0.50|2|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Alta', 'Media', 'Media', 'Baja', 'Baja', 'Baja', 'Alta']


Valores nuevos: [2, 3, 2, 2, 1, 1, 1, 3]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|156|13|2|Utilitario|
|2|161|14|3|Utilitario|
|3|135|8|2|Utilitario|
|4|158|11|2|Deportivo|
|5|180|2|1|Utilitario|
|6|127|12|1|Deportivo|
|7|137|3|1|Utilitario|
|8|136|13|3|Deportivo|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|404|4|2|
|2|635|11|2|
|3|10|554|1|


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
