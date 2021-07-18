import sys

N, K = map(int, sys.stdin.readline().split())
order = list(map(int, sys.stdin.readline().split()))
plug = set()

def index_update(digit):
    index[digit] -= 1
    if index[digit] == 0:
        del index[digit]
    return

index = {}
for i in order:
    if i in index:
        index[i] += 1
    else:
        index[i] = 1
res = 0

for i in range(K):
    if len(plug) < N:
        if order[i] not in plug:
            plug.add(order[i])
        index_update(order[i])
    else:
        if order[i] not in plug:
            res += 1
            MAX = -1
            for p in plug:
                try:
                    MAX = max(MAX, order.index(p, i))
                except:
                    plug.remove(p)
                    break
            else:
                plug.remove(order[MAX])

            plug.add(order[i])
            index_update(order[i])

        else:
            index_update(order[i])
print(res)
