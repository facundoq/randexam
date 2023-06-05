from test_generator import *
from questions.rules import *
from test_generator.data import Dataset


class OneRQuestion(DataQuestion):

    def generate(self, seed=None):
        # rule1,rule2=self.generate_rules()
        # rules=[rule1,rule2]
        # results=[DatasetMetric.eval_all(r,self.d.rows) for r in rules]

        # header=["Regla"]+list(results[0].keys())
        empty_data = [["Accuracy", "", "", ""]]

        results_table = Table(empty_data, header=[""] + self.d.attributes)

        data_table = Table(self.d.rows, header=self.d.header)
        rules_table = Table([["..."]], header=["Reglas con [atributo]"])
        q = Paragraphs([Text(
            f"Dada la siguiente discretización del conjunto de datos original, aplique el algoritmo OneR para encontrar el mejor atributo y las reglas asociadas para clasificar los ejemplos según el atributo Clase. "),
                        data_table,
                        Text("Mostrar el accuracy de cada atributo, y las reglas finales del OneR:"),
                        results_table, rules_table])

        best_model, attribute_models = OneR.fit(self.d.rows, self.d.attributes)
        # def format_row(r:Rule,res:{}):
        #     values=[f"{v:.2f}" for v in res.values()]
        #     return [str(r)]+values
        # data=[format_row(r,res) for r,res in zip(rules,results)]
        # a=Table(data,header=header)
        rules_tables = []
        confidence_metric = Confidence()
        for model in attribute_models:
            accuracy = model.accuracy(self.d.rows, self.d.column(3))
            rules = []
            for rule in model.rules:
                confidence = f"{confidence_metric.eval(rule, self.d.rows):.2f}"
                support = rule.antecedent.count_matches(self.d.rows)
                rules.append([rule, confidence, support])
            rules_table = Table(rules, header=[f"Reglas con {model.attribute_name} (accuracy={accuracy})", "Confianza",
                                               "Soporte(absoluto)"])
            rules_tables.append(rules_table)

        a = Paragraphs(
            [data_table,
             Text(f"Mejor atributo: {best_model.attribute_name}")]
            + rules_tables)
        return q, a

    def title(self):
        return "Modelo OneR"