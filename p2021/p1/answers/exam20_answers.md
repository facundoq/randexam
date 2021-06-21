---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|165|10|Media|Utilitario|
|2|182|4|Baja|Utilitario|
|3|156|8|Baja|Deportivo|
|4|148|9|Alta|Utilitario|
|5|147|13|Alta|Utilitario|
|6|148|8|Alta|Deportivo|
|7|150|10|Alta|Deportivo|
|8|133|10|Baja|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 3, 1, 1, 1, 1, 1, 0]

Intervalos: [[133.0,145.25), [145.25,157.5), [157.5,169.75), [169.75,182.0]]

Resultado de la discretización por frecuencia:

Valores: [3, 3, 2, 1, 0, 1, 2, 0]

Intervalos: [[133,148), [148,150), [150,165), [165,182]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-4.00)/9.00

Valores normalizados: 0.67, 0.00, 0.44, 0.56, 1.00, 0.44, 0.67, 0.67

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Alta → Clase = Utilitario|0.25|0.50|0.50|0.80|
|Clase = Deportivo → Antigüedad = Alta|0.25|0.38|0.67|1.33|
|Velocidad < 154 and Antigüedad = Media → Cilindros < 9|0.00|0.00|1.00|inf|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Alta|Muchos|Media|Utilitario|
|Alta|Pocos|Baja|Utilitario|
|Alta|Pocos|Baja|Deportivo|
|Media|Pocos|Alta|Utilitario|
|Baja|Muchos|Alta|Utilitario|
|Media|Pocos|Alta|Deportivo|
|Media|Muchos|Alta|Deportivo|
|Baja|Muchos|Baja|Utilitario|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Deportivo|0.67|3|
|Velocidad = Baja → Clase = Utilitario|1.00|2|
|Velocidad = Alta → Clase = Utilitario|0.67|3|



|Reglas con Cilindros (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.75|4|
|Cilindros = Pocos → Clase = Utilitario|0.50|4|



|Reglas con Antigüedad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|1.00|1|
|Antigüedad = Baja → Clase = Utilitario|0.67|3|
|Antigüedad = Alta → Clase = Utilitario|0.50|4|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Baja', 'Baja', 'Alta', 'Alta', 'Alta', 'Alta', 'Baja']


Valores nuevos: [2, 1, 1, 3, 3, 3, 3, 1]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|165|10|2|Utilitario|
|2|182|4|1|Utilitario|
|3|156|8|1|Deportivo|
|4|148|9|3|Utilitario|
|5|147|13|3|Utilitario|
|6|148|8|3|Deportivo|
|7|150|10|3|Deportivo|
|8|133|10|1|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|291|82|2|
|2|1181|716|2|
|3|65|8|2|


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
