from collections import Counter
from collections import defaultdict
from typing import Dict
from typing import Tuple

class Node(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.parent_name = None
        self.children = set() # names of children, if any

    def is_leaf(self):
        return len(self.children) == 0

def bottom_program(programs: Dict[str, Node]) -> str:
    potential_roots = set(programs.keys())
    for name in programs:
        potential_roots -= programs[name].children
    if len(potential_roots) != 1:
        raise ValueError('Must have exactly one program remaining: {0}'.format(potential_roots))
    return potential_roots.pop()

def balance(programs: Dict[str, Node], bottom_name: str) -> Tuple[str, int]:
    # returns the name of the corrected program and its corrected weight
    weights = {}
    def calculate_weight(name: str) -> int:
        if name in weights:
            return weights[name]
        weights[name] = programs[name].weight + sum(
            calculate_weight(child_name) for child_name in programs[name].children)
        return weights[name]
    calculate_weight(bottom_name)

    queue = [bottom_name]
    next_queue = []
    while len(queue) > 0:
        for name in queue:
            node = programs[name]
            if node.children:
                child_weights = [weights[child_name] for child_name in node.children]
                if len(set(child_weights)) == 2:
                    imbalanced_weight = max(child_weights) if child_weights.count(max(child_weights)) == 1 else min(child_weights)
                    target_weight = min(child_weights) if imbalanced_weight == max(child_weights) else max(child_weights)
                    for child_name in node.children:
                        print(weights[child_name], programs[child_name].weight)
                        print(target_weight, imbalanced_weight, child_weights)
                        if weights[child_name] == imbalanced_weight:
                            print([programs[n].weight for n in programs[child_name].children])
                            return (child_name,
                                programs[child_name].weight + target_weight - imbalanced_weight)
                elif len(set(child_weights)) >= 3:
                    print('More than one imbalance found')
            for child_name in node.children:
                next_queue.append(child_name)
        queue = next_queue
        next_queue = []
    raise ValueError('No imbalance found')
