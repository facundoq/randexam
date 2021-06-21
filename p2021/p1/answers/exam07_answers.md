---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|151|6|Media|Utilitario|
|2|159|9|Media|Deportivo|
|3|154|2|Media|Utilitario|
|4|144|7|Media|Deportivo|
|5|132|6|Baja|Utilitario|
|6|144|13|Alta|Deportivo|
|7|146|11|Media|Deportivo|
|8|158|5|Baja|Utilitario|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [2, 3, 3, 1, 0, 1, 2, 3]

Intervalos: [[132.0,138.75), [138.75,145.5), [145.5,152.25), [152.25,159.0]]

Resultado de la discretización por frecuencia:

Valores: [2, 3, 2, 1, 0, 1, 1, 3]

Intervalos: [[132,144), [144,151), [151,158), [158,159]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-2.00)/11.00

Valores normalizados: 0.36, 0.64, 0.00, 0.45, 0.36, 1.00, 0.82, 0.27

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|0.25|0.62|0.40|0.80|
|Clase = Utilitario → Antigüedad = Baja|0.25|0.50|0.50|2.00|
|Velocidad < 148 and Antigüedad = Alta → Cilindros < 7|0.00|0.12|0.00|0.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Media|Pocos|Media|Utilitario|
|Alta|Muchos|Media|Deportivo|
|Alta|Pocos|Media|Utilitario|
|Baja|Muchos|Media|Deportivo|
|Baja|Pocos|Baja|Utilitario|
|Baja|Muchos|Alta|Deportivo|
|Media|Muchos|Media|Deportivo|
|Alta|Pocos|Baja|Utilitario|


Mejor atributo: Cilindros


|Reglas con Velocidad (accuracy=0.625)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Utilitario|0.50|2|
|Velocidad = Baja → Clase = Deportivo|0.67|3|
|Velocidad = Alta → Clase = Utilitario|0.67|3|



|Reglas con Cilindros (accuracy=1.0)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Deportivo|1.00|4|
|Cilindros = Pocos → Clase = Utilitario|1.00|4|



|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|0.60|5|
|Antigüedad = Baja → Clase = Utilitario|1.00|2|
|Antigüedad = Alta → Clase = Deportivo|1.00|1|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Media', 'Media', 'Media', 'Media', 'Baja', 'Alta', 'Media', 'Baja']


Valores nuevos: [2, 2, 2, 2, 1, 3, 2, 1]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|151|6|2|Utilitario|
|2|159|9|2|Deportivo|
|3|154|2|2|Utilitario|
|4|144|7|2|Deportivo|
|5|132|6|1|Utilitario|
|6|144|13|3|Deportivo|
|7|146|11|2|Deportivo|
|8|158|5|1|Utilitario|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|49|34|2|
|2|234|29|2|
|3|116|81|2|


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
