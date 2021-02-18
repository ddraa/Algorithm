import sys

def KMPSearch(pat, txt):
    t = []
    M = len(pat)
    N = len(txt)

    lps = [0]*M

    computeLPS(pat, lps)

    i = 0  # index for txt[]
    j = 0  # index for pat[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        elif pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        if j == M:
            return True # efficiency
            j = lps[j-1]
    return False

def computeLPS(pat, lps):
    leng = 0

    i = 1
    while i < len(pat):
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i += 1

string = []
n, k = map(int, sys.stdin.readline().split())
for _ in range(n):
    input()
    string.append(sys.stdin.readline().split())
sample = string[0]

for i in range(len(sample) - k + 1):
    pattern = sample[i:i + k]
    c = 0
    for j in range(1, n):
        ans = KMPSearch(pattern, string[j])
        if not ans:
            ans = KMPSearch(list(reversed(pattern)), string[j])
            if not ans:
                break
            else:
                c += 1
        else:
            c += 1
    if c == n - 1:
        print("YES")
        exit(0)
print("NO")

