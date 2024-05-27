---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|119|13|Alta|Utilitario|
|2|120|7|Media|Deportivo|
|3|112|13|Media|Utilitario|
|4|118|13|Media|Deportivo|
|5|143|3|Baja|Deportivo|
|6|169|4|Baja|Deportivo|
|7|143|3|Media|Deportivo|
|8|154|9|Baja|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 0, 0, 0, 2, 3, 2, 2]

Intervalos: [[112.0,126.25), [126.25,140.5), [140.5,154.75), [154.75,169.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 1, 0, 0, 2, 3, 2, 3]

Intervalos: [[112,119), [119,143), [143,154), [154,169]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-3.00)/10.00

Valores normalizados: 1.00, 0.40, 1.00, 1.00, 0.00, 0.10, 0.00, 0.60

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Alta → Clase = Utilitario|0.12|0.12|1.00|2.67|
|Clase = Utilitario → Antigüedad = Media|0.12|0.38|0.33|0.67|
|Velocidad < 135 and Antigüedad = Baja → Cilindros < 8|0.00|0.00|1.00|inf|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Baja|Muchos|Alta|Utilitario|
|Media|Pocos|Media|Deportivo|
|Baja|Muchos|Media|Utilitario|
|Baja|Muchos|Media|Deportivo|
|Alta|Pocos|Baja|Deportivo|
|Alta|Pocos|Baja|Deportivo|
|Alta|Pocos|Media|Deportivo|
|Alta|Muchos|Baja|Utilitario|


Mejor atributo: Cilindros


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Deportivo|1.00|1|
|Velocidad = Baja → Clase = Utilitario|0.67|3|
|Velocidad = Alta → Clase = Deportivo|0.75|4|



|Reglas con Cilindros (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Utilitario|0.75|4|
|Cilindros = Pocos → Clase = Deportivo|1.00|4|



|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|0.75|4|
|Antigüedad = Baja → Clase = Deportivo|0.67|3|
|Antigüedad = Alta → Clase = Utilitario|1.00|1|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Alta', 'Media', 'Media', 'Media', 'Baja', 'Baja', 'Media', 'Baja']


Valores nuevos: [3, 2, 2, 2, 1, 1, 2, 1]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|119|13|3|Utilitario|
|2|120|7|2|Deportivo|
|3|112|13|2|Utilitario|
|4|118|13|2|Deportivo|
|5|143|3|1|Deportivo|
|6|169|4|1|Deportivo|
|7|143|3|2|Deportivo|
|8|154|9|1|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|37|577|1|
|2|1|565|1|
|3|85|961|1|


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
