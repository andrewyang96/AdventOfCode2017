def captcha(num: str) -> int:
    count = 0
    for idx, digit in enumerate(num):
        next_digit = num[idx+1] if idx < len(num) - 1 else num[0]
        if digit == next_digit:
            count += int(digit)
    return count

def captcha2(num: str) -> int:
    count = 0
    for idx, digit in enumerate(num):
        other_digit = num[idx+len(num)//2] if idx < len(num) / 2 else num[idx-len(num)//2]
        if digit == other_digit:
            count += int(digit)
    return count
