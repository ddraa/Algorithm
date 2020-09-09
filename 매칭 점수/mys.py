import re

def solution(word, pages):
    word = word.lower()
    answer = 0
    dic = {}
    index = 0
    for i in pages:
        i = i.lower()
        t = i
        head_s = t.find("<head>")
        head_e = t.find("</head>") + 7
        #print(i[head_s:head_e])
        head = t[head_s : head_e]

        for m in re.finditer("<meta", head):
            temp = head[m.start():]
            meta_e = temp.find('>')
            meta = temp[:meta_e]
            if "https://" in meta:
                t_url = meta[meta.find("https://"):]
                url_e = t_url.find('"')
                url = t_url[8:url_e]
                dic[url] = []

        b_score = 0
        while word in t:
            idx = t.find(word)
            if not (t[idx-1].isalpha() or t[idx+len(word)].isalpha()):
                b_score += 1
            t = t[idx+1:]

        dic[url].append(b_score)
        t = i
        ex_count = 0
        ex = []
        for a in re.finditer("<a href", t):
            ex_count += 1
            temp = t[a.start():]
            ex.append(temp[17:temp.find('>')-1])

        dic[url].append(ex_count)
        dic[url].append(ex)
        dic[url].append(index)
        index += 1
    answer = []
    score_dic = {}
    for i in dic:
        dic[i].append(dic[i][0])
    print(dic)
    for i in dic:
        for ex in dic[i][2]:
            if ex in dic:
                dic[ex][4] += (dic[i][0] / dic[i][1])
    print(dic)
    MAX = 0
    for i in dic:
        if dic[i][4] > MAX:
            MAX = dic[i][4]
    for i in dic:
        if dic[i][4] == MAX:
            answer.append(dic[i][3])


    return min(answer)

print(solution("Muzi",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
))