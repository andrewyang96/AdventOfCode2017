from typing import Dict
from typing import List
from typing import Tuple

def value_of(registers: Dict[str, int], x: str) -> int:
    try:
        return int(x)
    except ValueError:
        return registers.get(x, 0)

def recover_sound(instructions: List[Tuple[str, ...]]) -> int:
    last_played = None
    registers = {}
    i = 0
    while i >= 0 and i < len(instructions):
        ins = instructions[i]
        if ins[0] == 'snd':
            last_played = value_of(registers, ins[1])
        elif ins[0] == 'set':
            registers[ins[1]] = value_of(registers, ins[2])
        elif ins[0] == 'add':
            registers[ins[1]] = registers.get(ins[1], 0) + value_of(registers, ins[2])
        elif ins[0] == 'mul':
            registers[ins[1]] = registers.get(ins[1], 0) * value_of(registers, ins[2])
        elif ins[0] == 'mod':
            registers[ins[1]] = registers.get(ins[1], 0) % value_of(registers, ins[2])
        elif ins[0] == 'rcv':
            if value_of(registers, ins[1]) != 0:
                return last_played
        if ins[0] == 'jgz' and value_of(registers, ins[1]) > 0:
            i += value_of(registers, ins[2])
        else:
            i += 1
    raise ValueError('Nothing recovered')
