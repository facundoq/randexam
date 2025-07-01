---
title: Minería de Datos usando Sistemas Inteligentes - Tema 3
author:  Fecha 2 - 18 de Junio de 2025 

date: 
geometry: margin=1.6cm
---


|Nombres&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Apellidos&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|DNI/N° Legajo&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|#Hojas extra&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
|----------|----------|----------|----------|
|||||


El siguiente conjunto de datos tiene datos de clientes de una empresa y si se encuentran en el estado Activo o Inactivo.

**Tabla de datos**


| |Antigüedad|Edad|Nivel|Clase|
|----------|----------|----------|----------|----------|
|1|1|35|Medio|Inactivo|
|2|3|66|Medio|Activo|
|3|1|29|Bajo|Inactivo|
|4|4|21|Medio|Activo|
|5|3|71|Bajo|Inactivo|
|6|4|53|Alto|Activo|
|7|3|37|Bajo|Inactivo|
|8|1|36|Bajo|Inactivo|


### 1. Modelo OneR
 Dada la siguiente discretización del conjunto de datos original, aplique el algoritmo OneR para encontrar el mejor atributo y las reglas asociadas para clasificar los ejemplos según el atributo Clase. 


|Antigüedad|Edad|Nivel|Clase|
|----------|----------|----------|----------|
|Baja|Joven|Medio|Inactivo|
|Alta|Adulta|Medio|Activo|
|Baja|Joven|Bajo|Inactivo|
|Alta|Joven|Medio|Activo|
|Alta|Adulta|Bajo|Inactivo|
|Alta|Adulta|Alto|Activo|
|Alta|Mediana|Bajo|Inactivo|
|Baja|Mediana|Bajo|Inactivo|


Mostrar el accuracy de cada atributo, y las reglas finales del OneR:


||Antigüedad|Edad|Nivel|
|----------|----------|----------|----------|
|Accuracy||||



|Reglas con [atributo]|
|----------|
|...|


### 2. Métricas de Reglas
 Calcule el soporte, cobertura, confianza, e interés de las siguientes reglas:


|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Nivel = Medio → Clase = Inactivo|||||
|Clase = Activo → Nivel = Bajo|||||
|Antigüedad < 2 and Nivel = Bajo → Edad < 44|||||


Presentar los resultados en forma de tabla, e incluir los cálculos realizados en la hoja.

### 3. Agrupamiento de datos - Cálculo de asignaciones
 Dado el siguiente conjunto de ejemplos numerizado, y dados los centroides **c1** y **c2**, calcule la distancia euclídea de los ejemplos hacia estos centroides, y a cuál de ellos estarían asignados. No utilizar la clase en este ejercicio.


| |Antigüedad|Edad|Nivel|Clase|
|----------|----------|----------|----------|----------|
|1|1|35|2|Inactivo|
|2|3|66|2|Activo|
|3|1|29|1|Inactivo|



|Centroide|Antigüedad|Edad|Nivel|
|----------|----------|----------|----------|
|**c1**|1|36|1|
|**c2**|3|66|2|


Nota: Para presentar los resultados, no calcule las raíces cuadradas. En lugar de eso, deje expresadas las distancias como $\sqrt{valor}$. Utilice una tabla como la siguiente:


|Ejemplo|d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|$\sqrt{valor}$|$\sqrt{valor}$|(c1 o c2)|
|...|...|...|...|


### 4. Agrupamiento de datos - Cálculo de centroides
 Dado el siguiente conjunto de ejemplos numerizado, calcule los valores de los 2 centroides numerados desde 0 hasta 1 usando la asignación provista. No utilizar la clase en este ejercicio. Este ejercicio es independiente del resto del examen. Utilice una tabla con 2 filas y tantas columnas como atributos haya para presentar los centroides resultantes.


| |Antigüedad|Edad|Nivel|Cluster Asignado|
|----------|----------|----------|----------|----------|
|1|3|71|1|1|
|2|4|53|3|1|
|3|3|37|1|0|
|4|1|36|1|0|


### 5. Ganancia de Información
 Utilizando los datos originales, calcule la entropía general del conjunto de datos en base al atributo de clase. Luego, calcule la entropía y ganancia de información para los atributos Antigüedad y Nivel. Tenga en cuenta que para los atributos numéricos deberá utilizar la variante del algoritmo que busca la mejor discretización probando todos los puntos de corte posibles. Utilice la siguiente tabla para presentar los resultados:


|Atributo|Antigüedad|Nivel|
|----------|----------|----------|
|Entropía| | |
|Ganancia de Información| | |


En base a estos valores, indique cuál de los 2 atributos se elegiría para generar la raíz de un árbol de decisión.
Utilice dos decimales para los cálculos. 
Utilice logaritmo con base 2 para todos los cálculos (obligatorio).

Logaritmos de base 2


| | | | | | | | |
|----------|----------|----------|----------|----------|----------|----------|----------|
|$log_{2}(1/2)$|$log_{2}(1/3)$|$log_{2}(2/3)$|$log_{2}(1/4)$|$log_{2}(2/4)$|$log_{2}(3/4)$|$log_{2}(1/5)$|$log_{2}(2/5)$|
|-1.000|-1.585|-0.585|-2.000|-1.000|-0.415|-2.322|-1.322|
|$log_{2}(3/5)$|$log_{2}(4/5)$|$log_{2}(1/6)$|$log_{2}(2/6)$|$log_{2}(3/6)$|$log_{2}(4/6)$|$log_{2}(5/6)$|$log_{2}(1/7)$|
|-0.737|-0.322|-2.585|-1.585|-1.000|-0.585|-0.263|-2.807|
|$log_{2}(2/7)$|$log_{2}(3/7)$|$log_{2}(4/7)$|$log_{2}(5/7)$|$log_{2}(6/7)$|$log_{2}(1/8)$|$log_{2}(2/8)$|$log_{2}(3/8)$|
|-1.807|-1.222|-0.807|-0.485|-0.222|-3.000|-2.000|-1.415|
|$log_{2}(4/8)$|$log_{2}(5/8)$|$log_{2}(6/8)$|$log_{2}(7/8)$|
|-1.000|-0.678|-0.415|-0.193|


### 6. Cuartiles
 Calcule la mediana y los dos cuartiles del atributo Antigüedad.

 Nota: Utilice la definición de cuartil vista en la teoría.
