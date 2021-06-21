---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|161|2|Media|Deportivo|
|2|163|13|Media|Utilitario|
|3|136|13|Baja|Utilitario|
|4|136|14|Media|Deportivo|
|5|128|15|Alta|Utilitario|
|6|168|3|Media|Deportivo|
|7|146|10|Alta|Deportivo|
|8|170|7|Media|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [3, 3, 0, 0, 0, 3, 1, 3]

Intervalos: [[128.0,138.5), [138.5,149.0), [149.0,159.5), [159.5,170.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 2, 1, 1, 0, 3, 1, 3]

Intervalos: [[128,136), [136,161), [161,168), [168,170]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-2.00)/13.00

Valores normalizados: 0.00, 0.85, 0.85, 0.92, 1.00, 0.08, 0.62, 0.38

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Alta → Clase = Deportivo|0.12|0.25|0.50|1.00|
|Clase = Utilitario → Antigüedad = Media|0.25|0.50|0.50|0.80|
|Velocidad < 151 and Antigüedad = Alta → Cilindros < 10|0.00|0.25|0.00|0.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Media|Pocos|Media|Deportivo|
|Alta|Muchos|Media|Utilitario|
|Baja|Muchos|Baja|Utilitario|
|Baja|Muchos|Media|Deportivo|
|Baja|Muchos|Alta|Utilitario|
|Alta|Pocos|Media|Deportivo|
|Media|Pocos|Alta|Deportivo|
|Alta|Pocos|Media|Utilitario|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Deportivo|1.00|2|
|Velocidad = Baja → Clase = Utilitario|0.67|3|
|Velocidad = Alta → Clase = Utilitario|0.67|3|



|Reglas con Cilindros (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.75|4|
|Cilindros = Pocos → Clase = Deportivo|0.75|4|



|Reglas con Antigüedad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|0.60|5|
|Antigüedad = Baja → Clase = Utilitario|1.00|1|
|Antigüedad = Alta → Clase = Utilitario|0.50|2|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Media', 'Baja', 'Media', 'Alta', 'Media', 'Alta', 'Media']


Valores nuevos: [2, 2, 1, 2, 3, 2, 3, 2]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|161|2|2|Deportivo|
|2|163|13|2|Utilitario|
|3|136|13|1|Utilitario|
|4|136|14|2|Deportivo|
|5|128|15|3|Utilitario|
|6|168|3|2|Deportivo|
|7|146|10|3|Deportivo|
|8|170|7|2|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|690|148|2|
|2|739|1|2|
|3|9|731|1|


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
