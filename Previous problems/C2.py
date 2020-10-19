days = [31,28,31,30,31,30,31,31,30,31,30,31]
def solution(n, customers):
    answer = 0
    ki = {}
    for i in range(1, n+1):
        ki[i] = [0, 0] # sec, count
    for i in customers:
        t = i.split()
        md = list(map(int, t[0].split('/')))
        hms = list(map(int, t[1].split(':')))
        during = int(t[2]) * 60

        day = 0
        for k in range(0, 12):
            if md[0] >= k + 1:
                day += days[k]
        day += md[1] # date !

        sec = hms[0] * 3600 + hms[1] * 60 + hms[2] + day * 86400
        MAX = float('-inf')
        ## 운영되지 않은 시각 구하기
        kinum = 0
        for k in ki:
            if ki[k][0] <= sec: # 미운영 중이면
                if MAX < sec - ki[k][0]: # 미 운영중인 기간이 MAX보다 크면 ?
                    MAX = sec - ki[k][0]
                    kinum = k
        if kinum!=0: #미 운영중인 키오스크가 있으면
            ki[kinum][1] += 1
            ki[kinum][0] = sec + during # 끝나는 예상시간 저장
        else: # 모두 운영중이면
            MIN = float('inf')
            kinum = 0
            for k in ki:
                if MIN > ki[k][0] - sec:
                    MIN = ki[k][0] - sec
                    kinum = k
            ki[kinum][1] += 1
            ki[kinum][0] += during # 끝나는 예상시간 저장
    MAX = 0
    for n in ki:
        if ki[n][1] > MAX:
            MAX = ki[n][1]
    


print(solution(2, ["02/28 23:59:00 03","03/01 00:00:00 02", "03/01 00:05:00 01"]	))