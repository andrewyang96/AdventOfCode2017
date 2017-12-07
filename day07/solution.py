from typing import Dict

class Node(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = set()

def bottom_program(programs: Dict[str, Node]) -> str:
    potential_roots = set(programs.keys())
    for name in programs:
        potential_roots -= programs[name].children
    if len(potential_roots) != 1:
        raise ValueError('Must have exactly one program remaining: {0}'.format(potential_roots))
    return potential_roots.pop()
