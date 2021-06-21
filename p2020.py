from tqdm import tqdm
import copy
# TODO
# Incluir cuentas en clustering

from test_generator.markdown import Text,Paragraphs,Table
from test_generator.exam import Exam,Question,generate_and_save
from random import randrange,seed
from questions import trees, preprocessing


class Dataset:
    def __init__(self,rows,header:[str],attributes:[str],class_values:[str],ordinal_values=None):
        self.rows=rows
        self.header=header
        self.attributes=attributes
        self.class_values=class_values
        self.ordinal_values=ordinal_values

    @property
    def n(self):
        return len(self.rows)
    @property
    def m(self):
        return len(self.header)

    @property
    def str_rows(self):
        return [ [str(v) for v in row] for row in self.rows]

    def column(self,column:int):
        return [ row[column] for row in self.rows]
    def attribute(self,attribute:str):
        column=self.attributes.index(attribute)
        return self.column()
    def row(self,row:int):
        return self.rows[row]

    def discretize(self, col, new_values, strategy: preprocessing.Discretization):
        n_intervals=len(new_values)
        d=self.copy()
        values=d.column(col)
        intervals,values= preprocessing.discretize(values, n_intervals, strategy)
        
        values=[new_values[i] for i in values]
        d.replace_column(col,values)
        return d
    def replace_column(self,col,values):
        for r,v in zip(self.rows,values):
            r[col]=v

    def copy(self):
        rows=copy.deepcopy(self.rows)
        header=copy.deepcopy(self.header)
        attributes=copy.deepcopy(self.attributes)
        class_values=copy.deepcopy(self.class_values)
        return Dataset(rows,header,attributes,class_values,self.ordinal_values)

    @classmethod
    def people(cls,n=8):
        attributes=["Edad","Altura","Habilidad"]
        header=attributes+["Clase"]
        class_values=["Si", "No"]
        skill_values=["Baja","Media","Alta"]
        def random_person():
            age=randrange(15,20)
            height = int(np.random.normal(loc=170,scale=20))
            
            skill=skill_values[randrange(len(skill_values))]
            klass=class_values[randrange(len(class_values))]
            return [age,height,skill,klass]
        rows = [random_person() for i in range(n)]
        
        d=Dataset(rows,header,attributes,class_values,skill_values)
        # ensure all values appear at least once
        for i,values in [(2,skill_values),(3,class_values)]:
            col=d.column(i)
            missing_values=[]
            for val in values:
                if not val in col:
                    missing_values.append(val)
            for j,v in enumerate(missing_values):
                d.rows[j][i]=v
        return d
    
    def numerize(self):
        rows=[row.copy() for row in self.rows]
        for i in range(len(rows)):
            v=rows[i][2]
            rows[i][2]= self.ordinal_values.index(v)+1

        return Dataset(rows,self.header,self.attributes,self.class_values)




class DataQuestion(Question):
    def __init__(self,d:Dataset):
        self.d=d

from test_generator.markdown import Renderable
class DisplayTable(Renderable):
    def __init__(self,d:Dataset):
        self.d=d
    def render(self, seed=None):
        title=Text("**Tabla de datos**")
        t=Table(self.d.str_rows,header=self.d.header,number_rows=True)
        p=Paragraphs([title,t])
        return p.render()

class Discretization(DataQuestion):

    def answer(self,strategy,result):
        intervals,values=result
        e=Text(f"Resultado de la discretización por {strategy}:")
        v=Text(f"Valores: {values}")
        i=Text(f"Intervalos: {intervals}")
        a= Paragraphs([e,v,i])
        return a

    def generate(self, seed=None):
        n_intervals=3
        attribute_index=1#randrange(2)
        q=Paragraphs([Text(f"Discretice el atributo {self.d.attributes[attribute_index]}  por a) frecuencia y b) rango en {n_intervals} valores. En ambos casos, indique los intervalos resultantes. Realice un gráfico de barras para visualizar la frecuencia de los valores resultantes.\n\n Nota: La discretización es solo para este ejercicio; utilizar los datos originales en los siguientes.")])

        values=self.d.column(attribute_index)
        strategies={"rango": preprocessing.discretize_by_range, "frecuencia": preprocessing.discretize_by_frequency}
        results={k:f(values,n_intervals) for k,f in strategies.items()}
        answers=[self.answer(k,r) for k,r in results.items()]
        a=Paragraphs(answers)
        return q,a

    def title(self):
        return "Discretización de atributos"

class Normalization(DataQuestion):

    def answer(self, strategy:str, norm: preprocessing.CenterScaleNormalization, values):
        a=Text(f"Normalización {strategy} con transformación {norm}")
        normalized_values=norm.apply(values)
        normalized_values=", ".join([f"{v:.2f}" for v in normalized_values])
        v=Text(f"Valores normalizados: {normalized_values}")
        return Paragraphs([a,v])

    def generate(self, seed=None):
        attribute_index=0#randrange(2)
        q=Paragraphs([Text(f"Normalice el atributo {self.d.attributes[attribute_index]} mediante a) rango lineal uniforme y b) media/varianza. En ambos casos, indicar los valores resultantes. \n Nota: La normalización es solo para este ejercicio; utilizar los datos originales en los siguientes.")])
        values=self.d.column(attribute_index)
        values=np.array(values,dtype=np.float)
        strategies={"min/max": preprocessing.CenterScaleNormalization.min_max(values),
                    "mu/std": preprocessing.CenterScaleNormalization.mu_std(values)}
        answers =[self.answer(name,norm,values) for name,norm in strategies.items()]
        a=Paragraphs(answers)
        return q,a

    def title(self):
        return "Normalización de atributos"

class InformationGain(DataQuestion):

    def generate(self, seed=None):
        
        attributes=[self.d.attributes[0],self.d.attributes[2]]
        m=len(attributes)
        header=["Atributo"]+attributes
        data = [  ["Entropía"]+[" "]*m, 
                ["Ganancia de Información"]+[" "]*m
        ]

        infogain_table=Table(data,header=header)
        att =" y ".join(attributes)
        q=Paragraphs([Text(f"Calcule la entropía general del conjunto de datos en base al atributo de clase. Luego, calcule la entropía y ganancia de información para los atributos {att}. Utilice la siguiente tabla para presentar los resultados:"),
        infogain_table,
        Text(f"En base a estos valores, indique cuál de los {m} atributos se elegiría para generar la raíz de un árbol de decisión."),
        ])
        y=self.d.column(3)
        y=np.array(y)
        numeric=np.array(self.d.column(0))
        
        nominal=self.d.column(2)
        # values
        entropy_general= trees.entropy(y)
        entropy_nominal= trees.entropy_nominal(nominal, y)
        infogain_nominal= trees.information_gain_nominal(nominal, y)

        entropies_numeric,discretization_points= trees.entropy_numeric(numeric, y)
        infogains_numeric,_= trees.information_gain_numeric(numeric, y)
        # all
        entropy_numeric=entropies_numeric.min()
        infogain_numeric=infogains_numeric.max()
        def format(x):
            return f"{x:.2f}"
        results=[["Entropía",format(entropy_numeric),format(entropy_nominal)],
                  ["Ganancia",format(infogain_numeric),format(infogain_nominal)]]
        
        results_table=Table(results,header=header)
        # numericresults
        numeric_header=["Punto de corte", "Entropía", "Info Gain"]
        for l in [discretization_points,entropies_numeric,infogains_numeric]:
            for i in range(len(l)):
                l[i]=format(l[i])
        numeric_data=list(zip(discretization_points,entropies_numeric,infogains_numeric))

        numeric_table=Table(numeric_data,header=numeric_header)
        entropy_text=Text(f"Entropía general: {entropy_general}")
        a=Paragraphs([entropy_text,results_table,numeric_table])
        return q,a

    def title(self):
        return "Ganancia de Información"

from questions.rules import *

class OneRQuestion(DataQuestion):


    def generate(self, seed=None):
        # rule1,rule2=self.generate_rules()
        # rules=[rule1,rule2]
        # results=[DatasetMetric.eval_all(r,self.d.rows) for r in rules]

        # header=["Regla"]+list(results[0].keys())
        empty_data=[["Accuracy","","",""]]
    
        results_table=Table(empty_data,header=[""]+self.d.attributes)

        data_table=Table(self.d.rows,header=self.d.header)
        rules_table=Table([["..."]],header=["Reglas con [atributo]"])
        q=Paragraphs([Text(f"Dado la siguiente discretización del conjunto de datos original, aplique el algoritmo OneR para encontrar el mejor atributo y las reglas asociadas para clasificar los ejemplos según el atributo Clase. "),
        data_table,
        Text("Mostrar el accuracy de cada atributo, y las reglas finales del OneR:"),
        results_table,rules_table])

        best_model,attribute_models=OneR.fit(self.d.rows,self.d.attributes)
        # def format_row(r:Rule,res:{}):
        #     values=[f"{v:.2f}" for v in res.values()]
        #     return [str(r)]+values
        # data=[format_row(r,res) for r,res in zip(rules,results)]
        # a=Table(data,header=header)
        rules_tables=[]
        confidence_metric=Confidence()
        for model in attribute_models:
            accuracy=model.accuracy(self.d.rows,self.d.column(3))
            rules=[]
            for rule in model.rules:
                confidence=f"{confidence_metric.eval(rule,self.d.rows):.2f}"
                support=rule.antecedent.count_matches(self.d.rows)
                rules.append([rule,confidence,support])
            rules_table=Table(rules,header=[f"Reglas con {model.attribute_name} (accuracy={accuracy})","Confianza","Soporte(absoluto)"])
            rules_tables.append(rules_table)

        a=Paragraphs(
            [data_table,
            Text(f"Mejor atributo: {best_model.attribute_name}") ]
            +rules_tables)
        return q,a

    def title(self):
        return "Modelo OneR"



class RuleMetrics(DataQuestion):
    def dataset_rule(self,index:int,value,op=Operator.eq):
        attribute_name=self.d.header[index]
        return AttributeRange(index,value,op,name=attribute_name)

    def generate_rules(self):

        rule1=Rule(self.dataset_rule(2,"Alta"),self.dataset_rule(3,"Si"))
        def random_range(col):
            vals=self.d.column(col)
            m=round(sum(vals)/len(vals))
            return self.dataset_rule(col,m,op=Operator.lt)
        a=AndConditions([random_range(0), self.dataset_rule(2,"Baja")])
        c=random_range(1)
        rule2=Rule(a,c)
        #rule2=f"{self.d.attributes[1]} y {self.d.attributes[2]} → {self.d.attributes[0]}"
        return rule1,rule2

    def generate(self, seed=None):
        rule1,rule2=self.generate_rules()
        rules=[rule1,rule2]
        results=[DatasetMetric.eval_all(r,self.d.rows) for r in rules]

        header=["Regla"]+list(results[0].keys())
        empty_data=[[str(r),"","","",""] for r in rules ]
        rules_table=Table(empty_data,header=header)
        
        q=Paragraphs([Text("Calcule el soporte, cobertura, confianza, e interés de las siguientes reglas:"),
        rules_table])
        def format_row(r:Rule,res:{}):
            values=[f"{v:.2f}" for v in res.values()]
            return [str(r)]+values
        data=[format_row(r,res) for r,res in zip(rules,results)]
        a=Table(data,header=header)
        return q,a

    def title(self):
        return "Métricas de Reglas"


class Numerization(DataQuestion):
    def __init__(self, d:Dataset,d_numerized:Dataset):
        super().__init__(d)
        self.d_numerized=d_numerized

    def generate(self, seed=None):
        col=2
        q=Text(f"Numerizar el atributo {self.d.attributes[col]} del conjunto de datos, con la estrategia de generar un valor entero por cada valor numérico. Comenzar con el valor 1, y respetar el orden natural de dicho atributo (Baja < Media < Alta). Mostrar los valores resultantes.")

        original=Text(f"Valores originales: {self.d.column(col)}\n")
        nuevos = Text(f"Valores nuevos: {self.d_numerized.column(col)}\n")
        t=Table(self.d_numerized.str_rows,header=self.d_numerized.header,number_rows=True)
        a=Paragraphs([original,nuevos,t])
        
        return q,a
    def title(self):
        return "Numerización de datos"    

class CorrelationMatrix(DataQuestion):
    def generate(self,seed=None):
        attributes=["Ambiente","Temperatura","Humedad","Viento","Juega"]
        header = [" "]+attributes
        rows=[[1,0.28,0.11,0,-0.18],
              [0.28,1,0.75,-0.21,-0.11],
              [0.11,0.75,1,-0.12,-0.52],
              [0,-0.21,-0.12,1,-0.26],
              [-0.18,-0.11,-0.52,-.26,1]
             ]
        rows = [[str(v) for v in row] for row in rows]
        rows = [[a]+row for a,row in zip(attributes,rows)]

        correlation_matrix=Table(rows,header=header)
        q=Paragraphs(
            [Text("Dada la siguiente matriz de correlación, indique la verdad (V) o falsedad (F) de las afirmaciones:"),
            correlation_matrix,
            Text("a) Los atributos Ambiente y Viento son independientes.\nb) Es posible que si sube la Humedad, también suba el valor del atributo Juega.\nc) Los atributos Humedad y Temperatura están correlacionados linealmente, y la correlación es **fuerte**.\nd) La mayoría de los pares de atributos no están correlacionados linealmente."),
            ])
        aa=Text("a) Falso, ya que pueden estar correlacionados igual aunque no de forma lineal, por ejemplo, viente=ambiente^2")
        ab=Text("b) Falso,  la correlación es negativa")
        ac=Text("c) Falso, la correlación es débil (0.5<x<0.8)")
        ad=Text("d) Verdadero, de los 10 pares solo 2 tienen correlación lineal débil o fuerte.")
        a=Paragraphs([Text("F,F,F,V"),aa,ab,ac,ad])
        return q,a
    def title(self):
        return "Matriz de Correlación"


class CorrelationMatrix2(DataQuestion):
    def generate(self,seed=None):
        attributes=["Ambiente","Temperatura","Humedad","Viento","Juega"]
        header = [" "]+attributes
        rows=[[1,0.28,1,0,-0.18],
              [0.28,1,0.75,-0.85,-0.11],
              [1,0.75,1,-0.12,-1],
              [0,-0.85,-0.12,1,-0.26],
              [-0.18,-0.11,-1,-.26,1]
             ]
        rows = [[str(v) for v in row] for row in rows]
        rows = [[a]+row for a,row in zip(attributes,rows)]

        correlation_matrix=Table(rows,header=header)
        q=Paragraphs(
            [Text("Dada la siguiente matriz de correlación, indique la verdad (V) o falsedad (F) de las afirmaciones:"),
            correlation_matrix,
            Text("a) Los atributos Ambiente y Humedad son independientes.\nb) Los atributos Juega y Humedad son independientes \nc) Los atributos Viento y Temperatura están correlacionados linealmente, y la correlación es **fuerte**.\nd) La mayoría de los pares de atributos están correlacionados linealmente."),
            ])
        aa=Text("a) Falso, un valor de 1 indica que son linealmente dependientes con dependencia positiva ")
        ab=Text("b) Falso,  un valor de -1 indica que son linealmente dependientes con dependencia positiva")
        ac=Text("c) Verdadero, la correlación es fuerte (<-0.8)")
        ad=Text("d) Falso, de los 5*4/2=10 pares solo 4 tienen correlación lineal débil o fuerte.")
        a=Paragraphs([Text("F,F,V,F"),aa,ab,ac,ad])
        return q,a
    def title(self):
        return "Matriz de Correlación"


class TrueOrFalse(Question):

    def generate(self):
        questions=["Dado un conjunto de atributos, puede afirmarse que los que tengan el mismo valor de entropía también tendrán el mismo valor de Ganancia de Información (Information Gain).",
        "El índice Silhouette se calcula en base a la dispersión de los ejemplos de cada grupo (cluster) y la distancia entre los centros.",
        "Si se busca construir un árbol de clasificación, el atributo de clase no puede ser numérico.",
        "Las reglas de clasificación que se generan con OneR pueden ejecutarse en cualquier orden a diferencia de las generadas con el método PART.",
        "Dadas dos reglas con valor de confianza=1 (perfectas) será más interesante la que tenga un menor valor de soporte para el consecuente.",
        "Un atributo nominal sólo aparecerá una vez en una misma regla generada con el método PART (recuerde que se generan como una rama de un árbol parcialmente construido con C4.5)",
        "Para poder agrupar un conjunto de ejemplos utilizando el método K-Means es obligatorio que los valores de los atributos estén escalados."]
        answers="V,F,V,V,V,V,F"
        questions = [f"{i+1}) {q}" for i,q in enumerate(questions)]
        questions_text=Text("\n\n".join(questions))
        enunciado=Text("Indique el valor de verdad de las siguientes afirmaciones. Justifique su respuesta.")
        q=Paragraphs([enunciado,questions_text])
        return q,Text(answers)

    def title(self):
        return "Verdadero o Falso"



class RandomQuestions(Question):

    def generate(self):
        questions=[
        "La normalización lineal uniforme ¿es sensible a valores anómalos? ¿y la normalización por media/varianza?",
        "En un árbol de clasificación ¿a qué corresponden los nodos intermedios, los nodos hoja y las aristas?"
        "Dado un itemset con 3 items A,B,C, ¿cuántas reglas pueden generarse en base al itemset?",
        "El algoritmo Apriori ¿genera reglas de Asociación?",
        "El algoritmo FPGrowth ¿genera reglas de Asociación?",
        "Al generar reglas con APriori o FPGrowth ¿es necesario generar itemsets?",
        "Dados los items A y B, si A->B tiene soporte 0.7 ¿cuál será el soporte de B->A?",
        "¿Cuáles son las dos propiedades que deben cumplir los grupos (clusters) para obtener un buen agrupamiento?",
        "El peso de una red neuronal correspondiente al atributo A es negativo. Dado un ejemplo, si el valor de A sube, ¿a qué clase se acercará el ejemplo?",
        ]

        
        answers=[
            "Lineal si, media/varianza también pero menos",
            "Los nodos intermedios corresponden a atributos, las aristas a valores de esos atributos, y los nodos hoja a decisiones o predicciones de la clase",
            "6, A->(B,C) B->(A,C) C->(A,B), idem con 2 items en el antecedente",
            "No, genera itemsets",
            "No, genera itemsets",
            "Si, justamente generan itemsets",
            "El mismo",
            "Alta cohesión intra cluster y alta separación intercluster.",
            " A la clase 0, ya que a mayor valor de A, menor valor de la entrada neta.",
        ]
        def to_enumeration(a:[str]):
            a = [f"{i+1}) {x}" for i,x in enumerate(a)]
            return "\n\n".join(a)
        questions = to_enumeration(questions)
        enunciado=Text("Indique la respuesta a las siguientes preguntas. Justifique su respuesta.")
        q=Paragraphs([enunciado,Text(questions)])
        answers =to_enumeration(answers)
        return q,Text(answers)

    def title(self):
        return "Preguntas conceptuales"

class Clustering(DataQuestion):
    def generate_centroids(self):
        col0=self.d.column(0)
        col1=self.d.column(1)
        col0.sort(),col1.sort()
        c1=[col0[2],col1[3],1]
        c2=[col0[-3],col1[-2],2]

        c=Dataset([c1,c2],self.d.attributes[:3],self.d.attributes[:3],[])
        return c

    def calculate_distances(self,cd:Dataset):
        n_samples=self.d.n
        samples=[ r[:-1] for r in self.d.rows]
        centroids=cd.rows
        n_centroids=cd.n
        distances_rows=[]
        for i in range(n_samples):
            row=[]
            for j in range(n_centroids):
                sample,centroid=samples[i],centroids[j]
                distance=sum([(s-c)**2 for s,c in zip(sample,centroid)])
                row.append(distance)
            assigned_centroid=row.index(min(row))
            row.append(assigned_centroid+1)
            distances_rows.append(row)
        attributes=["d(c1)","d(c2)","Centroide asignado"]
        return Dataset(distances_rows,attributes,attributes,[])


    def db_vs_silhouette(self,):
        q=Text("b) El costo computacional del cálculo del índice Silhouette ¿suele ser mayor que el de Davies-Bouldin?. Justifique su respuesta.")
        a=Text("a) La afirmación es verdadera porque el Silhouette calcula para cada ejemplo su distancia promedio con los de su grupo y con los del grupo más cercano con esto obtiene el índice de cada ejmplo y finalmente los promedia. Por otro lado, DB compara agrupamientos y se espera que la cantidad de grupos sea considerablemente menor a la de ejemplos. Si esto último no ocurre, podría darse que DB fuera más costoso computacionalmente hablando pero este escenario no tiene mucho sentido en un contexto donde se busca construir un modelo descriptivo.")
        return q,a
        
    def silhouette_centers(self,):
        q= Text("b) ¿Es preciso conocer la posición de los centros para calcular el índice Silhouette del agrupamiento? Justifique su respuesta.")
        a= Text("b) Falso, ya que calcula distancias entre ejemplos y no centroides.")
        return q,a
    
    def silhouette_values(self):
        q= Text("b) En el índice Sillhouette, tanto -1 como 1 son buenos valores, donde -1 indica correlación negativa y 1 positiva, y 0 indica que el clustering no es bueno.")
        a= Text("b) Falso, 1 indica que el clustering es bueno (máxima cohesión y separación), y -1 que es malo (mínima cohesión y separación). ")
        return q,a

    def generate(self, seed=None):
        centroids=self.generate_centroids()
        distances=self.calculate_distances(centroids)

        header=["Ejemplo"]+distances.attributes
        distances_table=Table([ ["1","$\sqrt{valor}$","$\sqrt{valor}$","(c1 o c2)"], ["..."]*4 ],header=header)

        header=["Centroide"]+self.d.attributes
        
        rows_with_id=[[f"**c{i+1}**"]+row for i,row in enumerate(centroids.str_rows)]
        centroid_table=Table(rows_with_id,header=header)
        n_samples=3
        b_q,b_a=self.silhouette_values()
        q=Paragraphs(
            [Text(f"a) Utilizando la numerización de datos generada anteriormente, y dados los centroides **c1** y **c2**, calcule la distancia euclídea de los {n_samples} primeros ejemplos hacia estos centroides, y a cuál de ellos estarían asignados. No utilizar la clase en este ejercicio."),
            centroid_table,b_q,
            Text("Nota: Para presentar los resultados, no calcule las raíces cuadradas. En lugar de eso, deje expresada los distancias como $\sqrt{valor}$. Utilice una tabla como la siguiente:"),
            distances_table
            ])
        
        results_table=Table(distances.str_rows[:n_samples],distances.header,number_rows=True)
        a = Paragraphs([results_table,b_a])
        return q,a

    def title(self):
        return "Agrupamiento de datos"

class Perceptron(DataQuestion):

    def generate_w(self):
        n_cols=3
        cols=[self.d.column(i) for i in range(n_cols)]
        def rand_sign(): return -1 if randrange(2)==0 else 1
        mean_cols= [ sum(c)/len(c) for c in cols ]
        inv_mean = [round(1/m,2) for m in mean_cols]
        min_mean=min(inv_mean)
        noise=(randrange(2)+1)
        inv_mean_scaled=[ (im/min_mean)*noise for im in inv_mean]
        
        #def noise(): return random()*0.1*rand_sign()
        # inv_mean_scaled = [v*scale_factor/n_cols for v in inv_mean]
        w=[int(im) for im in inv_mean_scaled]
        b=int(sum([m*w for m,w in zip(mean_cols,w)]))
        w=[ 1 if v==0 else v for v in w ]
        return w,b

    def random_sample(self):
        values=[]
        for i in range(self.d.m):
            column=self.d.column(i)
            index=randrange(len(column))
            values.append(column[index])
        return values

    def calculate_random(self,w,b):
        sample=self.random_sample()
        a0,a1,a2,a3=sample
        return self.calculate_input(w,b,a1,a2)

    def calculate_input(self,w,b,a1,a2):
        w0,w1,w2=w
        a0_equilibrium=(b-w1*a1-w2*a2)/w0
        if w[0]>0:
            klass="No"
            sign="positivo"
        else:
            sign="negativo"
            klass="Si"
        clases={0:"No",1:"Si"}

        q=Text(f"a) Asumiendo que Clase=No está codificado con un 0, y Clase=Si con un 1, ¿cuál es el valor máximo del atributo {self.d.attributes[0]}  para que un ejemplo con {self.d.attributes[1]}={a1} y {self.d.attributes[2]}={a2} pertenezca a la Clase={klass}?")
        w_str=', '.join([str(v) for v in w])
        valores=Text(f"Recordamos que w={w_str} y b={b}")
        attributes_str=", ".join(self.d.attributes)
        a=[q,valores,
            Text(f"Dados esos valores, y asumiendo que $a_0$, $a_1$ y $a_2$ son los valores para los atributos {attributes_str}, para que el modelo esté entre generar 0 o 1 debe cumplirse:"),
        Text(f"$a_0 . w0 + a_1 . w_1 + a_2 . w_2 = b$"),
        Text(f"$a_0 . w0 = b - a_1 . w_1 - a_2 . w_2$"),
        Text(f"$a_0  = (b - a_1 . w_1 - a_2 . w_2)/w_0$"),
        Text(f"$a_0  = ({b} - {a1} . {w1} - {a2} {w2})/{w0}$"),
        Text(f"$a_0 = {a0_equilibrium}$"),

        Text(f"Como buscamos que esté en clase {klass}, y el signo de $w_0$ es {sign}, necesitamos que $a_0$ tenga como valor máximo {a0_equilibrium}."),
        ]
        a= Paragraphs(a)


        return q,a

    def calculate_output_single(self,w,b,n_samples=3):
        sample=self.random_sample()
        sample=sample[:3]
        p0,p1,p2 = [f"{a} vale {v}" for a,v in zip(self.d.attributes,sample)]
        attributes=f"{p0}, {p1} y {p2}"
        clases={0:"No",1:"Si"}
        enunciado=Text(f"b) Asumiendo que Clase={clases[0]} está codificado con un 0, y Clase={clases[1]} con un 1, ¿cómo clasificaría el modelo a un ejemplo donde {attributes}?")
        
        q= Paragraphs([enunciado,
        ])
        

        def perceptron_output(w,b,row):
            neta=0
            for wi,xi in zip(w,row):
                neta+=wi*xi
            cuenta = "+".join([f"{wi}×{xi}" for wi,xi in zip(w,row)])
            neta_s = f"{cuenta} ={neta}"
            salida=0 if neta<b else 1
            salida_s=f"0 ({neta}<{b})" if neta<b else f"1 ({neta}>={b})"
            return neta_s,salida_s, salida
        neta_s,salida_s,salida=perceptron_output(w,b,sample)
        calculo=Text(f"La salida neta es {neta_s}, y por ende la salida es {salida_s}, con clase {clases[salida]}")
        a=Paragraphs([enunciado,calculo])
        return q,a

    def calculate_output(self,w,b,n_samples=3):
        enunciado=Text("a)  Calcular la entrada neta y la salida final (0 o 1) de los {n_samples} primeros ejemplos de la tabla de datos. \n\n Nota: El cálculo de la entrada neta no incluye el sesgo o bias.")
        header=["","Ejemplo 1", "Ejemplo 2","..."]
        sample_data=[["Neta","","","..."],["Salida","","","..."]]
        t=Table(sample_data,header=header)
        q= Paragraphs([enunciado,
        Text("Para presentar los resultados, utilice una tabla como la siguiente:"),
        t
        ])
        

        def perceptron_output(w,b,row):
            neta=0
            for wi,xi in zip(w,row):
                neta+=wi*xi
            cuenta = "+".join([f"{wi}×{xi}" for wi,xi in zip(w,row)])
            neta_s = f"{cuenta} ={neta}"
            salida=0 if neta<b else 1
            salida_s=f"0 ({neta}<{b})" if neta<b else f"1 ({neta}>={b})"
            return neta_s,salida_s

        outputs = [perceptron_output(w,b,row[:-1]) for row in self.d.rows[:n_samples] ]
        netas,salidas=zip(*outputs)
        header=[""]+[f"Ejemplo {i+1}" for i in range(n_samples)]
        rows= [["Neta"]+[str(o) for o in netas],
               ["Salida"]+[str(o) for o in salidas]]
        result_table=Table(rows,header=header)
        a=Paragraphs([enunciado,result_table])
        return q,a


    def generate(self, seed=None):
        w,b=self.generate_w()

        attributes=", ".join(self.d.attributes)
        enunciado=Text(f"Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w={w}* (para los atributos {attributes}, respectivamente) y *sesgo={b}*:")

        q1,a1=self.calculate_random(w,b)
        q2,a2=self.calculate_output_single(w,b)
        

        q=Paragraphs(
            [enunciado,
            q1,
            q2
            ])
        
        a=Paragraphs([a1,a2])
        return q,a

    def title(self):
        return "Perceptrón"

from pathlib import Path
import numpy as np

def parcial1():
    seed(0)
    np.random.seed(0)
    d=Dataset.people(n=8)    
    d_numerized=d.numerize()


    questions=[Discretization(d),
                Normalization(d),
                InformationGain(d),
                RuleMetrics(d),
                Numerization(d,d_numerized),
                Clustering(d_numerized),
                Perceptron(d_numerized),
                CorrelationMatrix(d_numerized)
                ]
    intro=DisplayTable(d)
    exam=Exam("Minería de Datos usando Sistemas Inteligentes",intro,questions,
    subtitle="Primer Parcial - 17 de Junio de 2020",geometry="margin=2cm")
    return exam

def parcial2():
    seed(1)
    np.random.seed(1)
    d=Dataset.people(n=8)    
    d_numerized=d.numerize()
    d_discretized=d.discretize(0, ["Baja","Media","Alta"], preprocessing.Discretization.frequency)
    d_discretized=d_discretized.discretize(1, ["Baja","Alta"], preprocessing.Discretization.frequency)

    questions=[Discretization(d),
                Normalization(d),
                InformationGain(d),
                RuleMetrics(d),
                OneRQuestion(d_discretized),
                Numerization(d,d_numerized),
                Clustering(d_numerized),
                Perceptron(d_numerized),
                #CorrelationMatrix2(d_numerized),
                TrueOrFalse(),
                ]
    intro=DisplayTable(d)
    exam=Exam("Minería de Datos usando Sistemas Inteligentes",intro,questions,
    subtitle="Segunda Fecha - 1 de Julio de 2020",geometry="margin=2cm")
    return exam

def parcial3():
    
    d=Dataset.people(n=8)    
    d_numerized=d.numerize()
    d_discretized=d.discretize(0, ["Baja","Media","Alta"], preprocessing.Discretization.frequency)
    d_discretized=d_discretized.discretize(1, ["Baja","Alta"], preprocessing.Discretization.frequency)

    questions=[Discretization(d),
                Normalization(d),
                InformationGain(d),
                RuleMetrics(d),
                OneRQuestion(d_discretized),
                Numerization(d,d_numerized),
                Clustering(d_numerized),
                Perceptron(d_numerized),
                #CorrelationMatrix2(d_numerized),
                #TrueOrFalse(),
                RandomQuestions(),
                ]
    intro=DisplayTable(d)
    exam=Exam("Minería de Datos usando Sistemas Inteligentes",intro,questions,
    subtitle="Tercera Fecha - 15 de Julio de 2020",geometry="margin=2cm")
    return exam

if __name__ == "__main__":
    seed(2)
    np.random.seed(2)
    n_exams=8
    folderpath=Path("p3")
    for i in tqdm(range(n_exams)):
        exam=parcial3()
        filename = f"exam{i+1:02d}"
        generate_and_save(exam,folderpath,filename,pdf=True)

