---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|141|7|Alta|Utilitario|
|2|164|2|Alta|Utilitario|
|3|120|6|Baja|Deportivo|
|4|155|10|Media|Utilitario|
|5|146|13|Baja|Utilitario|
|6|160|4|Baja|Utilitario|
|7|157|5|Media|Deportivo|
|8|108|10|Alta|Deportivo|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 3, 0, 3, 2, 3, 3, 0]

Intervalos: [[108.0,122.0), [122.0,136.0), [136.0,150.0), [150.0,164.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 3, 0, 2, 1, 3, 2, 0]

Intervalos: [[108,141), [141,155), [155,160), [160,164]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-2.00)/11.00

Valores normalizados: 0.45, 0.00, 0.36, 0.73, 1.00, 0.18, 0.27, 0.73

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Baja → Clase = Deportivo|0.12|0.38|0.33|0.89|
|Clase = Deportivo → Antigüedad = Baja|0.12|0.38|0.33|0.89|
|Velocidad < 144 and Antigüedad = Alta → Cilindros < 7|0.00|0.25|0.00|0.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Baja|Muchos|Alta|Utilitario|
|Alta|Pocos|Alta|Utilitario|
|Baja|Pocos|Baja|Deportivo|
|Media|Muchos|Media|Utilitario|
|Media|Muchos|Baja|Utilitario|
|Alta|Pocos|Baja|Utilitario|
|Alta|Pocos|Media|Deportivo|
|Baja|Muchos|Alta|Deportivo|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|1.00|2|
|Velocidad = Baja → Clase = Deportivo|0.67|3|
|Velocidad = Alta → Clase = Utilitario|0.67|3|



|Reglas con Cilindros (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.75|4|
|Cilindros = Pocos → Clase = Utilitario|0.50|4|



|Reglas con Antigüedad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.50|2|
|Antigüedad = Baja → Clase = Utilitario|0.67|3|
|Antigüedad = Alta → Clase = Utilitario|0.67|3|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Alta', 'Baja', 'Media', 'Baja', 'Baja', 'Media', 'Alta']


Valores nuevos: [3, 3, 1, 2, 1, 1, 2, 3]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|141|7|3|Utilitario|
|2|164|2|3|Utilitario|
|3|120|6|1|Deportivo|
|4|155|10|2|Utilitario|
|5|146|13|1|Utilitario|
|6|160|4|1|Utilitario|
|7|157|5|2|Deportivo|
|8|108|10|3|Deportivo|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|5|266|1|
|2|549|114|2|
|3|441|1386|1|


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
