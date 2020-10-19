def solution(n, arr1, arr2):
    answer = []

    for i,j in zip(arr1, arr2):
        b1 = bin(i)[2:]
        b2 = bin(j)[2:]
        while len(b1) != n:
            b1 = '0' + b1
        while len(b2) != n:
            b2 = '0' + b2

        t = ""
        for k1, k2 in zip(b1, b2):
            if k1 == '0' and k2 == '0':
                t += ' '
            else:
                t += '#'
        answer.append(t)

    return answer

solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])