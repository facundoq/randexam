---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|133|13|Baja|Deportivo|
|2|179|8|Alta|Utilitario|
|3|145|11|Media|Deportivo|
|4|129|10|Baja|Deportivo|
|5|166|7|Media|Deportivo|
|6|141|3|Alta|Utilitario|
|7|131|9|Alta|Deportivo|
|8|163|4|Media|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [0, 3, 1, 0, 2, 0, 0, 2]

Intervalos: [[129.0,141.5), [141.5,154.0), [154.0,166.5), [166.5,179.0]]

Resultado de la discretización por frecuencia:

Valores: [1, 3, 2, 0, 3, 1, 0, 2]

Intervalos: [[129,133), [133,145), [145,166), [166,179]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-3.00)/10.00

Valores normalizados: 1.00, 0.50, 0.80, 0.70, 0.40, 0.00, 0.60, 0.10

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Baja → Clase = Utilitario|0.00|0.25|0.00|0.00|
|Clase = Deportivo → Antigüedad = Alta|0.12|0.62|0.20|0.53|
|Velocidad < 148 and Antigüedad = Baja → Cilindros < 8|0.00|0.25|0.00|0.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Baja|Muchos|Baja|Deportivo|
|Alta|Pocos|Alta|Utilitario|
|Media|Muchos|Media|Deportivo|
|Baja|Muchos|Baja|Deportivo|
|Alta|Pocos|Media|Deportivo|
|Media|Pocos|Alta|Utilitario|
|Baja|Muchos|Alta|Deportivo|
|Alta|Pocos|Media|Utilitario|


Mejor atributo: Cilindros


|Reglas con Velocidad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|0.50|2|
|Velocidad = Baja → Clase = Deportivo|1.00|3|
|Velocidad = Alta → Clase = Utilitario|0.67|3|



|Reglas con Cilindros (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Deportivo|1.00|4|
|Cilindros = Pocos → Clase = Utilitario|0.75|4|



|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|0.67|3|
|Antigüedad = Baja → Clase = Deportivo|1.00|2|
|Antigüedad = Alta → Clase = Utilitario|0.67|3|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Alta', 'Media', 'Baja', 'Media', 'Alta', 'Alta', 'Media']


Valores nuevos: [1, 3, 2, 1, 2, 3, 3, 2]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|133|13|1|Deportivo|
|2|179|8|3|Utilitario|
|3|145|11|2|Deportivo|
|4|129|10|1|Deportivo|
|5|166|7|2|Deportivo|
|6|141|3|3|Utilitario|
|7|131|9|3|Deportivo|
|8|163|4|2|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|26|904|1|
|2|2117|269|2|
|3|153|325|1|


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
