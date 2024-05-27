---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|178|10|Baja|Utilitario|
|2|166|10|Baja|Utilitario|
|3|159|11|Media|Utilitario|
|4|125|7|Alta|Deportivo|
|5|159|9|Alta|Deportivo|
|6|156|12|Alta|Utilitario|
|7|162|12|Baja|Utilitario|
|8|165|13|Alta|Deportivo|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [3, 3, 2, 0, 2, 2, 2, 3]

Intervalos: [[125.0,138.25), [138.25,151.5), [151.5,164.75), [164.75,178.0]]

Resultado de la discretización por frecuencia:

Valores: [3, 3, 1, 0, 1, 0, 2, 2]

Intervalos: [[125,159), [159,162), [162,166), [166,178]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-7.00)/6.00

Valores normalizados: 0.50, 0.50, 0.67, 0.00, 0.33, 0.83, 0.83, 1.00

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Alta → Clase = Deportivo|0.38|0.50|0.75|2.00|
|Clase = Deportivo → Antigüedad = Media|0.00|0.38|0.00|0.00|
|Velocidad < 159 and Antigüedad = Media → Cilindros < 10|0.00|0.00|1.00|inf|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Alta|Pocos|Baja|Utilitario|
|Alta|Pocos|Baja|Utilitario|
|Media|Muchos|Media|Utilitario|
|Baja|Pocos|Alta|Deportivo|
|Media|Pocos|Alta|Deportivo|
|Baja|Muchos|Alta|Utilitario|
|Media|Muchos|Baja|Utilitario|
|Alta|Muchos|Alta|Deportivo|


Mejor atributo: Antigüedad


|Reglas con Velocidad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|0.67|3|
|Velocidad = Baja → Clase = Utilitario|0.50|2|
|Velocidad = Alta → Clase = Utilitario|0.67|3|



|Reglas con Cilindros (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.75|4|
|Cilindros = Pocos → Clase = Utilitario|0.50|4|



|Reglas con Antigüedad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|1.00|1|
|Antigüedad = Baja → Clase = Utilitario|1.00|3|
|Antigüedad = Alta → Clase = Deportivo|0.75|4|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Baja', 'Media', 'Alta', 'Alta', 'Alta', 'Baja', 'Alta']


Valores nuevos: [1, 1, 2, 3, 3, 3, 1, 3]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|178|10|1|Utilitario|
|2|166|10|1|Utilitario|
|3|159|11|2|Utilitario|
|4|125|7|3|Deportivo|
|5|159|9|3|Deportivo|
|6|156|12|3|Utilitario|
|7|162|12|1|Utilitario|
|8|165|13|3|Deportivo|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|362|177|2|
|2|50|9|2|
|3|1|38|1|


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
