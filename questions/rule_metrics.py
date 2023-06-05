from test_generator import *
from questions.rules import *
from random import randrange

class RuleMetrics(DataQuestion):
    def dataset_rule(self, index: int, value, op=Operator.eq):
        attribute_name = self.d.header[index]
        return AttributeRange(index, value, op, name=attribute_name)

    def dataset_rule_random_value(self,index:int,op=Operator.eq):
        values =list(set(self.d.column(index)))
        rand_index = randrange(0, len(values))
        value = values[rand_index]
        return self.dataset_rule(index,value,op)

    def generate_rules(self):

        rule1 = Rule(self.dataset_rule_random_value(2), self.dataset_rule_random_value(3))
        rule2 = Rule(self.dataset_rule_random_value(3), self.dataset_rule_random_value(2))

        def random_range(col):
            vals = self.d.column(col)
            m = round(sum(vals) / len(vals))
            return self.dataset_rule(col, m, op=Operator.lt)

        a = AndConditions([random_range(0), self.dataset_rule_random_value(2)])
        c = random_range(1)
        rule3 = Rule(a, c)
        # rule2=f"{self.d.attributes[1]} y {self.d.attributes[2]} → {self.d.attributes[0]}"
        return [rule1, rule2,rule3]

    def generate(self, seed=None):
        rules = self.generate_rules()
        results = [DatasetMetric.eval_all(r, self.d.rows) for r in rules]

        header = ["Regla"] + list(results[0].keys())
        empty_data = [[str(r), "", "", "", ""] for r in rules]
        rules_table = Table(empty_data, header=header)

        q = Paragraphs([Text("Calcule el soporte, cobertura, confianza, e interés de las siguientes reglas:"),
                        rules_table,
                       Text("Presentar los resultados en forma de tabla, e incluir los cálculos realizados en la hoja.")])

        def format_row(r: Rule, res: dict):
            values = [f"{v:.3f}" for v in res.values()]
            return [str(r)] + values

        data = [format_row(r, res) for r, res in zip(rules, results)]
        a = Table(data, header=header)
        return q, a

    def title(self):
        return "Métricas de Reglas"
