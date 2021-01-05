from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
MIN = float('inf')
people = {x for x in range(1, N + 1)}

# divide team
teams = list(combinations(range(1, N + 1), N//2))

for idx, team in enumerate(teams):
    if idx == len(teams)//2:break
    link = people - set(team)
    s_score, l_score = 0, 0
    for i, j in combinations(team, 2):
        s_score += mat[i - 1][j - 1]
        s_score += mat[j - 1][i - 1]
    for i, j in combinations(link, 2):
        l_score += mat[i - 1][j - 1]
        l_score += mat[j - 1][i - 1]

    d = abs(s_score - l_score)
    if d < MIN:
        MIN = d
print(MIN)