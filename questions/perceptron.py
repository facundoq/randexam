from test_generator import *
from random import randrange,seed

class Perceptron(DataQuestion):

    def __init__(self,d:Dataset,class_column:int,points=1):
        super().__init__(d,points=points)
        self.class_column=class_column
        self.class_values = list(set(self.d.column(class_column)))
        self.c0,self.c1 = self.class_values
        self.classes = {0:self.c0,1:self.c1}
        assert len(self.class_values) == 2, "Should have only 2 class values for a perceptron"

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
        c0,c1 = self.class_values
        w0,w1,w2=w
        a0_equilibrium=(b-w1*a1-w2*a2)/w0
        if w[0]>0:
            klass=c1
            sign="positivo"
        else:
            sign="negativo"
            klass=c0


        q=Text(f"a) Asumiendo que Clase={c0} está codificado con un 0, y Clase={c1} con un 1, ¿cuál es el valor máximo del atributo {self.d.attributes[0]}  para que un ejemplo con {self.d.attributes[1]}={a1} y {self.d.attributes[2]}={a2} pertenezca a la Clase={klass}?")
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
        enunciado=Text(f"b) Asumiendo que Clase={self.c0} está codificado con un 0, y Clase={self.c1} con un 1, ¿cómo clasificaría el modelo a un ejemplo donde {attributes}?")

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
        calculo=Text(f"La salida neta es {neta_s}, y por ende la salida es {salida_s}, con clase {self.classes[salida]}")
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


    def _generate(self, seed=None):
        w,b=self.generate_w()

        attributes=", ".join(self.d.attributes)
        enunciado=Text(f"Utilizando la numerización de datos generada anteriormente, y dado un modelo de perceptrón donde los pesos son *w={w}* (para los atributos {attributes}, respectivamente) y *sesgo={b}*:")

        q1,a1=self.calculate_output_single(w,b)
        q2,a2=self.calculate_random(w,b)


        q=Paragraphs(
            [enunciado,
            q1,
            q2
            ])

        a=Paragraphs([a1,a2])
        return q,a

    def title(self):
        return "Perceptrón"