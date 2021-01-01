while True:
    l = list(map(int, input().split()))
    l.sort()
    a, b, c = l[0], l[1], l[2]
    if a == 0 and a == b and a == c:
        break
    print("right") if a ** 2 + b ** 2 == c ** 2 else print("wrong")