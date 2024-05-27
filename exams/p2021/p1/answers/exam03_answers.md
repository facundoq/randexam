---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|147|13|Alta|Utilitario|
|2|136|10|Alta|Deportivo|
|3|150|6|Media|Utilitario|
|4|158|15|Alta|Utilitario|
|5|133|11|Baja|Utilitario|
|6|167|5|Alta|Utilitario|
|7|163|8|Alta|Deportivo|
|8|157|7|Alta|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 0, 2, 2, 0, 3, 3, 2]

Intervalos: [[133.0,141.5), [141.5,150.0), [150.0,158.5), [158.5,167.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 0, 1, 2, 0, 3, 3, 2]

Intervalos: [[133,147), [147,157), [157,163), [163,167]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-5.00)/10.00

Valores normalizados: 0.80, 0.50, 0.10, 1.00, 0.60, 0.00, 0.30, 0.20

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|0.00|0.12|0.00|0.00|
|Clase = Utilitario → Antigüedad = Media|0.12|0.75|0.17|1.33|
|Velocidad < 151 and Antigüedad = Alta → Cilindros < 9|0.00|0.25|0.00|0.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Baja|Muchos|Alta|Utilitario|
|Baja|Muchos|Alta|Deportivo|
|Media|Pocos|Media|Utilitario|
|Alta|Muchos|Alta|Utilitario|
|Baja|Muchos|Baja|Utilitario|
|Alta|Pocos|Alta|Utilitario|
|Alta|Pocos|Alta|Deportivo|
|Media|Pocos|Alta|Utilitario|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|1.00|2|
|Velocidad = Baja → Clase = Utilitario|0.67|3|
|Velocidad = Alta → Clase = Utilitario|0.67|3|



|Reglas con Cilindros (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.75|4|
|Cilindros = Pocos → Clase = Utilitario|0.75|4|



|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|1.00|1|
|Antigüedad = Baja → Clase = Utilitario|1.00|1|
|Antigüedad = Alta → Clase = Utilitario|0.67|6|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Alta', 'Media', 'Alta', 'Baja', 'Alta', 'Alta', 'Alta']


Valores nuevos: [3, 3, 2, 3, 1, 3, 3, 3]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|147|13|3|Utilitario|
|2|136|10|3|Deportivo|
|3|150|6|2|Utilitario|
|4|158|15|3|Utilitario|
|5|133|11|1|Utilitario|
|6|167|5|3|Utilitario|
|7|163|8|3|Deportivo|
|8|157|7|3|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|26|121|1|
|2|126|493|1|
|3|13|114|1|


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
