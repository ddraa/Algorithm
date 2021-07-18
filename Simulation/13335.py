import sys

N, W, L = map(int, sys.stdin.readline().split())
trucks = list(map(int, sys.stdin.readline().split()))

time = {i : 0 for i in range(N)}
bridge = set()
i, t = 0, 0
while i < N:
    weight = trucks[i]
    if L - weight >= 0:
        L -= weight
        bridge.add(i)
    else:
        i -= 1

    removed = set()
    for truck in bridge:
        time[truck] += 1
        if time[truck] == W:
            removed.add(truck)
            L += trucks[truck]
    bridge -= removed
    t += 1
    i += 1

print(t + W)