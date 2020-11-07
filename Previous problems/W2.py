def oper(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    else:
        return a * b


def solution(s, op):
    answer = []

    for i in range(1, len(s)):
        l = s[:i]
        r = s[i:]
        answer.append(oper(int(l), int(r), op))

    return answer

print(solution("31402"	, "*"))