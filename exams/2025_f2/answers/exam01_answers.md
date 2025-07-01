---
title: Minería de Datos usando Sistemas Inteligentes - Tema 3 (Respuestas)
author:  Fecha 2 - 18 de Junio de 2025 

date: 
geometry: margin=1.6cm
---



### 1. Modelo OneR (Puntos: 1)
 
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


Mejor atributo: Nivel


|Reglas con Antigüedad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Antigüedad = Baja → Clase = Inactivo|1.00|3|
|Antigüedad = Alta → Clase = Activo|0.60|5|



|Reglas con Edad (accuracy=0.75)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Edad = Adulta → Clase = Activo|0.67|3|
|Edad = Joven → Clase = Inactivo|0.67|3|
|Edad = Mediana → Clase = Inactivo|1.00|2|



|Reglas con Nivel (accuracy=0.875)|Confianza|Soporte(absoluto)|
|----------|----------|----------|
|Nivel = Alto → Clase = Activo|1.00|1|
|Nivel = Medio → Clase = Activo|0.67|3|
|Nivel = Bajo → Clase = Inactivo|1.00|4|


### 2. Métricas de Reglas (Puntos: 1)
 
|Regla|Soporte|Cobertura|Confianza|Interés|
|----------|----------|----------|----------|----------|
|Nivel = Medio → Clase = Inactivo|0.125|0.375|0.333|0.533|
|Clase = Activo → Nivel = Bajo|0.000|0.375|0.000|0.000|
|Antigüedad < 2 and Nivel = Bajo → Edad < 44|0.250|0.250|1.000|1.600|


### 3. Agrupamiento de datos - Cálculo de asignaciones (Puntos: 1.5)
 
| |d(c1)|d(c2)|Centroide asignado|
|----------|----------|----------|----------|
|1|2|965|1|
|2|905|0|2|
|3|49|1374|1|


### 4. Agrupamiento de datos - Cálculo de centroides (Puntos: 1)
 
| |Antigüedad|Edad|Nivel|Cluster Asignado|
|----------|----------|----------|----------|
|1|2|36|1|
|2|3.5|62|2|


### 5. Ganancia de Información (Puntos: 2)
 Entropías calculadas con logaritmo con base 2

Entropía general: 0.954434002924965


|Atributo|Antigüedad|Nivel|
|----------|----------|----------|
|Entropía|0.49|0.34|
|Ganancia|0.47|0.61|



|Antigüedad: Punto de corte|Entropía|Info Gain|
|----------|----------|----------|
|2|0.61|0.35|
|3.5|0.49|0.47|


### 6. Cuartiles (Puntos: 1)
 Valores ordenados de  Antigüedad:

[1.0, 1.0, 1.0, 3.0, 3.0, 3.0, 4.0, 4.0]

Índices de los cuartiles:

2.25, 4.5, 6.75

Cuartiles:

q1=1.0, q2=3.0, q3=3.75
