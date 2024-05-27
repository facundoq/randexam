---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|146|8|Alta|Utilitario|
|2|167|6|Media|Utilitario|
|3|156|14|Media|Utilitario|
|4|166|9|Baja|Utilitario|
|5|135|7|Baja|Utilitario|
|6|148|4|Baja|Deportivo|
|7|171|15|Media|Utilitario|
|8|140|15|Baja|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 3, 2, 3, 0, 1, 3, 0]

Intervalos: [[135.0,144.0), [144.0,153.0), [153.0,162.0), [162.0,171.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 3, 2, 2, 0, 1, 3, 0]

Intervalos: [[135,146), [146,156), [156,167), [167,171]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-4.00)/11.00

Valores normalizados: 0.36, 0.18, 0.91, 0.45, 0.27, 0.00, 1.00, 1.00

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Baja → Clase = Deportivo|0.12|0.50|0.25|2.00|
|Clase = Deportivo → Antigüedad = Alta|0.00|0.12|0.00|0.00|
|Velocidad < 154 and Antigüedad = Baja → Cilindros < 10|0.25|0.38|0.67|1.07|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Baja|Pocos|Alta|Utilitario|
|Alta|Pocos|Media|Utilitario|
|Media|Muchos|Media|Utilitario|
|Alta|Muchos|Baja|Utilitario|
|Baja|Pocos|Baja|Utilitario|
|Media|Pocos|Baja|Deportivo|
|Alta|Muchos|Media|Utilitario|
|Baja|Muchos|Baja|Utilitario|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|0.50|2|
|Velocidad = Baja → Clase = Utilitario|1.00|3|
|Velocidad = Alta → Clase = Utilitario|1.00|3|



|Reglas con Cilindros (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|1.00|4|
|Cilindros = Pocos → Clase = Utilitario|0.75|4|



|Reglas con Antigüedad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|1.00|3|
|Antigüedad = Baja → Clase = Utilitario|0.75|4|
|Antigüedad = Alta → Clase = Utilitario|1.00|1|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Media', 'Media', 'Baja', 'Baja', 'Baja', 'Media', 'Baja']


Valores nuevos: [3, 2, 2, 1, 1, 1, 2, 1]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|146|8|3|Utilitario|
|2|167|6|2|Utilitario|
|3|156|14|2|Utilitario|
|4|166|9|1|Utilitario|
|5|135|7|1|Utilitario|
|6|148|4|1|Deportivo|
|7|171|15|2|Utilitario|
|8|140|15|1|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|1|453|1|
|2|445|83|2|
|3|136|102|2|


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
