---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|132|2|Media|Deportivo|
|2|162|4|Media|Utilitario|
|3|147|10|Baja|Deportivo|
|4|140|13|Alta|Deportivo|
|5|131|6|Baja|Utilitario|
|6|158|14|Media|Utilitario|
|7|161|10|Media|Utilitario|
|8|140|2|Media|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 3, 2, 1, 0, 3, 3, 1]

Intervalos: [[131.0,138.75), [138.75,146.5), [146.5,154.25), [154.25,162.0]]

Resultado de la discretización por frecuencia:

Valores: [0, 3, 2, 1, 0, 2, 3, 1]

Intervalos: [[131,140), [140,147), [147,161), [161,162]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-2.00)/12.00

Valores normalizados: 0.00, 0.17, 0.67, 0.92, 0.33, 1.00, 0.67, 0.00

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|0.12|0.62|0.20|0.53|
|Clase = Deportivo → Antigüedad = Media|0.12|0.38|0.33|0.53|
|Velocidad < 146 and Antigüedad = Alta → Cilindros < 8|0.00|0.12|0.00|0.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Baja|Pocos|Media|Deportivo|
|Alta|Pocos|Media|Utilitario|
|Media|Muchos|Baja|Deportivo|
|Media|Muchos|Alta|Deportivo|
|Baja|Pocos|Baja|Utilitario|
|Alta|Muchos|Media|Utilitario|
|Alta|Muchos|Media|Utilitario|
|Media|Pocos|Media|Utilitario|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Deportivo|0.67|3|
|Velocidad = Baja → Clase = Utilitario|0.50|2|
|Velocidad = Alta → Clase = Utilitario|1.00|3|



|Reglas con Cilindros (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.50|4|
|Cilindros = Pocos → Clase = Utilitario|0.75|4|



|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.80|5|
|Antigüedad = Baja → Clase = Utilitario|0.50|2|
|Antigüedad = Alta → Clase = Deportivo|1.00|1|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Media', 'Baja', 'Alta', 'Baja', 'Media', 'Media', 'Media']


Valores nuevos: [2, 2, 1, 3, 1, 2, 2, 2]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|132|2|2|Deportivo|
|2|162|4|2|Utilitario|
|3|147|10|1|Deportivo|
|4|140|13|3|Deportivo|
|5|131|6|1|Utilitario|
|6|158|14|2|Utilitario|
|7|161|10|2|Utilitario|
|8|140|2|2|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|81|798|1|
|2|489|98|2|
|3|65|134|1|


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
