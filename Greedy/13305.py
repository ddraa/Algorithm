N = int(input())
road = list(map(int, input().split()))
fuel = list(map(int, input().split()))

i = 0
s = 0
f = fuel[0]
while i < len(road):
    f = min(fuel[i], f)
    s += f * road[i]
    i += 1
print(s)