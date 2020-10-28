N = int(input())
for i in range(3):
    t = list()
    for _ in range(N):
        t.append(int(input()))

    if i == 0: # kor
        print(f'Kor) sum: {sum(t)}, avg: {round(sum(t)/float(N),2)}')
    elif i == 1: # eng
        print(f'Eng) sum: {sum(t)}, avg: {round(sum(t) / float(N), 2)}')
    else:
        print(f'Math) sum: {sum(t)}, avg: {round(sum(t) / float(N), 2)}')