from _collections import deque

op = []

def solution(encrypted_text, key, rotation):
    answer = ''

    de = deque(encrypted_text)
    for _ in range(abs(rotation)):
        if rotation > 0:
            de.append(de.popleft())
        else:
            de.appendleft(de.pop())


    for i, j in zip(de, key):
        n = ord(i) + -(ord(j) - ord('a') + 1)
        if n < ord('a'):
            n += 26
        answer += chr(n)
    print(answer)
    return answer


solution("qyyigoptvfb", "abcdefghijk", 3)