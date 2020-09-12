def toSec(h,m,s):
    return 3600*h + 60*m + s
def toTime(s):
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return h, m, s
def solution(play_time, adv_time, logs):
    answer = ''
    play_time = toSec(int(play_time[:2]), int(play_time[3:5]), int(play_time[6:]))
    adv_time = toSec(int(adv_time[:2]), int(adv_time[3:5]), int(adv_time[6:]))

    check = []
    start_time = [0]
    search = {}
    esearch = {}
    for i in logs:
        start = toSec(int(i[:2]), int(i[3:5]), int(i[6:8]))
        end = toSec(int(i[9:11]), int(i[12:14]), int(i[15:]))
        start_time.append(start)
        check.append(start)
        check.append(end)
        search[start] = end
        esearch[end] = start
    check.sort()
    start_time.sort()
    #print(log)
    #print(search)



    #for i in start_list:
        #print(i)
    #print(check)
    MAX = 0
    answer = 0
    for ad_start in start_time: # 정답 리스트들 중 하
        #print(ad_start)
        ad_end = ad_start + adv_time
        people = 0
        noo = 0
        cur_time = ad_start
        past_time = ad_start
        #print(toTime(ad_start), toTime(ad_end), "일 때 입니다")

        for l in check:
            if l in start_time:  # l is start time
                e = search[l]
                if not (l >= ad_end or e <= ad_start):  # in range
                    cur_time = l
                    noo += (cur_time - past_time) * people
                    people += 1
                    past_time = cur_time

            else:  # l is end time
                s = esearch[l]
                if not (s >= ad_end or l <= ad_start):
                    cur_time = l
                    noo += (cur_time - past_time) * people
                    people -= 1
                    past_time = cur_time
        print(toTime(ad_start), noo)

        if MAX < noo:
            MAX = noo
            answer = ad_start
    h, m, s = toTime(answer)
    #print(h, m, s)

    answer = ""
    if h < 10:
        answer += "0"+str(h) +':'
    else:
        answer += str(h) + ':'
    if m < 10:
        answer += '0'+str(m) +':'
    else:
        answer += str(m) + ':'
    if s < 10:
        answer += '0' + str (s)
    else:
        answer += str(s)
    print(answer)

    return answer

solution("99:59:59"	,"25:00:00"	,["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]	)