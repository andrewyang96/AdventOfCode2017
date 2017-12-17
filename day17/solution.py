from tqdm import trange

def spinlock(num_steps: int) -> int:
    buffer = [0]
    idx = 0
    for i in range(1, 2018):
        idx = (idx + num_steps) % len(buffer)
        buffer.insert(idx + 1, i)
        idx += 1
    return buffer[buffer.index(2017) + 1]

def spinlock2(num_steps: int) -> int:
    n = 0
    idx = 0
    for i in trange(1, 50000001):
        idx = (idx + num_steps) % i
        if idx == 0:
            n = i
        idx += 1
    return n
