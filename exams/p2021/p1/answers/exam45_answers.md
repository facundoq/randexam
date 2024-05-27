---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|147|10|Media|Utilitario|
|2|162|3|Alta|Utilitario|
|3|139|3|Baja|Utilitario|
|4|141|11|Alta|Deportivo|
|5|152|4|Alta|Utilitario|
|6|147|8|Alta|Utilitario|
|7|143|15|Media|Deportivo|
|8|139|14|Alta|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 3, 0, 0, 2, 1, 0, 0]

Intervalos: [[139.0,144.75), [144.75,150.5), [150.5,156.25), [156.25,162.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 3, 0, 1, 3, 2, 1, 0]

Intervalos: [[139,141), [141,147), [147,152), [152,162]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-3.00)/12.00

Valores normalizados: 0.58, 0.00, 0.00, 0.67, 0.08, 0.42, 1.00, 0.92

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Baja → Clase = Utilitario|0.12|0.12|1.00|1.33|
|Clase = Utilitario → Antigüedad = Alta|0.50|0.75|0.67|1.07|
|Velocidad < 146 and Antigüedad = Alta → Cilindros < 8|0.00|0.25|0.00|0.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Alta|Muchos|Media|Utilitario|
|Alta|Pocos|Alta|Utilitario|
|Baja|Pocos|Baja|Utilitario|
|Baja|Muchos|Alta|Deportivo|
|Alta|Pocos|Alta|Utilitario|
|Alta|Pocos|Alta|Utilitario|
|Media|Muchos|Media|Deportivo|
|Baja|Muchos|Alta|Utilitario|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Deportivo|1.00|1|
|Velocidad = Baja → Clase = Utilitario|0.67|3|
|Velocidad = Alta → Clase = Utilitario|1.00|4|



|Reglas con Cilindros (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.50|4|
|Cilindros = Pocos → Clase = Utilitario|1.00|4|



|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.50|2|
|Antigüedad = Baja → Clase = Utilitario|1.00|1|
|Antigüedad = Alta → Clase = Utilitario|0.80|5|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Alta', 'Baja', 'Alta', 'Alta', 'Alta', 'Media', 'Alta']


Valores nuevos: [2, 3, 1, 3, 3, 3, 2, 3]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|147|10|2|Utilitario|
|2|162|3|3|Utilitario|
|3|139|3|1|Utilitario|
|4|141|11|3|Deportivo|
|5|152|4|3|Utilitario|
|6|147|8|3|Utilitario|
|7|143|15|2|Deportivo|
|8|139|14|3|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|41|17|2|
|2|470|346|2|
|3|29|189|1|


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
