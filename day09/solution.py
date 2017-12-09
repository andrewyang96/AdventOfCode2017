def group_score(stream: str) -> int:
    score = 0
    nesting = 0
    in_garbage = False
    cancel_next_char = False
    for char in stream:
        if in_garbage:
            if cancel_next_char:
                cancel_next_char = False
            elif char == '>':
                in_garbage = False
            elif char == '!':
                cancel_next_char = True
        elif char == '{':
            nesting += 1
            score += nesting
        elif char == '}':
            nesting -= 1
        elif char == '<':
            in_garbage = True
        # commas are ignored
    if nesting != 0:
        raise ValueError('Incorrectly formed: nesting is {0}'.format(nesting))
    return score

def count_canceled_chars(stream: str) -> int:
    num_canceled_chars = 0
    in_garbage = False
    cancel_next_char = False
    for char in stream:
        if in_garbage:
            if cancel_next_char:
                cancel_next_char = False
            elif char == '>':
                in_garbage = False
            elif char == '!':
                cancel_next_char = True
            else:
                num_canceled_chars += 1
        elif char == '<':
            in_garbage = True
    return num_canceled_chars
