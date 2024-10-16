from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N + 1)

for i in range(N+1):
    graph[i].sort()

def bfs(start):
    que = deque()
    que.append(start)
    visited[start] = 1
    
    while que:
        node = que.popleft()
        
        for i in graph[node]:
            if visited[i]==0:
                visited[i] = 1
                que.append(i)
    
   
c = 0
visitedSum = sum(visited)
for i in range(1, N+1):
    bfs(i)
    t = sum(visited)
    if visitedSum != t:
        visitedSum = t 
        c += 1

print(c)