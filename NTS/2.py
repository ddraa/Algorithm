def solution(drum):
    N = len(drum)
    ans = 0
    visited = [[-1 for _ in range(N)] for _ in range(N)]

    for start in range(N):
        path = []
        sc = 0
        x, y = 0, start
        star = []

        while x < N and y < N:
            if visited[x][y] != -1: # visited before .. 이미 방문한곳을 재 방문했다면.. 결정을 해야한
                must_sc = visited[x][y] # 앞으로 무조건 만날 별의 개수를 더해야줘야 함
                if len(star) + visited[x][y] < 2: # ok
                    ans += 1


                # 갱신작업
                while path:
                    x, y = path.pop()
                    if star and (x, y) == star[-1]:
                        star.pop()
                        sc += 1
                    visited[x][y] = sc + must_sc
                break


            path.append((x, y)) # save path

            if drum[x][y] == '#':
                x += 1
            elif drum[x][y] == '>':
                y += 1
            elif drum[x][y] == '<':
                y -= 1
            else:
                star.append((x, y))
                x += 1

        else: # all path is new load..
            if len(star) < 2:
                ans += 1

            # 갱신작업
            while path:
                x, y = path.pop()
                if star and (x, y) == star[-1]:
                    star.pop()
                    sc += 1
                visited[x][y] = sc

    return ans


# print(solution(["######",
#  ">>#<#*",
#  "****##",
#  "****<<",
#  "######",
#  "######"])) # visited check 케이스

print(solution(["####<#",
">>#<#*",
"****##",
"***#<<",
"######",
"######"]))