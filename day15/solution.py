from typing import Generator

def make_generator(start: int, factor: int) -> Generator[int, None, None]:
    value = start
    while True:
        value = (value * factor) % 2147483647
        yield value

def final_count(a_start: int, b_start: int, num_iters: int) -> int:
    gen_a = make_generator(a_start, 16807)
    gen_b = make_generator(b_start, 48271)
    count = 0
    mask = 2 ** 16 - 1
    for i in range(num_iters):
        value_a = next(gen_a)
        value_b = next(gen_b)
        count += (value_a & mask == value_b & mask)
    return count

def make_generator2(start: int, factor: int, multiple: int) -> Generator[int, None, None]:
    value = start
    while True:
        value = (value * factor) % 2147483647
        if value % multiple == 0:
            yield value

def final_count2(a_start: int, b_start: int, num_iters: int) -> int:
    gen_a = make_generator2(a_start, 16807, 4)
    gen_b = make_generator2(b_start, 48271, 8)
    count = 0
    mask = 2 ** 16 - 1
    for i in range(num_iters):
        value_a = next(gen_a)
        value_b = next(gen_b)
        count += (value_a & mask == value_b & mask)
    return count
