def solution(penter, pexit, pescape, data):
    answer = ''
    n = len(penter)
    for i in range(0, len(data), n):
        part = data[i:i+n]
        if part in [penter, pexit, pescape]:
            answer += pescape + part
        else:
            answer += part
    return penter + answer + pexit

print(solution("1", "0", "1", "0000"))