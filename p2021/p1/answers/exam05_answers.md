---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|139|10|Alta|Deportivo|
|2|137|8|Alta|Deportivo|
|3|139|10|Alta|Deportivo|
|4|149|8|Baja|Utilitario|
|5|133|15|Media|Deportivo|
|6|153|10|Media|Utilitario|
|7|174|15|Media|Utilitario|
|8|161|7|Baja|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 0, 0, 1, 0, 1, 3, 2]

Intervalos: [[133.0,143.25), [143.25,153.5), [153.5,163.75), [163.75,174.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 0, 1, 2, 0, 2, 3, 3]

Intervalos: [[133,139), [139,149), [149,161), [161,174]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-7.00)/8.00

Valores normalizados: 0.38, 0.12, 0.38, 0.12, 1.00, 0.38, 1.00, 0.00

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Baja → Clase = Utilitario|0.25|0.25|1.00|2.00|
|Clase = Utilitario → Antigüedad = Alta|0.00|0.50|0.00|0.00|
|Velocidad < 148 and Antigüedad = Media → Cilindros < 10|0.00|0.12|0.00|0.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Media|Muchos|Alta|Deportivo|
|Baja|Pocos|Alta|Deportivo|
|Media|Muchos|Alta|Deportivo|
|Media|Pocos|Baja|Utilitario|
|Baja|Muchos|Media|Deportivo|
|Alta|Muchos|Media|Utilitario|
|Alta|Muchos|Media|Utilitario|
|Alta|Pocos|Baja|Utilitario|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Deportivo|0.67|3|
|Velocidad = Baja → Clase = Deportivo|1.00|2|
|Velocidad = Alta → Clase = Utilitario|1.00|3|



|Reglas con Cilindros (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Deportivo|0.60|5|
|Cilindros = Pocos → Clase = Utilitario|0.67|3|



|Reglas con Antigüedad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.67|3|
|Antigüedad = Baja → Clase = Utilitario|1.00|2|
|Antigüedad = Alta → Clase = Deportivo|1.00|3|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Alta', 'Alta', 'Baja', 'Media', 'Media', 'Media', 'Baja']


Valores nuevos: [3, 3, 3, 1, 2, 2, 2, 1]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|139|10|3|Deportivo|
|2|137|8|3|Deportivo|
|3|139|10|3|Deportivo|
|4|149|8|1|Utilitario|
|5|133|15|2|Deportivo|
|6|153|10|2|Utilitario|
|7|174|15|2|Utilitario|
|8|161|7|1|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|0|225|1|
|2|8|309|1|
|3|0|225|1|


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
