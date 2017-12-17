from functools import reduce

def knot_hash2(input_str: str) -> str:
    # copied from day 10
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

def get_num_used_squares(input_str: str) -> int:
    num_used_squares = 0
    for i in range(128):
        kn = knot_hash2('{0}-{1}'.format(input_str, i))
        num_used_squares += sum(char == '1' for char in format(int(kn, 16), 'b'))
    return num_used_squares

def get_num_contiguous_regions(input_str: str) -> int:
    grid = [[False] * 128 for _ in range(128)]

    # populate grid
    for i in range(128):
        kn = knot_hash2('{0}-{1}'.format(input_str, i))
        grid[i] = [char == '1' for char in format(int(kn, 16), 'b').zfill(128)]

    def do_search(grid, i, j, visited_coords):
        if i < 0 or i >= 128:
            return 0
        if j < 0 or j >= 128:
            return 0
        if not grid[i][j]:
            return 0
        if (i, j) in visited_coords:
            return 0
        visited_coords.add((i, j))
        do_search(grid, i+1, j, visited_coords)
        do_search(grid, i-1, j, visited_coords)
        do_search(grid, i, j+1, visited_coords)
        do_search(grid, i, j-1, visited_coords)
        return 1

    # count num contiguous True regions
    visited_coords = set()
    num_regions = 0
    for i in range(128):
        for j in range(128):
            num_regions += do_search(grid, i, j, visited_coords)
    return num_regions
