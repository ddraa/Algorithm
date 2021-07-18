import sys


def isCCW(p1, p2, p3):
    ret = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]
    ret = ret - (p1[1] * p2[0]) - (p2[1] * p3[0]) - (p3[1] * p1[0])

    if ret > 0:
        return 1
    elif ret < 0:
        return -1
    else:
        return 0


def CrossCheck(x1, y1, x2, y2, x3, y3, x4, y4):
    r1 = isCCW([x1, y1], [x2, y2], [x3, y3])
    r2 = isCCW([x1, y1], [x2, y2], [x4, y4])
    r3 = isCCW([x3, y3], [x4, y4], [x1, y1])
    r4 = isCCW([x3, y3], [x4, y4], [x2, y2])

    if r1 * r2 == 0 and r3 * r4 == 0:
        if [x1, y1] > [x2, y2]:
            x1, y1, x2, y2 = x2, y2, x1, y1
        if [x3, y3] > [x4, y4]:
            x3, y3, x4, y4 = x4, y4, x3, y3

        if [x1, y1] <= [x4, y4] and [x3, y3] <= [x2, y2]:
            return True
        else:
            return False

    if r1 * r2 <= 0 and r3 * r4 <= 0:
        return True
    else:
        return False


def get_crosspt(x11, y11, x12, y12, x21, y21, x22, y22):
    if x12 == x11 or x22 == x21:
        print('delta x=0')
        if x12 == x11:
            cx = x12
            m2 = (y22 - y21) / (x22 - x21)
            cy = m2 * (cx - x21) + y21
            return cx, cy

        if x22 == x21:
            cx = x22
            m1 = (y12 - y11) / (x12 - x11)
            cy = m1 * (cx - x11) + y11
            return cx, cy

    m1 = (y12 - y11) / (x12 - x11)
    m2 = (y22 - y21) / (x22 - x21)
    if m1 == m2:
        print('parallel')
        return None
    cx = (x11 * m1 - y11 - x21 * m2 + y21) / (m1 - m2)
    cy = m1 * (cx - x11) + y11

    return cx, cy


a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

res = CrossCheck(*a, *b)
if res:
    print(1)
    print(get_crosspt(*a, *b))
else:
    print(0)
