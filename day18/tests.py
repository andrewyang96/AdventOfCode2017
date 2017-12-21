from solution import recover_sound

def process_file(f):
    return [tuple(line.strip().split()) for line in f]

with open('test_input.txt', 'r') as f:
    test_instructions = process_file(f)

with open('input.txt', 'r') as f:
    instructions = process_file(f)

assert recover_sound(test_instructions) == 4
print(recover_sound(instructions))
