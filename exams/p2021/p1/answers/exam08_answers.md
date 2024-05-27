---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|162|10|Media|Utilitario|
|2|163|10|Baja|Utilitario|
|3|154|5|Alta|Deportivo|
|4|163|8|Alta|Utilitario|
|5|138|12|Alta|Utilitario|
|6|168|2|Alta|Utilitario|
|7|157|4|Baja|Deportivo|
|8|145|6|Baja|Deportivo|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [3, 3, 2, 3, 0, 3, 2, 0]

Intervalos: [[138.0,145.5), [145.5,153.0), [153.0,160.5), [160.5,168.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 3, 1, 3, 0, 3, 1, 0]

Intervalos: [[138,154), [154,162), [162,163), [163,168]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-2.00)/10.00

Valores normalizados: 0.80, 0.80, 0.30, 0.60, 1.00, 0.00, 0.20, 0.40

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Baja → Clase = Deportivo|0.25|0.38|0.67|1.78|
|Clase = Utilitario → Antigüedad = Baja|0.12|0.62|0.20|0.53|
|Velocidad < 156 and Antigüedad = Alta → Cilindros < 7|0.12|0.25|0.50|1.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Media|Muchos|Media|Utilitario|
|Alta|Muchos|Baja|Utilitario|
|Baja|Pocos|Alta|Deportivo|
|Alta|Muchos|Alta|Utilitario|
|Baja|Muchos|Alta|Utilitario|
|Alta|Pocos|Alta|Utilitario|
|Media|Pocos|Baja|Deportivo|
|Baja|Pocos|Baja|Deportivo|


Mejor atributo: Cilindros


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|0.50|2|
|Velocidad = Baja → Clase = Deportivo|0.67|3|
|Velocidad = Alta → Clase = Utilitario|1.00|3|



|Reglas con Cilindros (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|1.00|4|
|Cilindros = Pocos → Clase = Deportivo|0.75|4|



|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|1.00|1|
|Antigüedad = Baja → Clase = Deportivo|0.67|3|
|Antigüedad = Alta → Clase = Utilitario|0.75|4|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Baja', 'Alta', 'Alta', 'Alta', 'Alta', 'Baja', 'Baja']


Valores nuevos: [2, 1, 3, 3, 3, 3, 1, 1]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|162|10|2|Utilitario|
|2|163|10|1|Utilitario|
|3|154|5|3|Deportivo|
|4|163|8|3|Utilitario|
|5|138|12|3|Utilitario|
|6|168|2|3|Utilitario|
|7|157|4|1|Deportivo|
|8|145|6|1|Deportivo|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|81|2|2|
|2|101|4|2|
|3|1|106|1|


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
