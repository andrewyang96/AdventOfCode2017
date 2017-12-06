from typing import List

def iterate(l: List[int]) -> List[int]:
    next_l = l[:]
    idx = next_l.index(max(next_l))
    next_l[idx] = 0
    for i in range(l[idx]):
        next_l[(idx+i+1) % len(next_l)] += 1
    return next_l

def serialize(l: List[int]) -> str:
    return ','.join(map(str, l))

def reallocate(l: List[int]) -> int:
    seen = set([serialize(l)])
    next_l = iterate(l)
    while serialize(next_l) not in seen:
        seen.add(serialize(next_l))
        l = next_l
        next_l = iterate(l)
    return len(seen)

def reallocate2(l: List[int]) -> int:
    seen = {serialize(l) : 0}
    next_l = iterate(l)
    while serialize(next_l) not in seen:
        seen[serialize(l)] = len(seen)
        l = next_l
        next_l = iterate(l)
    return len(seen) - seen[serialize(next_l)] + 1
