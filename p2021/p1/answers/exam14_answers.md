---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|133|8|Baja|Deportivo|
|2|152|7|Alta|Utilitario|
|3|161|3|Media|Deportivo|
|4|135|14|Alta|Utilitario|
|5|146|12|Media|Utilitario|
|6|150|4|Alta|Deportivo|
|7|129|6|Baja|Deportivo|
|8|154|7|Baja|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 2, 3, 0, 2, 2, 0, 3]

Intervalos: [[129.0,137.0), [137.0,145.0), [145.0,153.0), [153.0,161.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 2, 3, 1, 1, 2, 0, 3]

Intervalos: [[129,135), [135,150), [150,154), [154,161]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-3.00)/11.00

Valores normalizados: 0.45, 0.36, 0.00, 1.00, 0.82, 0.09, 0.27, 0.36

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|0.12|0.25|0.50|1.00|
|Clase = Utilitario → Antigüedad = Alta|0.25|0.50|0.50|1.33|
|Velocidad < 145 and Antigüedad = Alta → Cilindros < 8|0.00|0.12|0.00|0.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Baja|Muchos|Baja|Deportivo|
|Alta|Muchos|Alta|Utilitario|
|Alta|Pocos|Media|Deportivo|
|Baja|Muchos|Alta|Utilitario|
|Media|Muchos|Media|Utilitario|
|Media|Pocos|Alta|Deportivo|
|Baja|Pocos|Baja|Deportivo|
|Alta|Muchos|Baja|Utilitario|


Mejor atributo: Cilindros


|Reglas con Velocidad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|0.50|2|
|Velocidad = Baja → Clase = Deportivo|0.67|3|
|Velocidad = Alta → Clase = Utilitario|0.67|3|



|Reglas con Cilindros (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.80|5|
|Cilindros = Pocos → Clase = Deportivo|1.00|3|



|Reglas con Antigüedad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.50|2|
|Antigüedad = Baja → Clase = Deportivo|0.67|3|
|Antigüedad = Alta → Clase = Utilitario|0.67|3|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Alta', 'Media', 'Alta', 'Media', 'Alta', 'Baja', 'Baja']


Valores nuevos: [1, 3, 2, 3, 2, 3, 1, 1]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|133|8|1|Deportivo|
|2|152|7|3|Utilitario|
|3|161|3|2|Deportivo|
|4|135|14|3|Utilitario|
|5|146|12|2|Utilitario|
|6|150|4|3|Deportivo|
|7|129|6|1|Deportivo|
|8|154|7|1|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|6|381|1|
|2|290|25|2|
|3|692|163|2|


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
