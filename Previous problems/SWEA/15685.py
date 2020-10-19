K = int(input())
MAP = {}
def set_index(di):
    if di == 0:
        return 0, 1
    elif di == 1:
        return -1, 0
    elif di == 2:
        return 0, -1
    else:
        return 1, 0

for _ in range(K):
    stack = []
    x, y, d, g = map(int, input().split())
    tx, ty = set_index(d)
    stack.append([y, x]) # 0 gen
    stack.append([y+tx, x+ty]) # init

    gen = 1
    while gen <= g:
        la_idx = len(stack)-1
        c_x, c_y = stack[la_idx] # center
        la_idx -= 1
        temp = []
        while la_idx >= 0:
            ax, ay = stack[la_idx] # before
            dx = ax - c_x
            dy = ay - c_y

            new_x = c_x + dy
            new_y = c_y - dx

            temp.append([new_x, new_y])
            la_idx -= 1
        stack = stack + temp
        gen += 1
    for i in stack:
        x, y = i
        MAP[f'{x},{y}'] = True
count = 0
for l in MAP:
    x, y = map(int, l.split(','))
    if f'{x+1},{y}' in MAP and f'{x+1},{y+1}' in MAP and f'{x},{y+1}' in MAP:
        count += 1
print(count)