from questions import trees
from test_generator import *
import numpy as np

class InformationGain(DataQuestion):
    def __init__(self, d:Dataset, numeric_attribute:int,nominal_attribute:int,class_index:int,log_base=2,points=2,include_table=False):
        super().__init__(d,points=points)
        self.numeric_attribute=numeric_attribute
        self.nominal_attribute = nominal_attribute
        self.class_index=class_index
        self.log_base=log_base
        self.include_table = include_table
    
    def generate_log_tables(self,n,columns=8):
        log_values = []
        log_header = []
        for m in range(2,n+1):
            log_values += [f"{trees.log(i/ m,log_base=self.log_base):.3f}" for i in range(1,m)]
            log_header += [f"$log_{{{self.log_base}}}({i}/{m})$" for i in range(1,m) ]
        def split(a, m):
            n,k = divmod(len(a), m)
            if k>0:
                n+=1
            return list([a[i*m : min((i+1)*m,len(a)) ] for i in range(n)])
        def interleave(a,b):
            return [val for pair in zip(a, b) for val in pair]
        logs = interleave(split(log_header,columns),split(log_values,columns))
        print(logs)
        return Table(logs,column_separator="|")
        
    
    def _generate(self, seed=None):
        attribute_indices=[self.numeric_attribute,self.nominal_attribute]
        attributes = [self.d.attributes[i] for i in attribute_indices]
        m = len(attributes)
        header = ["Atributo"] + attributes
        data = [["Entropía"] + [" "] * m,
                ["Ganancia de Información"] + [" "] * m
                ]

        infogain_table = Table(data, header=header)
        att = " y ".join(attributes)
        trees.log_base = self.log_base
        n = self.d.n
        numeric_attribute_name = self.d.attributes[self.numeric_attribute]
        q = [Text(
            f"Utilizando los datos originales, calcule la entropía general del conjunto de datos en base al atributo de clase. Luego, calcule la entropía y ganancia de información para los atributos {att}. Tenga en cuenta que el atributo {numeric_attribute_name} es numérico, por lo cual deberá utilizar la variante del algoritmo que busca la mejor discretización probando todos los puntos de corte posibles.  Utilice la siguiente tabla para presentar los resultados:"),
                        infogain_table,
                        Text(
                            f"En base a estos valores, indique cuál de los {m} atributos se elegiría para generar la raíz de un árbol de decisión.\n"
                            f"Utilice dos decimales para los cálculos. \n"
                            f"Recuerde que para los atributos numéricos debe calcular la ganancia de información de todos los puntos de corte.\n"
                            f"Utilice logaritmo con base {self.log_base} para todos los cálculos (obligatorio)."
                            f""),
                        Text(f"Algunos de logaritmos base {self.log_base} (use su calculadora para otros):"),
                        
                        ]
        if self.include_table:
            print("appending")
            q.append(self.generate_log_tables(n))
        y = self.d.column(self.class_index)
        y = np.array(y)

        numeric = np.array(self.d.column(self.numeric_attribute))
        nominal = self.d.column(self.nominal_attribute)

        # values

        entropy_general = trees.score(y,log_base=self.log_base)
        entropy_nominal = trees.entropy_nominal(nominal, y,log_base=self.log_base)
        infogain_nominal = trees.information_gain_nominal(nominal, y,log_base=self.log_base)

        entropies_numeric, discretization_points = trees.entropy_numeric(numeric, y,log_base=self.log_base)
        infogains_numeric, _ = trees.information_gain_numeric(numeric, y,log_base=self.log_base)
        # all
        entropy_numeric = entropies_numeric.min()
        infogain_numeric = infogains_numeric.max()

        def format(x):
            return f"{x:.2f}"

        results = [["Entropía", format(entropy_numeric), format(entropy_nominal)],
                   ["Ganancia", format(infogain_numeric), format(infogain_nominal)]]

        results_table = Table(results, header=header)
        # numericresults
        numeric_header = ["Punto de corte", "Entropía", "Info Gain"]
        for l in [discretization_points, entropies_numeric, infogains_numeric]:
            for i in range(len(l)):
                l[i] = format(l[i])
        numeric_data = list(zip(discretization_points, entropies_numeric, infogains_numeric))

        numeric_table = Table(numeric_data, header=numeric_header)
        base_text = Text(f"Entropías calculadas con logaritmo con base {self.log_base}")
        entropy_text = Text(f"Entropía general: {entropy_general}")
        a = Paragraphs([base_text,entropy_text, results_table,f"Entropía de cortes del atributo {numeric_attribute_name}", numeric_table])
        return q, a

    def title(self):
        return "Ganancia de Información"