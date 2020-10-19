def convert(number, b):
    H = "0123456789ABCDEF"
    q, r = divmod(number, b)
    if q == 0:
        return H[r]
    else:
        return convert(q, b) + H[r]

def solution(n):
    return int("".join(reversed(convert(n, 3))), 3)