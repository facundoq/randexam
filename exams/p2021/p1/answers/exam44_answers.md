---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|148|11|Baja|Deportivo|
|2|150|10|Media|Utilitario|
|3|147|2|Alta|Deportivo|
|4|147|13|Alta|Utilitario|
|5|156|15|Alta|Deportivo|
|6|132|6|Alta|Utilitario|
|7|165|4|Media|Deportivo|
|8|163|14|Baja|Deportivo|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [1, 2, 1, 1, 2, 0, 3, 3]

Intervalos: [[132.0,140.25), [140.25,148.5), [148.5,156.75), [156.75,165.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 2, 1, 1, 2, 0, 3, 3]

Intervalos: [[132,147), [147,150), [150,163), [163,165]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-2.00)/13.00

Valores normalizados: 0.69, 0.62, 0.00, 0.85, 1.00, 0.31, 0.15, 0.92

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Baja → Clase = Utilitario|0.00|0.25|0.00|0.00|
|Clase = Deportivo → Antigüedad = Baja|0.25|0.62|0.40|1.60|
|Velocidad < 151 and Antigüedad = Alta → Cilindros < 9|0.25|0.38|0.67|1.78|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Media|Muchos|Baja|Deportivo|
|Media|Pocos|Media|Utilitario|
|Baja|Pocos|Alta|Deportivo|
|Baja|Muchos|Alta|Utilitario|
|Alta|Muchos|Alta|Deportivo|
|Baja|Pocos|Alta|Utilitario|
|Alta|Pocos|Media|Deportivo|
|Alta|Muchos|Baja|Deportivo|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|0.50|2|
|Velocidad = Baja → Clase = Utilitario|0.67|3|
|Velocidad = Alta → Clase = Deportivo|1.00|3|



|Reglas con Cilindros (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Deportivo|0.75|4|
|Cilindros = Pocos → Clase = Utilitario|0.50|4|



|Reglas con Antigüedad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.50|2|
|Antigüedad = Baja → Clase = Deportivo|1.00|2|
|Antigüedad = Alta → Clase = Utilitario|0.50|4|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Media', 'Alta', 'Alta', 'Alta', 'Alta', 'Media', 'Baja']


Valores nuevos: [1, 2, 3, 3, 3, 3, 2, 1]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|148|11|1|Deportivo|
|2|150|10|2|Utilitario|
|3|147|2|3|Deportivo|
|4|147|13|3|Utilitario|
|5|156|15|3|Deportivo|
|6|132|6|3|Utilitario|
|7|165|4|2|Deportivo|
|8|163|14|1|Deportivo|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|6|77|1|
|2|10|53|1|
|3|64|225|1|


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
