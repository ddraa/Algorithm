def solution(line1, line2):
    answer = line1.count(line2)
    c = 1
    while True:
        string = ""
        for i, s in enumerate(line2):
            string += s
            if i == len(line2) - 1:
                break
            string += '_' * c

        if len(string) > len(line1):
            break

        for si in range(len(line1) - len(string) + 1):
            k, res = 0, 0

            while si + k < len(line1) and k < len(string):
                if string[k] == line1[si + k]:
                    res += 1
                    if res == len(line2):
                        answer += 1
                        break
                k += c + 1
        c += 1
    return answer

solution("abacaba", "acb")