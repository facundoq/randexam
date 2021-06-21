---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|157|6|Baja|Deportivo|
|2|148|10|Baja|Deportivo|
|3|166|11|Media|Deportivo|
|4|172|15|Alta|Deportivo|
|5|182|8|Baja|Utilitario|
|6|129|3|Baja|Utilitario|
|7|128|11|Baja|Utilitario|
|8|142|3|Alta|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 1, 2, 3, 3, 0, 0, 1]

Intervalos: [[128.0,141.5), [141.5,155.0), [155.0,168.5), [168.5,182.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 1, 2, 3, 3, 0, 0, 1]

Intervalos: [[128,142), [142,157), [157,172), [172,182]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-3.00)/12.00

Valores normalizados: 0.25, 0.58, 0.67, 1.00, 0.42, 0.00, 0.67, 0.00

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Baja → Clase = Deportivo|0.25|0.62|0.40|0.80|
|Clase = Utilitario → Antigüedad = Baja|0.38|0.50|0.75|1.20|
|Velocidad < 153 and Antigüedad = Alta → Cilindros < 8|0.12|0.12|1.00|2.67|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Media|Pocos|Baja|Deportivo|
|Media|Muchos|Baja|Deportivo|
|Alta|Muchos|Media|Deportivo|
|Alta|Muchos|Alta|Deportivo|
|Alta|Pocos|Baja|Utilitario|
|Baja|Pocos|Baja|Utilitario|
|Baja|Muchos|Baja|Utilitario|
|Baja|Pocos|Alta|Utilitario|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Deportivo|1.00|2|
|Velocidad = Baja → Clase = Utilitario|1.00|3|
|Velocidad = Alta → Clase = Deportivo|0.67|3|



|Reglas con Cilindros (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Deportivo|0.75|4|
|Cilindros = Pocos → Clase = Utilitario|0.75|4|



|Reglas con Antigüedad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|1.00|1|
|Antigüedad = Baja → Clase = Utilitario|0.60|5|
|Antigüedad = Alta → Clase = Utilitario|0.50|2|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Baja', 'Media', 'Alta', 'Baja', 'Baja', 'Baja', 'Alta']


Valores nuevos: [1, 1, 2, 3, 1, 1, 1, 3]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|157|6|1|Deportivo|
|2|148|10|1|Deportivo|
|3|166|11|2|Deportivo|
|4|172|15|3|Deportivo|
|5|182|8|1|Utilitario|
|6|129|3|1|Utilitario|
|7|128|11|1|Utilitario|
|8|142|3|3|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|230|110|2|
|2|41|329|1|
|3|585|1|2|


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
