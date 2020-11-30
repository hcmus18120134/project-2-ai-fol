from entity import Entity, Fact, Rule
import os
import pickle
import pdb


def copy(obj): return pickle.loads(pickle.dumps(obj))


objs = set()


def GeneralParser(sentence: str, tokenizer: str = ':-'):
    components = sentence.split(tokenizer)
    is_fact = (len(components) == 1)
    components[-1] = components[-1].split('.')[0]
    if is_fact:
        components = Fact.parse(components[0])
        for obj in components.args:
            objs.add(obj)
    else:
        components = Rule.parse(components)
    return (is_fact, components)


def unify(x, y, theta: dict):
    if theta is False:
        return False
    if x == y:        # i.e: Parent = Parent, z = z, Mary = Mary
        return theta
    if is_variable(x):
        return unify_var(x, y, theta)
    if is_variable(y):
        return unify_var(y, x, theta)
    if is_fact(x) and is_fact(y):
        return unify(x.args, y.args, unify(x.func_name, y.func_name, theta))
    if is_list(x) and is_list(y) and len(x) == len(y):
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    return False


def unify_var(var, x, theta: dict):
    if var in theta.keys():
        return unify(theta[var], x, theta)
    if x in theta.keys():
        return unify(var, theta[x], theta)
    theta[var] = x
    return theta


def is_variable(x):
    return isinstance(x, str) and x[0].isupper()


def is_fact(x):
    return isinstance(x, Entity)


def is_list(x):
    return isinstance(x, list)
