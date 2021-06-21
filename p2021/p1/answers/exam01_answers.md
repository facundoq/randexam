---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|174|4|Alta|Deportivo|
|2|140|6|Baja|Utilitario|
|3|142|14|Media|Utilitario|
|4|133|12|Media|Deportivo|
|5|162|3|Media|Deportivo|
|6|115|15|Media|Utilitario|
|7|176|11|Baja|Utilitario|
|8|138|6|Alta|Deportivo|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [3, 1, 1, 1, 3, 0, 3, 1]

Intervalos: [[115.0,130.25), [130.25,145.5), [145.5,160.75), [160.75,176.0]]

Resultado de la discretización por frecuencia:

Valores: [3, 1, 2, 0, 2, 0, 3, 1]

Intervalos: [[115,138), [138,142), [142,174), [174,176]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-3.00)/12.00

Valores normalizados: 0.08, 0.25, 0.92, 0.75, 0.00, 1.00, 0.67, 0.25

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Alta → Clase = Utilitario|0.00|0.25|0.00|0.00|
|Clase = Deportivo → Antigüedad = Media|0.25|0.50|0.50|1.00|
|Velocidad < 148 and Antigüedad = Media → Cilindros < 9|0.00|0.38|0.00|0.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Alta|Pocos|Alta|Deportivo|
|Media|Pocos|Baja|Utilitario|
|Media|Muchos|Media|Utilitario|
|Baja|Muchos|Media|Deportivo|
|Alta|Pocos|Media|Deportivo|
|Baja|Muchos|Media|Utilitario|
|Alta|Muchos|Baja|Utilitario|
|Baja|Pocos|Alta|Deportivo|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|1.00|2|
|Velocidad = Baja → Clase = Deportivo|0.67|3|
|Velocidad = Alta → Clase = Deportivo|0.67|3|



|Reglas con Cilindros (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.75|4|
|Cilindros = Pocos → Clase = Deportivo|0.75|4|



|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.50|4|
|Antigüedad = Baja → Clase = Utilitario|1.00|2|
|Antigüedad = Alta → Clase = Deportivo|1.00|2|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Baja', 'Media', 'Media', 'Media', 'Media', 'Baja', 'Alta']


Valores nuevos: [3, 1, 2, 2, 2, 2, 1, 3]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|174|4|3|Deportivo|
|2|140|6|1|Utilitario|
|3|142|14|2|Utilitario|
|4|133|12|2|Deportivo|
|5|162|3|2|Deportivo|
|6|115|15|2|Utilitario|
|7|176|11|1|Utilitario|
|8|138|6|3|Deportivo|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|1301|245|2|
|2|5|549|1|
|3|80|400|1|


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
