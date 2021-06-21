---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|182|4|Baja|Utilitario|
|2|138|5|Baja|Deportivo|
|3|123|11|Baja|Deportivo|
|4|160|5|Alta|Deportivo|
|5|162|10|Alta|Utilitario|
|6|150|8|Media|Deportivo|
|7|126|14|Baja|Utilitario|
|8|143|15|Alta|Deportivo|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [3, 1, 0, 2, 2, 1, 0, 1]

Intervalos: [[123.0,137.75), [137.75,152.5), [152.5,167.25), [167.25,182.0]]

Resultado de la discretización por frecuencia:

Valores: [3, 1, 0, 2, 3, 2, 0, 1]

Intervalos: [[123,138), [138,150), [150,162), [162,182]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-4.00)/11.00

Valores normalizados: 0.00, 0.09, 0.64, 0.09, 0.55, 0.36, 0.91, 1.00

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.00|0.12|0.00|0.00|
|Clase = Deportivo → Antigüedad = Alta|0.25|0.62|0.40|1.07|
|Velocidad < 148 and Antigüedad = Alta → Cilindros < 9|0.00|0.12|0.00|0.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Alta|Pocos|Baja|Utilitario|
|Baja|Pocos|Baja|Deportivo|
|Baja|Muchos|Baja|Deportivo|
|Alta|Pocos|Alta|Deportivo|
|Alta|Muchos|Alta|Utilitario|
|Media|Pocos|Media|Deportivo|
|Baja|Muchos|Baja|Utilitario|
|Media|Muchos|Alta|Deportivo|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Deportivo|1.00|2|
|Velocidad = Baja → Clase = Deportivo|0.67|3|
|Velocidad = Alta → Clase = Utilitario|0.67|3|



|Reglas con Cilindros (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.50|4|
|Cilindros = Pocos → Clase = Deportivo|0.75|4|



|Reglas con Antigüedad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|1.00|1|
|Antigüedad = Baja → Clase = Utilitario|0.50|4|
|Antigüedad = Alta → Clase = Deportivo|0.67|3|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Baja', 'Baja', 'Alta', 'Alta', 'Media', 'Baja', 'Alta']


Valores nuevos: [1, 1, 1, 3, 3, 2, 1, 3]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|182|4|1|Utilitario|
|2|138|5|1|Deportivo|
|3|123|11|1|Deportivo|
|4|160|5|3|Deportivo|
|5|162|10|3|Utilitario|
|6|150|8|2|Deportivo|
|7|126|14|1|Utilitario|
|8|143|15|3|Deportivo|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|1952|588|2|
|2|9|569|1|
|3|234|1382|1|


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
