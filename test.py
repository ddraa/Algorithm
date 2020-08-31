from _collections import deque

arr = [1,4,5,7]
target = 15

c_list = []
def bfs(s, c):
    queue = deque()
    queue.append([s, c])
    while queue:
        s, c = queue.popleft()
        if s == target:
            c_list.append(c+1)
            return
        elif s < target:
            for k in arr:
                queue.append([s+k, c+1])

for i in arr:
    bfs(i, 0)
print(min(c_list))