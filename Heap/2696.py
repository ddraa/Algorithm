import sys, bisect
## 11 30

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        q = N // 10
        if N % 10 != 0:
            q += 1

        arr = []
        for _ in range(q):
            temp = list(map(int, sys.stdin.readline().split()))
            for t in temp:
                arr.append(t)
        q = []

        c = 0
        print((N + 1) // 2)
        for i, n in enumerate(arr):
            bisect.insort(q, n)
            if (i + 1) % 2 == 1:
                print(q[len(q) // 2], end=" ")
                c += 1
                if c == 10:
                    c = 0
                    print()
        print()
    return

if __name__ == '__main__':
    solve()