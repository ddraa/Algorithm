from _collections import deque
N = int(input())

def bfs(s):
    queue = deque()
    queue.append([s,0])
    visited = {s:True}
    while queue:
        n, c = queue.popleft()
        if n == 1:
            return c
        else:
            c += 1
            if n-1 not in visited:
                queue.append([n-1,c])
                visited[n-1] = True
            if n % 6 == 0:
                queue.append([n / 3, c])
                visited[n / 3] = True
                queue.append([n / 2, c])
                visited[n / 2] = True
            else:
                if n%3==0 and n/3 not in visited:
                    queue.append([n/3,c])
                    visited[n/3] = True
                elif n%2==0 and n/2 not in visited:
                    queue.append([n/2,c])
                    visited[n/2] = True

print(bfs(N))