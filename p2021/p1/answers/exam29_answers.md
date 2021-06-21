---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|131|4|Alta|Utilitario|
|2|186|9|Alta|Deportivo|
|3|141|4|Baja|Utilitario|
|4|147|7|Media|Utilitario|
|5|139|5|Baja|Deportivo|
|6|146|13|Alta|Utilitario|
|7|153|3|Baja|Deportivo|
|8|153|8|Media|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 3, 0, 1, 0, 1, 1, 1]

Intervalos: [[131.0,144.75), [144.75,158.5), [158.5,172.25), [172.25,186.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 3, 1, 2, 0, 1, 3, 3]

Intervalos: [[131,141), [141,147), [147,153), [153,186]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-3.00)/10.00

Valores normalizados: 0.10, 0.60, 0.10, 0.40, 0.20, 1.00, 0.00, 0.50

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.25|0.25|1.00|1.60|
|Clase = Utilitario → Antigüedad = Media|0.25|0.62|0.40|1.60|
|Velocidad < 150 and Antigüedad = Alta → Cilindros < 7|0.12|0.25|0.50|1.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Baja|Pocos|Alta|Utilitario|
|Alta|Muchos|Alta|Deportivo|
|Baja|Pocos|Baja|Utilitario|
|Media|Muchos|Media|Utilitario|
|Baja|Pocos|Baja|Deportivo|
|Media|Muchos|Alta|Utilitario|
|Alta|Pocos|Baja|Deportivo|
|Alta|Muchos|Media|Utilitario|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|1.00|2|
|Velocidad = Baja → Clase = Utilitario|0.67|3|
|Velocidad = Alta → Clase = Deportivo|0.67|3|



|Reglas con Cilindros (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.75|4|
|Cilindros = Pocos → Clase = Utilitario|0.50|4|



|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|1.00|2|
|Antigüedad = Baja → Clase = Deportivo|0.67|3|
|Antigüedad = Alta → Clase = Utilitario|0.67|3|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Alta', 'Baja', 'Media', 'Baja', 'Alta', 'Baja', 'Media']


Valores nuevos: [3, 3, 1, 2, 1, 3, 1, 2]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|131|4|3|Utilitario|
|2|186|9|3|Deportivo|
|3|141|4|1|Utilitario|
|4|147|7|2|Utilitario|
|5|139|5|1|Deportivo|
|6|146|13|3|Utilitario|
|7|153|3|1|Deportivo|
|8|153|8|2|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|105|510|1|
|2|2045|1090|2|
|3|1|170|1|


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
