from forward_chaining import forward_chaining
from utils import unify


class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def query(self, alpha):
        res = []
        for fact in self.facts:
            phi = unify(fact, alpha, dict())
            if phi:
                res.append(phi)
        return res

    def solve(self):
        return forward_chaining(self)

    def show_facts(self):
        for x in self.facts:
            print(vars(x))

    def viz(self):
        print('============ FACTS ==============')
        for f in self.facts:
            print(f.func_name)
            print(f.args)
        print('============ RULES ==============')

        for f in self.rules:
            print(f.main.func_name)
            print(f.main.args)
            for g in f.mapping:
                print('--', g.func_name)
                print('--', g.args)
        print('=================================')
