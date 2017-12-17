from tqdm import trange
from typing import List
from typing import Union

class SpinMove(object):
    def __init__(self, size):
        self.size = size

class ExchangeMove(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

class PartnerMove(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

def parse_dance_moves(input_str: str) -> List[Union[SpinMove, ExchangeMove, PartnerMove]]:
    dance_moves = []
    for s in input_str.split(','):
        if s[0] == 's':
            dance_moves.append(SpinMove(int(s[1:])))
        elif s[0] == 'x':
            a, b = map(int, s[1:].split('/'))
            dance_moves.append(ExchangeMove(a, b))
        elif s[0] == 'p':
            a, b = s[1:].split('/')
            dance_moves.append(PartnerMove(a, b))
        else:
            raise ValueError('{0} is not a valid move'.format(s))
    return dance_moves

def dance(programs: List[str], dance_moves: List[Union[SpinMove, ExchangeMove, PartnerMove]]) -> List[str]:
    for dance_move in dance_moves:
        if type(dance_move) == SpinMove:
            programs = programs[-dance_move.size:] + programs[:-dance_move.size]
        elif type(dance_move) == ExchangeMove:
            temp = programs[dance_move.b]
            programs[dance_move.b] = programs[dance_move.a]
            programs[dance_move.a] = temp
        elif type(dance_move) == PartnerMove:
            a = programs.index(dance_move.a)
            b = programs.index(dance_move.b)
            temp = programs[b]
            programs[b] = programs[a]
            programs[a] = temp
        else:
            raise ValueError('Encountered invalid move')
    return programs

def dance2(programs: List[str], dance_moves: List[Union[SpinMove, ExchangeMove, PartnerMove]], num_iters: int) -> List[str]:
    for _ in trange(num_iters):
        programs = dance(programs, dance_moves)
    return programs
