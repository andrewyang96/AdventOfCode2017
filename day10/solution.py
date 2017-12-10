from functools import reduce
from typing import List

def knot_hash(list_size: int, lens: List[int]) -> int:
    nums = list(range(list_size))
    curr_pos = 0
    skip_size = 0
    for length in lens:
        if curr_pos + length <= list_size:
            nums[curr_pos:curr_pos+length] = reversed(nums[curr_pos:curr_pos+length])
        else:
            # wraparound
            for i, num in enumerate(reversed(nums[curr_pos:] + nums[:(curr_pos+length)%list_size])):
                nums[(curr_pos+i)%list_size] = num
        curr_pos = (curr_pos + length + skip_size) % list_size
        skip_size += 1
    return nums[0] * nums[1]

def knot_hash2(input_str: str) -> str:
    sparse_hash = list(range(256))
    lens = [ord(char) for char in input_str] + [17, 31, 73, 47, 23]
    curr_pos = 0
    skip_size = 0

    # run 64 rounds of knot hash to obtain sparse hash
    for rnd in range(64):
        for length in lens:
            if curr_pos + length <= 256:
                sparse_hash[curr_pos:curr_pos+length] = reversed(sparse_hash[curr_pos:curr_pos+length])
            else:
                # wraparound
                for i, num in enumerate(reversed(sparse_hash[curr_pos:] + sparse_hash[:(curr_pos+length)%256])):
                    sparse_hash[(curr_pos+i)%256] = num
            curr_pos = (curr_pos + length + skip_size) % 256
            skip_size += 1

    # make dense hash
    dense_hash = []
    for i in range(16):
        dense_hash.append(sparse_hash[i*16])
        for j in range(1, 16):
            dense_hash[i] ^= sparse_hash[i*16+j]

    # return hexadecmial hash
    return reduce(lambda x, y: x + y, map(lambda num: format(num, 'x').zfill(2), dense_hash))
