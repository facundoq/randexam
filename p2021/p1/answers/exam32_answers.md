---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|177|6|Baja|Deportivo|
|2|130|9|Alta|Utilitario|
|3|144|2|Baja|Deportivo|
|4|146|10|Baja|Deportivo|
|5|108|6|Baja|Utilitario|
|6|179|3|Baja|Deportivo|
|7|155|9|Alta|Deportivo|
|8|134|13|Media|Deportivo|


### 1. Discretización de atributos (puntos: 1)
 Resultado de la discretización por rango:

Valores: [3, 1, 2, 2, 0, 3, 2, 1]

Intervalos: [[108.0,125.75), [125.75,143.5), [143.5,161.25), [161.25,179.0]]

Resultado de la discretización por frecuencia:

Valores: [3, 0, 1, 2, 0, 3, 2, 1]

Intervalos: [[108,134), [134,146), [146,177), [177,179]]

### 2. Normalización de atributos (puntos: 1)
 Normalización rango con transformación (x-2.00)/11.00

Valores normalizados: 0.36, 0.64, 0.00, 0.73, 0.36, 0.09, 0.64, 1.00

### 3. Métricas de Reglas (puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Alta → Clase = Deportivo|0.12|0.25|0.50|0.67|
|Clase = Deportivo → Antigüedad = Baja|0.50|0.75|0.67|1.07|
|Velocidad < 147 and Antigüedad = Alta → Cilindros < 7|0.00|0.12|0.00|0.00|


### 4. Modelo OneR (puntos: 1)
 
|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Alta|Pocos|Baja|Deportivo|
|Baja|Muchos|Alta|Utilitario|
|Media|Pocos|Baja|Deportivo|
|Media|Muchos|Baja|Deportivo|
|Baja|Pocos|Baja|Utilitario|
|Alta|Pocos|Baja|Deportivo|
|Alta|Muchos|Alta|Deportivo|
|Baja|Muchos|Media|Deportivo|


Mejor atributo: Velocidad


|Reglas con Velocidad (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Velocidad = Media → Clase = Deportivo|1.00|2|
|Velocidad = Baja → Clase = Utilitario|0.67|3|
|Velocidad = Alta → Clase = Deportivo|1.00|3|



|Reglas con Cilindros (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Cilindros = Muchos → Clase = Deportivo|0.75|4|
|Cilindros = Pocos → Clase = Deportivo|0.75|4|



|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Media → Clase = Deportivo|1.00|1|
|Antigüedad = Baja → Clase = Deportivo|0.80|5|
|Antigüedad = Alta → Clase = Utilitario|0.50|2|


### 5. Numerización de datos (puntos: 1)
 Valores originales: ['Baja', 'Alta', 'Baja', 'Baja', 'Baja', 'Baja', 'Alta', 'Media']


Valores nuevos: [1, 3, 1, 1, 1, 1, 3, 2]



|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|177|6|1|Deportivo|
|2|130|9|3|Utilitario|
|3|144|2|1|Deportivo|
|4|146|10|1|Deportivo|
|5|108|6|1|Utilitario|
|6|179|3|1|Deportivo|
|7|155|9|3|Deportivo|
|8|134|13|2|Deportivo|


### 6. Agrupamiento de datos (puntos: 1)
 
|Fila|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|1849|500|2|
|2|29|630|1|
|3|116|185|1|


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
