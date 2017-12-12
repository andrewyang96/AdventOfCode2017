from solution import count_connections_to_0
from solution import count_groups
from solution import Node

def process_file(f):
    nodes = {}
    for line in f:
        num, neighbors = line.strip().split(' <-> ')
        num = int(num)
        nodes[num] = Node(num)
        nodes[num].neighbors = set(int(n) for n in neighbors.split(', '))
    return nodes

with open('test_input.txt', 'r') as f:
    test_nodes = process_file(f)

with open('input.txt', 'r') as f:
    nodes = process_file(f)

assert count_connections_to_0(test_nodes) == 6
print(count_connections_to_0(nodes))

assert count_groups(test_nodes) == 2
print(count_groups(nodes))
