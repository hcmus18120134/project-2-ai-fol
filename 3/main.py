import os
import sys
from knowledge import KnowledgeBase
from utils import GeneralParser

id = f'{int(sys.argv[1]) :02d}'
root = 'test/'

inp = os.path.join(root, id,  'knowledge.pl')
query = os.path.join(root, id, 'query.pl')
out = os.path.join(root, id,  'answers.txt')

kb = KnowledgeBase()
if __name__ == "__main__":
    with open(inp, 'r') as f:
        for sentence in f.readlines():
            if sentence == '\n':
                continue
            res = GeneralParser(sentence)
            if res[0]:
                kb.add_fact(res[1])
            else:
                kb.add_rule(res[1])
    # kb.viz()
    kb.solve()
    print('\n - - - - Initializing database - - - -  \n')

    kb.show_facts()
    print('\n - - - - - Analysing query - - - - - - \n')

    with open(query, 'r') as f:
        with open(out, 'w') as f_out:
            for query_str in f.readlines():
                if query_str == '\n':
                    continue
                _, alpha = GeneralParser(query_str)
                print(kb.query(alpha))
                f_out.write(query_str.split('\n')[0] + '\n')
                results = kb.query(alpha)

                for res in results:
                    f_out.write(list(res.keys())[0] +
                                ' = ' + list(res.values())[0] + '\n')
                f_out.write('\n')

    print('\n - - - - - - - - Done - - - - - - - - \n')
