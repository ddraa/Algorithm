def solution(n, t, m, timetable):
    answer = False
    timetable.sort()
    time, bus_time = [], []
    for i in timetable:
        time.append(int(i[:2])*60 + int(i[3:]))
    for i in range(n):
        bus_time.append(540+i*t)
    for bus in bus_time:
        rest_sit = m
        go = []
        while time and rest_sit>0 and time[0] <= bus: # in bus time, del queue unit
            go.append(time.pop(0))
            rest_sit -= 1

    if rest_sit>0: # last bus can
        answer = bus_time[-1]
    else:
        if go:
            answer = go[-1]-1 # just before the last
        else: # not take yet
            answer = bus_time[-1]
    q, r = divmod(answer,60)
    q = "0"+str(q) if q<10 else str(q)
    r = "0"+str(r) if r<10 else str(r)
    answer = q+':'+r
    return answer