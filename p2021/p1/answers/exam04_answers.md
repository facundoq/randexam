---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|163|15|Media|Utilitario|
|2|139|9|Alta|Deportivo|
|3|148|9|Baja|Utilitario|
|4|135|13|Alta|Utilitario|
|5|145|12|Baja|Deportivo|
|6|157|10|Baja|Deportivo|
|7|139|14|Baja|Deportivo|
|8|144|8|Alta|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [3, 0, 1, 0, 1, 3, 0, 1]

Intervalos: [[135.0,142.0), [142.0,149.0), [149.0,156.0), [156.0,163.0]]

Resultado de la discretización por frecuencia:

Valores: [3, 1, 2, 0, 2, 3, 1, 1]

Intervalos: [[135,139), [139,145), [145,157), [157,163]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-8.00)/7.00

Valores normalizados: 1.00, 0.14, 0.14, 0.71, 0.57, 0.29, 0.86, 0.00

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Alta → Clase = Deportivo|0.12|0.38|0.33|0.67|
|Clase = Deportivo → Antigüedad = Baja|0.38|0.50|0.75|1.50|
|Velocidad < 146 and Antigüedad = Alta → Cilindros < 11|0.25|0.38|0.67|1.33|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Alta|Muchos|Media|Utilitario|
|Baja|Pocos|Alta|Deportivo|
|Alta|Pocos|Baja|Utilitario|
|Baja|Muchos|Alta|Utilitario|
|Media|Muchos|Baja|Deportivo|
|Alta|Pocos|Baja|Deportivo|
|Baja|Muchos|Baja|Deportivo|
|Media|Pocos|Alta|Utilitario|


Mejor atributo: Antigüedad


|Reglas con Velocidad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|0.50|2|
|Velocidad = Baja → Clase = Deportivo|0.67|3|
|Velocidad = Alta → Clase = Utilitario|0.67|3|



|Reglas con Cilindros (accuracy=0.5)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.50|4|
|Cilindros = Pocos → Clase = Utilitario|0.50|4|



|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|1.00|1|
|Antigüedad = Baja → Clase = Deportivo|0.75|4|
|Antigüedad = Alta → Clase = Utilitario|0.67|3|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Alta', 'Baja', 'Alta', 'Baja', 'Baja', 'Baja', 'Alta']


Valores nuevos: [2, 3, 1, 3, 1, 1, 1, 3]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|163|15|2|Utilitario|
|2|139|9|3|Deportivo|
|3|148|9|1|Utilitario|
|4|135|13|3|Utilitario|
|5|145|12|1|Deportivo|
|6|157|10|1|Deportivo|
|7|139|14|1|Deportivo|
|8|144|8|3|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|602|227|2|
|2|5|106|1|
|3|82|29|2|


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
