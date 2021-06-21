---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|162|12|Media|Deportivo|
|2|137|8|Media|Deportivo|
|3|155|7|Baja|Utilitario|
|4|130|14|Alta|Utilitario|
|5|149|5|Media|Deportivo|
|6|125|10|Alta|Deportivo|
|7|166|5|Baja|Deportivo|
|8|156|14|Baja|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [3, 1, 2, 0, 2, 0, 3, 3]

Intervalos: [[125.0,135.25), [135.25,145.5), [145.5,155.75), [155.75,166.0]]

Resultado de la discretización por frecuencia:

Valores: [3, 1, 2, 0, 1, 0, 3, 2]

Intervalos: [[125,137), [137,155), [155,162), [162,166]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-5.00)/9.00

Valores normalizados: 0.78, 0.33, 0.22, 1.00, 0.00, 0.56, 0.00, 1.00

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|0.38|0.38|1.00|1.60|
|Clase = Utilitario → Antigüedad = Alta|0.12|0.38|0.33|1.33|
|Velocidad < 148 and Antigüedad = Media → Cilindros < 9|0.12|0.12|1.00|2.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Alta|Muchos|Media|Deportivo|
|Baja|Pocos|Media|Deportivo|
|Media|Pocos|Baja|Utilitario|
|Baja|Muchos|Alta|Utilitario|
|Media|Pocos|Media|Deportivo|
|Baja|Muchos|Alta|Deportivo|
|Alta|Pocos|Baja|Deportivo|
|Alta|Muchos|Baja|Utilitario|


Mejor atributo: Antigüedad


|Reglas con Velocidad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|0.50|2|
|Velocidad = Baja → Clase = Deportivo|0.67|3|
|Velocidad = Alta → Clase = Deportivo|0.67|3|



|Reglas con Cilindros (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.50|4|
|Cilindros = Pocos → Clase = Deportivo|0.75|4|



|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|1.00|3|
|Antigüedad = Baja → Clase = Utilitario|0.67|3|
|Antigüedad = Alta → Clase = Utilitario|0.50|2|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Media', 'Baja', 'Alta', 'Media', 'Alta', 'Baja', 'Baja']


Valores nuevos: [2, 2, 1, 3, 2, 3, 1, 1]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|162|12|2|Deportivo|
|2|137|8|2|Deportivo|
|3|155|7|1|Utilitario|
|4|130|14|3|Utilitario|
|5|149|5|2|Deportivo|
|6|125|10|3|Deportivo|
|7|166|5|1|Deportivo|
|8|156|14|1|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|642|41|2|
|2|1|398|1|
|3|325|54|2|


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
