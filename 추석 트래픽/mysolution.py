from _collections import deque

def solution(lines):
    answer = 0
    queue = deque()
    start_list = []
    end_list = []
    for t in lines:
        l = t.split()
        minute_t1 = l[1].split('.')
        minute_t2 = minute_t1[0].split(':')
        seconds = 3600*int(minute_t2[0]) + 60*int(minute_t2[1]) + int(minute_t2[2])
        print(l)
        ms_t = l[2].split('.')
        ms_tt = ms_t[1][:-1]
        if len(ms_tt) == 2:
            ms_tt += '0'
        elif len(ms_tt) == 1:
            ms_tt += '0'*2
        ms = int(ms_t[0] + ms_tt)
        start_ms = seconds*1000 - ms + 1
        end_list.append(seconds*1000 + ms)
        start_list.append(start_ms)
    start_list.sort() # sort
    end_list.sort()
    start_time = start_list[0]

    print(start_list)
    MAX = 0
    for k in start_list:
        if k - start_time <= 1000:
            queue.append(k)
            MAX = max(MAX,len(queue))
        else:
            while queue and k - queue[0] > 1000:
                queue.popleft()
            if queue:
                start_time = queue[0]
            else:
                start_time = k
            queue.append(k)
            MAX = max(MAX,len(queue))
        print(queue)


    queue = deque()
    start_time = end_list[0]
    for k in end_list:
        if k - start_time <= 1000:
            queue.append(k)
            MAX = max(MAX,len(queue))
        else:
            while queue and k - queue[0] > 1000:
                queue.popleft()
            if queue:
                start_time = queue[0]
            else:
                start_time = k
            queue.append(k)
            MAX = max(MAX,len(queue))
        print(queue)
    return MAX







print(solution(["2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"]))