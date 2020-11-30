import itertools
from entity import Entity, Fact, Rule
from utils import unify, copy


def SUBST(exp_1, exp_2):

    if len(exp_1) != len(exp_2):
        return False

    for f1, f2 in zip(exp_1, exp_2):
        if f1.func_name != f2.func_name:
            return False
    # pdb.set_trace()
    return unify(exp_1, exp_2, dict())


def forward_chaining(kb, depth=-1):
    while True:
        new_facts = set()
        for rule in kb.rules:
            num_premises = len(rule.mapping)
            potential_facts = kb.facts

            potential_premises = list(itertools.permutations(
                potential_facts, num_premises))
            for tuple_premises in potential_premises:
                premises = [premise for premise in tuple_premises]
                theta = SUBST(rule.mapping, premises)
                if not theta:
                    continue
                # pdb.set_trace()
                new_fact = Fact(copy(rule.main))
                for idx, arg in enumerate(new_fact.args):
                    if arg in theta.keys():
                        new_fact.args[idx] = theta[arg]

                if new_fact not in new_facts and new_fact not in kb.facts:
                    new_facts.add(new_fact)
        if not new_facts:
            return
        kb.facts.update(new_facts)
