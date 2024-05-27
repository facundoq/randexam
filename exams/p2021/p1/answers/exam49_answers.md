---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|159|15|Media|Utilitario|
|2|147|11|Alta|Utilitario|
|3|148|2|Baja|Utilitario|
|4|147|7|Baja|Deportivo|
|5|135|6|Baja|Deportivo|
|6|142|7|Baja|Deportivo|
|7|128|13|Baja|Utilitario|
|8|176|7|Baja|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 1, 1, 1, 0, 1, 0, 3]

Intervalos: [[128.0,140.0), [140.0,152.0), [152.0,164.0), [164.0,176.0]]

Resultado de la discretización por frecuencia:

Valores: [3, 2, 2, 2, 0, 1, 0, 3]

Intervalos: [[128,142), [142,147), [147,159), [159,176]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-2.00)/13.00

Valores normalizados: 1.00, 0.69, 0.00, 0.38, 0.31, 0.38, 0.85, 0.38

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Alta → Clase = Utilitario|0.12|0.12|1.00|1.60|
|Clase = Deportivo → Antigüedad = Media|0.00|0.38|0.00|0.00|
|Velocidad < 148 and Antigüedad = Media → Cilindros < 8|0.00|0.00|1.00|inf|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Alta|Muchos|Media|Utilitario|
|Media|Muchos|Alta|Utilitario|
|Alta|Pocos|Baja|Utilitario|
|Media|Muchos|Baja|Deportivo|
|Baja|Pocos|Baja|Deportivo|
|Baja|Muchos|Baja|Deportivo|
|Baja|Muchos|Baja|Utilitario|
|Alta|Muchos|Baja|Utilitario|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|0.50|2|
|Velocidad = Baja → Clase = Deportivo|0.67|3|
|Velocidad = Alta → Clase = Utilitario|1.00|3|



|Reglas con Cilindros (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.67|6|
|Cilindros = Pocos → Clase = Utilitario|0.50|2|



|Reglas con Antigüedad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|1.00|1|
|Antigüedad = Baja → Clase = Utilitario|0.50|6|
|Antigüedad = Alta → Clase = Utilitario|1.00|1|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Alta', 'Baja', 'Baja', 'Baja', 'Baja', 'Baja', 'Baja']


Valores nuevos: [2, 3, 1, 1, 1, 1, 1, 1]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|159|15|2|Utilitario|
|2|147|11|3|Utilitario|
|3|148|2|1|Utilitario|
|4|147|7|1|Deportivo|
|5|135|6|1|Deportivo|
|6|142|7|1|Deportivo|
|7|128|13|1|Utilitario|
|8|176|7|1|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|354|126|2|
|2|45|9|2|
|3|61|121|1|


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
