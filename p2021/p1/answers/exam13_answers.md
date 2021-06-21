---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|144|4|Baja|Utilitario|
|2|150|4|Alta|Deportivo|
|3|140|4|Alta|Deportivo|
|4|160|8|Media|Utilitario|
|5|143|10|Media|Utilitario|
|6|168|7|Baja|Deportivo|
|7|156|12|Media|Deportivo|
|8|158|2|Baja|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 1, 0, 2, 0, 3, 2, 2]

Intervalos: [[140.0,147.0), [147.0,154.0), [154.0,161.0), [161.0,168.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 1, 0, 3, 0, 3, 2, 2]

Intervalos: [[140,144), [144,156), [156,160), [160,168]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-2.00)/10.00

Valores normalizados: 0.20, 0.20, 0.20, 0.60, 0.80, 0.50, 1.00, 0.00

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Alta → Clase = Deportivo|0.25|0.25|1.00|2.00|
|Clase = Deportivo → Antigüedad = Baja|0.12|0.50|0.25|0.67|
|Velocidad < 152 and Antigüedad = Baja → Cilindros < 6|0.12|0.12|1.00|2.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Baja|Pocos|Baja|Utilitario|
|Media|Pocos|Alta|Deportivo|
|Baja|Pocos|Alta|Deportivo|
|Alta|Muchos|Media|Utilitario|
|Baja|Muchos|Media|Utilitario|
|Alta|Muchos|Baja|Deportivo|
|Media|Muchos|Media|Deportivo|
|Alta|Pocos|Baja|Utilitario|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Deportivo|1.00|2|
|Velocidad = Baja → Clase = Utilitario|0.67|3|
|Velocidad = Alta → Clase = Utilitario|0.67|3|



|Reglas con Cilindros (accuracy=0.5)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.50|4|
|Cilindros = Pocos → Clase = Utilitario|0.50|4|



|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.67|3|
|Antigüedad = Baja → Clase = Utilitario|0.67|3|
|Antigüedad = Alta → Clase = Deportivo|1.00|2|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Alta', 'Alta', 'Media', 'Media', 'Baja', 'Media', 'Baja']


Valores nuevos: [1, 3, 3, 2, 2, 1, 2, 1]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|144|4|1|Utilitario|
|2|150|4|3|Deportivo|
|3|140|4|3|Deportivo|
|4|160|8|2|Utilitario|
|5|143|10|2|Utilitario|
|6|168|7|1|Deportivo|
|7|156|12|2|Deportivo|
|8|158|2|1|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|4|233|1|
|2|36|101|1|
|3|16|361|1|


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
