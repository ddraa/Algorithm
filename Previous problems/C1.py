
MAX = float('-inf')
def convert(number, b):
    H = "0123456789ABCDEF"
    q, r = divmod(number, b)
    if q == 0:
        return H[r]
    else:
        return convert(q, b) + H[r]


def solution(N):
    global MAX
    for base in range(2,10): # 2 ~ 9
        b_n = list(map(int, convert(N, base)))
        m = 1
        for i in range(len(b_n)):
            if b_n[i] != 0:
                m *= b_n[i]
        if MAX <= m:
            MAX = m
            k = base
    print([k, MAX])
    return [k, MAX]

solution(10)