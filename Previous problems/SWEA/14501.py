import itertools

MAX = float('-inf')
N = int(input())
day = []
for i in range(1, N+1): # day[i] = [day, during, pay]
    day.append([i] + list(map(int, input().split())))
for i in range(1, N+1):
    com = itertools.combinations(day, i)

    for d in com:
        cur_time = d[0][0] # init cur time
        income = 0
        succeed = True
        for dd in d:
            if dd[0] >= cur_time:
                cur_time = dd[0] + dd[1]
                if cur_time > N + 1:
                    succeed = False
                    break
                income += dd[2]
            else:
                succeed = False
                break
        if succeed:
            if income > MAX:
                MAX = income
if MAX == float('-inf'):
    print(0)
else:
    print(MAX)
