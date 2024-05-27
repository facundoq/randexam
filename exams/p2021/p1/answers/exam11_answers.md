---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|146|4|Alta|Deportivo|
|2|146|6|Media|Utilitario|
|3|152|7|Media|Utilitario|
|4|156|3|Media|Deportivo|
|5|152|15|Alta|Utilitario|
|6|151|4|Alta|Deportivo|
|7|139|7|Baja|Utilitario|
|8|155|3|Media|Deportivo|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 1, 3, 3, 3, 2, 0, 3]

Intervalos: [[139.0,143.25), [143.25,147.5), [147.5,151.75), [151.75,156.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 1, 2, 3, 2, 1, 0, 3]

Intervalos: [[139,146), [146,152), [152,155), [155,156]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-3.00)/12.00

Valores normalizados: 0.08, 0.25, 0.33, 0.00, 1.00, 0.08, 0.33, 0.00

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|0.25|0.50|0.50|1.00|
|Clase = Utilitario → Antigüedad = Alta|0.12|0.50|0.25|0.67|
|Velocidad < 150 and Antigüedad = Alta → Cilindros < 6|0.12|0.12|1.00|2.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Baja|Pocos|Alta|Deportivo|
|Baja|Muchos|Media|Utilitario|
|Alta|Muchos|Media|Utilitario|
|Alta|Pocos|Media|Deportivo|
|Alta|Muchos|Alta|Utilitario|
|Media|Pocos|Alta|Deportivo|
|Baja|Muchos|Baja|Utilitario|
|Alta|Pocos|Media|Deportivo|


Mejor atributo: Cilindros


|Reglas con Velocidad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Deportivo|1.00|1|
|Velocidad = Baja → Clase = Utilitario|0.67|3|
|Velocidad = Alta → Clase = Utilitario|0.50|4|



|Reglas con Cilindros (accuracy=1.0)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|1.00|4|
|Cilindros = Pocos → Clase = Deportivo|1.00|4|



|Reglas con Antigüedad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.50|4|
|Antigüedad = Baja → Clase = Utilitario|1.00|1|
|Antigüedad = Alta → Clase = Deportivo|0.67|3|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Media', 'Media', 'Media', 'Alta', 'Alta', 'Baja', 'Media']


Valores nuevos: [3, 2, 2, 2, 3, 3, 1, 2]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|146|4|3|Deportivo|
|2|146|6|2|Utilitario|
|3|152|7|2|Utilitario|
|4|156|3|2|Deportivo|
|5|152|15|3|Utilitario|
|6|151|4|3|Deportivo|
|7|139|7|1|Utilitario|
|8|155|3|2|Deportivo|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|1|46|1|
|2|4|37|1|
|3|45|0|2|


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
