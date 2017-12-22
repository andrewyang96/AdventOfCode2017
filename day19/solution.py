from typing import List

def get_letters(grid: List[List[str]]) -> str:
    i_dir, j_dir = 1, 0
    i, j = 0, grid[0].index('|')
    height, width = len(grid), len(grid[0])
    letters_encontered = ''
    while i >= 0 and i < height and j >= 0 and j < width:
        char = grid[i][j]
        if char == '+':
            if i_dir == 0:
                if i > 0 and grid[i-1][j] != ' ':
                    i_dir, j_dir = -1, 0
                elif i < height-1 and grid[i+1][j] != ' ':
                    i_dir, j_dir = 1, 0
                else:
                    raise ValueError('Invalid rotation')
            elif j_dir == 0:
                if j > 0 and grid[i][j-1] != ' ':
                    i_dir, j_dir = 0, -1
                elif j < width-1 and grid[i][j+1] != ' ':
                    i_dir, j_dir = 0, 1
                else:
                    raise ValueError('Invalid rotation')
            else:
                raise ValueError('One of i_dir and j_dir must be 0')
        elif 'A' <= char <= 'Z':
            letters_encontered += char
        i += i_dir
        j += j_dir
    return letters_encontered

def get_num_steps(grid: List[List[str]]) -> int:
    i_dir, j_dir = 1, 0
    i, j = 0, grid[0].index('|')
    height, width = len(grid), len(grid[0])
    num_steps = -1
    while i >= 0 and i < height and j >= 0 and j < width:
        char = grid[i][j]
        if char == '+':
            if i_dir == 0:
                if i > 0 and grid[i-1][j] != ' ':
                    i_dir, j_dir = -1, 0
                elif i < height-1 and grid[i+1][j] != ' ':
                    i_dir, j_dir = 1, 0
                else:
                    raise ValueError('Invalid rotation')
            elif j_dir == 0:
                if j > 0 and grid[i][j-1] != ' ':
                    i_dir, j_dir = 0, -1
                elif j < width-1 and grid[i][j+1] != ' ':
                    i_dir, j_dir = 0, 1
                else:
                    raise ValueError('Invalid rotation')
            else:
                raise ValueError('One of i_dir and j_dir must be 0')
        i += i_dir
        j += j_dir
        num_steps += 1
    return num_steps
