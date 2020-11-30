import re


class Entity:
    def __init__(self, name: str, args: list):
        self.func_name = name
        self.args = args

    def __eq__(self, other):
        res = bool(self.func_name == other.func_name)
        res = bool(res and (len(self.args) == len(other.args)))
        if res:
            for idx in range(len(self.args)):
                if self.args[idx] != other.args[idx]:
                    return False

        return res

    def __hash__(self):
        return hash((self.func_name, *self.args))

    @staticmethod
    def parse(sentence: str):
        name, args = sentence.split('(')[:2]
        name = name.replace(' ', '')
        name = name.replace('\n', '')
        args = args.replace('.', '')

        args = args.replace(')', ',')
        args = args.replace(' ', ',')
        args = [x.strip() for x in args.split(',')]
        args = [x for x in args if x != '']
        return Entity(name=name, args=args)


class Fact(Entity):
    def __init__(self, obj: Entity):
        self.func_name = obj.func_name
        self.args = obj.args

    def __eq__(self, other):
        res = bool(self.func_name == other.func_name)
        res = bool(res and (len(self.args) == len(other.args)))
        if res:
            for idx in range(len(self.args)):
                if self.args[idx] != other.args[idx]:
                    return False

        return res

    def __hash__(self):
        return hash((self.func_name, *self.args))

    @staticmethod
    def parse(sentence: str):
        return Fact(Entity.parse(sentence))


class Rule:
    def __init__(self, main_func: Entity, mapping_funcs: list):
        self.main = main_func
        self.mapping = mapping_funcs

    @staticmethod
    def parse(components: list):
        main_func = Entity.parse(components[0])
        components = components[1].split('),')
        mapping_funcs = [Entity.parse(x) for x in components]
        return Rule(main_func, mapping_funcs)
