def convert(number, b):
    H = "0123456789ABCDEF"
    q, r = divmod(number, b)
    if q == 0:
        return H[r]
    else:
        return convert(q, b) + H[r]

# 2AF(16th) -> 4th .. . . . 16 -> 10 -> 4 process

t = int("2AF",16) # 16 -> 10
c = convert(t,2) # 10 -> 2
print(c)