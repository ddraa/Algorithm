N = int(input())
star = [[' '] * N for _ in range(N)]

def stars(size, x, y):
    if size == 1:
        star[x][y] = '*'
    else:
        n_size = size // 3
        for dy in range(3):
            for dx in range(3):
                if not(dx == 1 and dy == 1):
                    stars(n_size, x + dx * n_size, y + dy * n_size)

stars(N, 0, 0)
for i in star:
    print("".join(i))