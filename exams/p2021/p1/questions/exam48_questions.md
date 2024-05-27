---
title: Minería de Datos usando Sistemas Inteligentes
author: Primera Fecha - 17 de Junio de 2021 - Promoción
date: 
geometry: margin=2cm
---

**Tabla de datos**


|Fila|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|----------|
|1|182|4|Baja|Utilitario|
|2|138|5|Baja|Deportivo|
|3|123|11|Baja|Deportivo|
|4|160|5|Alta|Deportivo|
|5|162|10|Alta|Utilitario|
|6|150|8|Media|Deportivo|
|7|126|14|Baja|Utilitario|
|8|143|15|Alta|Deportivo|


### 1. Discretización de atributos
 Discretice el atributo Velocidad  por a) frecuencia y b) rango en 4 valores. En ambos casos, indique los intervalos resultantes. Realice un gráfico de barras para visualizar la frecuencia de los valores resultantes.

 Nota: La discretización es solo para este ejercicio; utilizar los datos originales en los siguientes.

### 2. Normalización de atributos
 Normalice el atributo Cilindros mediante: 

1. rango lineal uniforme (min/max)


Indicar los valores resultantes normalizados. 
 Nota: La normalización es solo para este ejercicio. Utilizar los datos originales en los siguientes.

### 3. Métricas de Reglas
 Calcule el soporte, cobertura, confianza, e interés de las siguientes reglas:


|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Antigüedad = Media → Clase = Utilitario|||||
|Clase = Deportivo → Antigüedad = Alta|||||
|Velocidad < 148 and Antigüedad = Alta → Cilindros < 9|||||


Presentar los resultados en forma de tabla, e incluir los cálculos realizados en la hoja.

### 4. Modelo OneR
 Dada la siguiente discretización del conjunto de datos original, aplique el algoritmo OneR para encontrar el mejor atributo y las reglas asociadas para clasificar los ejemplos según el atributo Clase. 


|Velocidad|Cilindros|Antigüedad|Clase|
|----------|----------|----------|----------|
|Alta|Pocos|Baja|Utilitario|
|Baja|Pocos|Baja|Deportivo|
|Baja|Muchos|Baja|Deportivo|
|Alta|Pocos|Alta|Deportivo|
|Alta|Muchos|Alta|Utilitario|
|Media|Pocos|Media|Deportivo|
|Baja|Muchos|Baja|Utilitario|
|Media|Muchos|Alta|Deportivo|


Mostrar el accuracy de cada atributo, y las reglas finales del OneR:


||Velocidad|Cilindros|Antigüedad|
|----------|----------|----------|----------|
|Accuracy||||



|Reglas con [atributo]|
|----------|
|...|


### 5. Numerización de datos
 Numerizar el atributo **Antigüedad** del conjunto de datos original. Utilizar la estrategia de generar un valor entero por cada valor numérico. Comenzar con el valor 1, y respetar el orden natural de dicho atributo, de menor a mayor. Mostrar los valores resultantes.

### 6. Agrupamiento de datos
 Utilizando la numerización de datos generada anteriormente, y dados los centroides **c1** y **c2**, calcule la distancia euclídea de los 3 primeros ejemplos hacia estos centroides, y a cuál de ellos estarían asignados. No utilizar la clase en este ejercicio.


|Centroide|Velocidad|Cilindros|Antigüedad|
|----------|----------|----------|----------|
|**c1**|138|8|1|
|**c2**|160|14|3|


Nota: Para presentar los resultados, no calcule las raíces cuadradas. En lugar de eso, deje expresada los distancias como $\sqrt{valor}$. Utilice una tabla como la siguiente:


|Ejemplo|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|$\sqrt{valor}$|$\sqrt{valor}$|(c1 o c2)|
|...|...|...|...|


### 7. Conceptos de Agrupamientos
 Indique verdadero (V) o falso (F) para las siguientes preguntas. **Justifique** su respuesta.

a) El indice Silhouette es superior a Davies Bouldin ya que considera distancias inter e intra cluster.

b) Es preciso conocer la posición de los centros para calcular el índice Davies-Bouldin del agrupamiento

c) En el índice Silhouette, el clustering es perfecto cuando vale 0, y los valores extremos -1 y 1 indican desviaciones negativas y positivas del óptimo.

d) El índice Silhouette siempre mejora a medida que se aumenta el número de clusters k

### 8. Matriz de Correlación
 Dada la siguiente matriz de correlación, indique la verdad (V) o falsedad (F) de las afirmaciones:


| |Desarrollo|Contaminación|Calidad de Vida|Población|
|----------|----------|----------|----------|----------|
|Desarrollo|1|-0.25|0.88|0.0001|
|Contaminación|-0.25|1|0.75|-0.72|
|Calidad de Vida|0.88|0.75|1|0.12|
|Población|0.0001|-0.72|0.12|1|


a) Los atributos Desarrollo y Población son aproximadamente independientes.
b) Es probable que si sube el Desarrollo, también suba la Calidad de Vida.
c) Los atributos Desarrollo y Contaminación están correlacionados linealmente, y la correlación es **Débil**.
d) Los atributos Población y Contaminación están correlacionados linealmente, y la correlación es **Débil**.
e) La mayoría de los pares de atributos no están correlacionados linealmente.

### 9. Conceptos de Minería de Datos
 Indique el valor de verdad de a las siguientes afirmaciones. Justifique sus respuestas.

a) Es posible calcular la mediana de un atributo ordinal

b) El valor de la Ganancia de Información (Information Gain) de un
atributo que toma siempre el mismo valor en todos los ejemplos es cero.

c) Si se busca construir un árbol de clasificación, el atributo de clase (marcado como label) debe ser de tipo ordinal.

d) No es posible calcular la Tasa de Ganancia (Gain Ratio) de un atributo numérico continuo (con decimales).

e) Es posible que al representar el diagrama de barras de un atributo discretizado por frecuencia se observen barras con alturas diferentes.

f)  Un atributo nominal puede tener 2 modas.

g) Es posible calcular la tasa de acierto (accuracy) de un conjunto de reglas de asociación utilizando una matriz de confusión.
