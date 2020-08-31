def solution(lines):
    start_list, end_list, s_e = [], [], []
    for t in lines:
        l = t.split()
        minute_t1 = l[1].split('.')
        minute_t2 = minute_t1[0].split(':')
        seconds = 3600*int(minute_t2[0]) + 60*int(minute_t2[1]) + int(minute_t2[2])
        ms_t = l[2].split('.')
        if len(ms_t)>1:
            ms_tt = ms_t[1][:-1]
            if len(ms_tt) == 2:
                ms_tt += '0'
            elif len(ms_tt) == 1:
                ms_tt += '0'*2
            ms = int(ms_t[0] + ms_tt)
        else:
            ms = int(ms_t[0][0])*1000

        start_ms = seconds*1000+int(minute_t1[1]) - ms + 1
        end_list.append(seconds*1000 + int(minute_t1[1]))
        start_list.append(start_ms)
        s_e.append([start_ms, seconds*1000+int(minute_t1[1])])

    base_list = start_list + end_list
    base_list.sort()
    MAX = 0
    for i in base_list:
        start = i
        end = i + 999 # 1 min
        count = 0
        for k in s_e:
            if not (k[0] > end or k[1] < start):
                count += 1
        MAX = max(MAX,count)
    return MAX

