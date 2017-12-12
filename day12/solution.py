from typing import Dict

class Node(object):
    def __init__(self, num):
        self.num = num
        self.neighbors = set()

with open('input.txt', 'r') as f:
    nodes = {}
    for line in f:
        num, neighbors = line.strip().split(' <-> ')
        num = int(num)
        nodes[num] = Node(num)
        nodes[num].neighbors = set(int(n) for n in neighbors.split(', '))

def count_connections_to_0(nodes: Dict[int, Node]) -> int:
    visited = set([0])
    queue = nodes[0].neighbors.copy()
    next_queue = set()
    while len(queue) > 0:
        for next_num in queue:
            if next_num in visited:
                continue
            visited.add(next_num)
            next_node = nodes[next_num]
            next_queue.update(next_node.neighbors)
        queue = next_queue
        next_queue = set()
    return len(visited)

def count_groups(nodes: Dict[int, Node]) -> int:
    num_groups = 0
    visited = set()
    for num, node in nodes.items():
        if num in visited:
            continue
        num_groups += 1
        queue = node.neighbors.copy()
        next_queue = set()
        while len(queue) > 0:
            for next_num in queue:
                if next_num in visited:
                    continue
                next_node = nodes[next_num]
                visited.add(next_num)
                next_queue.update(next_node.neighbors)
            queue = next_queue
            next_queue = set()
    return num_groups
