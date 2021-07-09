import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    words = []
    for _ in range(N):
        words.append(sys.stdin.readline().rstrip())
    words.sort()

    for i in range(len(words) - 1):
        if words[i + 1].startswith(words[i]):
            print("NO")
            break
    else:
        print("YES")