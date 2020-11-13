def solution(n, horizontal):
    answer = [[0] * n for _ in range(n)]
    if n == 1:
        return answer

    t = 0
    i, j = 0, 0
    cross = 2

    if horizontal:
        right = True
        reverse = False
    else:
        right = False
        reverse = False

    while True:
        if cross == n + 1: # center check
            cross -= 2
            reverse = True
            if not right:
                right = True
            else:
                right = False

        if right and not reverse:
            if answer[n-1][n-1] != 0:
                break
            j += 1
            t += 1
            answer[i][j] = t
            right = False
            if cross  <= n:
                for _ in range(cross - 1):
                    i += 1
                    j -= 1
                    t += 2
                    answer[i][j] = t
                cross += 1
            continue

        if not right and not reverse: # down
            if answer[n-1][n-1] != 0:
                break
            i += 1
            t += 1
            answer[i][j] = t
            right = True
            if cross <= n:
                for _ in range(cross - 1):
                    i -= 1
                    j += 1
                    t += 2
                    answer[i][j] = t
                cross += 1
            continue

        if right and reverse:
            if answer[n-1][n-1] != 0:
                break
            j += 1
            t += 1
            answer[i][j] = t
            right = False
            for _ in range(cross - 1):
                i -= 1
                j += 1
                t += 2
                answer[i][j] = t
            cross -= 1
            continue


        if not right and reverse:
            if answer[n-1][n-1] != 0:
                break
            i += 1
            t += 1
            answer[i][j] = t
            right = True
            for _ in range(cross - 1):
                i += 1
                j -= 1
                t += 2
                answer[i][j] = t
            cross -= 1
            continue
    return answer

s = solution(5, False)
for a in s:
    print(a)