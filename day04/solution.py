from collections import Counter
from typing import List

def valid(passphrases: List[List[str]]) -> int:
    return sum(len(set(line)) == len(line) for line in passphrases)

def valid2(passphrases: List[List[str]]) -> int:
    return sum(
        len(set(line)) == len(line) 
        for line in map(
            lambda line: [
                frozenset(Counter(passphrase).items()) for passphrase in line
            ], passphrases
        )
    )
