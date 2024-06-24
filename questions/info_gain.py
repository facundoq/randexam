from questions import trees
from test_generator import *
import numpy as np

class InformationGain(DataQuestion):
    def __init__(self, d:Dataset, numeric_attributes:list[int],nominal_attributes:list[int],class_index:int,log_base=2,points=2,include_table=False):
        super().__init__(d,points=points)
        if isinstance(numeric_attributes , int):
            numeric_attributes  = [numeric_attributes ]
        if isinstance(nominal_attributes , int):
            nominal_attributes  = [nominal_attributes ]

        self.numeric_attributes=numeric_attributes
        self.nominal_attributes = nominal_attributes
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
        return Table(logs,column_separator="|")
        
    def nominal_results(self,y:np.ndarray):
        nominal_entropies,nominal_infogains = [], []
        for nominal_attribute in self.nominal_attributes:
            nominal = self.d.column(nominal_attribute)
            entropy = trees.entropy_nominal(nominal, y,log_base=self.log_base)
            infogain = trees.information_gain_nominal(nominal, y,log_base=self.log_base)
            nominal_entropies.append(entropy)
            nominal_infogains.append(infogain)
        return nominal_entropies,nominal_infogains

    def numeric_results(self,y:np.ndarray):
        numeric_entropies,numeric_infogains, cutpoint_tables = [], [], []
        for numeric_attribute in self.numeric_attributes:
            numeric = np.array(self.d.column(numeric_attribute))
            entropies_numeric, discretization_points = trees.entropy_numeric(numeric, y,log_base=self.log_base)
            infogains_numeric, _ = trees.information_gain_numeric(numeric, y,log_base=self.log_base)
            # all
            numeric_entropies.append(entropies_numeric.min())
            numeric_infogains.append(infogains_numeric.max())
            numeric_attribute_name = self.d.attributes[numeric_attribute]
            # generate table for cutpoints
            cutpoints_header = [f"{numeric_attribute_name}: Punto de corte", "Entropía", "Info Gain"]
            for l in [discretization_points, entropies_numeric, infogains_numeric]:
                for i in range(len(l)):
                    l[i] = f"{l[i]:.2f}"
            cutpoints_data = list(zip(discretization_points, entropies_numeric, infogains_numeric))

            cutpoint_tables.append(Table(cutpoints_data, header=cutpoints_header))
        return numeric_entropies,numeric_infogains,cutpoint_tables

    def _generate(self, seed=None):
        attribute_indices = self.numeric_attributes+self.nominal_attributes
        assert(len(attribute_indices)>1, "Must include at least two attributes.")        
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
        numeric_attribute_warning = ""
        if len(self.numeric_attributes)>0:
            numeric_attribute_warning =f"""Tenga en cuenta que para los atributos numéricos deberá utilizar la variante del algoritmo que busca la mejor discretización probando todos los puntos de corte posibles."""

        q = [Text(
            f"Utilizando los datos originales, calcule la entropía general del conjunto de datos en base al atributo de clase. Luego, calcule la entropía y ganancia de información para los atributos {att}. {numeric_attribute_warning} Utilice la siguiente tabla para presentar los resultados:"),
                        infogain_table,
                        Text(
                            f"En base a estos valores, indique cuál de los {m} atributos se elegiría para generar la raíz de un árbol de decisión.\n"
                            f"Utilice dos decimales para los cálculos. \n"
                            f"Utilice logaritmo con base {self.log_base} para todos los cálculos (obligatorio)."),
                        
                        
                        ]
        if self.include_table:
            q.append(Text(f"Logaritmos de base {self.log_base}"))
            q.append(self.generate_log_tables(n))
        y = self.d.column(self.class_index)
        y = np.array(y)
        # values
        entropy_general = trees.score(y,log_base=self.log_base)
        nominal_entropies,nominal_infogains = self.nominal_results(y)
        numeric_entropies,numeric_infogains, cutpoints_tables = self.numeric_results(y)

        def format_list(l):
            return list(map(lambda x: f"{x:.2f}",l))
        results = [
            ["Entropía"] + format_list(numeric_entropies+nominal_entropies),
            ["Ganancia"] + format_list(numeric_infogains+nominal_infogains),
                ]
        results_table = Table(results, header=header)
        # numericresults
        
        base_text = Text(f"Entropías calculadas con logaritmo con base {self.log_base}")
        entropy_text = Text(f"Entropía general: {entropy_general}")
        a = Paragraphs([base_text,entropy_text, results_table,]+cutpoints_tables)

        # f"Entropía de cortes del atributo {numeric_attribute_name}", numeric_table
        return q, a

    def title(self):
        return "Ganancia de Información"