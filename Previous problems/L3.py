def solution(n):
    answer = []
    count = 0
    n = str(n)
    length = len(n)
    l = length // 2
    while l >= 0 :
        print(n)
        if len(n) > 2:
            a = int(n[:l])
            b = int(n[l:])
            c = int(n[:l+1])
            d = int(n[l+1:])
            #print(c, d)

            m1 = max(a, b)
            m2 = max(c, d)
            if m1>m2:
                x = c
                y = d
            else:
                x = a
                y = b

            result = x + y
            n = str(result)
            l = len(n) // 2
        elif len(n) == 2:
            a = int(n[:l])
            b = int(n[l:])
            s = str(a+b)
            if len(s) == 1:
                return count + 1, int(s)
            else:
                return count + 2, int(s[0]) + int(s[1])
        else: # len == 1
            return  count, int(n)

        count += 1
    return answer

print(solution(10007))