---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|142|4|Alta|Deportivo|
|2|135|9|Baja|Utilitario|
|3|153|14|Media|Utilitario|
|4|145|4|Media|Utilitario|
|5|157|4|Alta|Utilitario|
|6|147|5|Baja|Utilitario|
|7|164|11|Alta|Utilitario|
|8|153|3|Alta|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 0, 2, 1, 3, 1, 3, 2]

Intervalos: [[135.0,142.25), [142.25,149.5), [149.5,156.75), [156.75,164.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 0, 2, 1, 3, 1, 3, 2]

Intervalos: [[135,145), [145,153), [153,157), [157,164]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-3.00)/11.00

Valores normalizados: 0.09, 0.55, 1.00, 0.09, 0.09, 0.18, 0.73, 0.00

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Baja → Clase = Utilitario|0.25|0.25|1.00|1.14|
|Clase = Deportivo → Antigüedad = Alta|0.12|0.12|1.00|2.00|
|Velocidad < 150 and Antigüedad = Alta → Cilindros < 7|0.12|0.12|1.00|1.60|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Baja|Pocos|Alta|Deportivo|
|Baja|Muchos|Baja|Utilitario|
|Alta|Muchos|Media|Utilitario|
|Baja|Pocos|Media|Utilitario|
|Alta|Pocos|Alta|Utilitario|
|Media|Muchos|Baja|Utilitario|
|Alta|Muchos|Alta|Utilitario|
|Alta|Pocos|Alta|Utilitario|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|1.00|1|
|Velocidad = Baja → Clase = Utilitario|0.67|3|
|Velocidad = Alta → Clase = Utilitario|1.00|4|



|Reglas con Cilindros (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|1.00|4|
|Cilindros = Pocos → Clase = Utilitario|0.75|4|



|Reglas con Antigüedad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|1.00|2|
|Antigüedad = Baja → Clase = Utilitario|1.00|2|
|Antigüedad = Alta → Clase = Utilitario|0.75|4|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Baja', 'Media', 'Media', 'Alta', 'Baja', 'Alta', 'Alta']


Valores nuevos: [3, 1, 2, 2, 3, 1, 3, 3]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|142|4|3|Deportivo|
|2|135|9|1|Utilitario|
|3|153|14|2|Utilitario|
|4|145|4|2|Utilitario|
|5|157|4|3|Utilitario|
|6|147|5|1|Utilitario|
|7|164|11|3|Utilitario|
|8|153|3|3|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|10|171|1|
|2|126|329|1|
|3|164|9|2|


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
