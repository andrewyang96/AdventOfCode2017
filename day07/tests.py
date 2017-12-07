import re
from solution import Node
from solution import bottom_program

pattern = re.compile(r'^(?P<name>\w+) \((?P<weight>\d+)\)( \-\> (?P<children>.*?))?$')

def process_file(f):
    programs = {}
    for line in f:
        match = pattern.match(line.strip())
        name, weight, children = match.group('name'), match.group('weight'), match.group('children')
        programs[name] = Node(name, int(weight))
        if children:
            programs[name].children = set(children.split(', '))
    return programs

with open('test_input.txt', 'r') as f:
    test_programs = process_file(f)

with open('input.txt', 'r') as f:
    programs = process_file(f)

assert bottom_program(test_programs) == 'tknk'
print(bottom_program(programs))
