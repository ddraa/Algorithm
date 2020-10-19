import sys
sys.setrecursionlimit(10**8)
visited = {}
COUNT = 0
def dfs(dic, depar, hub, dest):
    global COUNT
    if depar == dest:
        if hub in visited:
            COUNT += 1
        return
    for ad in dic[depar]:
        if ad not in visited:
            visited[ad] = True
            dfs(dic, ad, hub,dest)
            del visited[ad]


def solution(depar, hub, dest, roads):
    dic = {}
    for r in roads:
        if r[0] in dic:
            dic[r[0]].append(r[1])
            dic[r[0]] = [r[1]]
        else:
            dic[r[0]] = [r[1]]
    visited[depar] = True
    dfs(dic, depar, hub, dest)
    return COUNT % 10007


print(solution("ULSAN"	,"SEOUL"	,"BUSAN"	,[["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]	))