---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|159|2|Baja|Deportivo|
|2|176|9|Alta|Utilitario|
|3|148|7|Alta|Utilitario|
|4|131|3|Alta|Deportivo|
|5|132|3|Baja|Utilitario|
|6|140|5|Media|Utilitario|
|7|124|8|Baja|Deportivo|
|8|162|5|Media|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 3, 1, 0, 0, 1, 0, 2]

Intervalos: [[124.0,137.0), [137.0,150.0), [150.0,163.0), [163.0,176.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 3, 2, 0, 1, 1, 0, 3]

Intervalos: [[124,132), [132,148), [148,162), [162,176]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-2.00)/7.00

Valores normalizados: 0.00, 1.00, 0.71, 0.14, 0.14, 0.43, 0.86, 0.43

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Alta → Clase = Deportivo|0.12|0.38|0.33|0.89|
|Clase = Utilitario → Antigüedad = Baja|0.12|0.62|0.20|0.53|
|Velocidad < 146 and Antigüedad = Alta → Cilindros < 5|0.12|0.12|1.00|2.67|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Alta|Pocos|Baja|Deportivo|
|Alta|Muchos|Alta|Utilitario|
|Media|Muchos|Alta|Utilitario|
|Baja|Pocos|Alta|Deportivo|
|Baja|Pocos|Baja|Utilitario|
|Media|Muchos|Media|Utilitario|
|Baja|Muchos|Baja|Deportivo|
|Alta|Muchos|Media|Utilitario|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|1.00|2|
|Velocidad = Baja → Clase = Deportivo|0.67|3|
|Velocidad = Alta → Clase = Utilitario|0.67|3|



|Reglas con Cilindros (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.80|5|
|Cilindros = Pocos → Clase = Deportivo|0.67|3|



|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|1.00|2|
|Antigüedad = Baja → Clase = Deportivo|0.67|3|
|Antigüedad = Alta → Clase = Utilitario|0.67|3|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Alta', 'Alta', 'Alta', 'Baja', 'Media', 'Baja', 'Media']


Valores nuevos: [1, 3, 3, 3, 1, 2, 1, 2]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|159|2|1|Deportivo|
|2|176|9|3|Utilitario|
|3|148|7|3|Utilitario|
|4|131|3|3|Deportivo|
|5|132|3|1|Utilitario|
|6|140|5|2|Utilitario|
|7|124|8|1|Deportivo|
|8|162|5|2|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|742|40|2|
|2|1952|290|2|
|3|260|122|2|


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
