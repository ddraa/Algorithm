N = int(input())

def hanoi(n, frm, to, otr):
    if n == 1:
        print(frm, to)
        return
    else:
        hanoi(n-1, frm, otr, to)
        print(frm, to)
        hanoi(n-1, otr, to, frm)
print(2**N-1)
hanoi(N, 1, 3, 2)