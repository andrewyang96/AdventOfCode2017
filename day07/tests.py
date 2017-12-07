import re
from solution import Node
from solution import bottom_program
from solution import balance

pattern = re.compile(r'^(?P<name>\w+) \((?P<weight>\d+)\)( \-\> (?P<children>.*?))?$')

def process_file(f):
    programs = {}
    parents = {} # maps child to parent
    for line in f:
        match = pattern.match(line.strip())
        name, weight, children = match.group('name'), match.group('weight'), match.group('children')
        programs[name] = Node(name, int(weight))
        if children:
            programs[name].children = set(children.split(', '))
    for child_name, parent_name in parents.items():
        programs[child_name].parent_name = parent_name
    return programs

with open('test_input.txt', 'r') as f:
    test_programs = process_file(f)

with open('input.txt', 'r') as f:
    programs = process_file(f)

assert bottom_program(test_programs) == 'tknk'
bottom_name = bottom_program(programs)
print(bottom_name)

assert balance(test_programs, 'tknk') == ('ugml', 60)
print(balance(programs, bottom_name))
