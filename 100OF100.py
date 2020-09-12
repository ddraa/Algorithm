def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    i = 0
    while i < len(new_id):
        if not (new_id[i] == '.' or new_id[i].isalpha() or new_id[i].isdigit() or new_id[i] == '-' or new_id[i] == '_'):
            new_id = new_id[:i] + new_id[i+1:]
            i -= 1
        i += 1
    i = 0
    print(new_id)
    while i < len(new_id)-1: #  .. -> .
        if new_id[i] == '.':
            k = 1
            while i+k < len(new_id) and new_id[i+k] == '.':
                k += 1
            new_id = new_id[:i+1] + new_id[i+k:]
        i += 1

    print(new_id)
    if new_id[0] == '.':
        new_id = new_id[1:]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    print(new_id)
    if not new_id: # 빈 문자열
        new_id = "a"
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    if len(new_id) <= 2:
        t = new_id[-1]
        while len(new_id != 3):
            new_id += t
    print(new_id)


    return new_id

solution("...!@BaT#*..y.abcdefghijklm")