from collections import deque

def bfs(graph, start, visitedBFS):
    count = 0
    
    que = deque([start])
    visitedBFS[start] = True
    
    while que:
        v = que.popleft()
        count += 1
        
        for i in graph[v]:
            if not visitedBFS[i]:
                que.append(i)
                visitedBFS[i] = True
    return count

def dfs(graph, v, visitedDFS, c=[0]):
    c[0] += 1
    visited[v] = True
    
    for i in graph[v]:
        if not visitedDFS[i]:
            dfs(graph, i, visitedDFS)
    return c[0]

N = int(input())
V = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(V):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False]*(N+1)

print(bfs(graph, 1, visited) - 1)
print(dfs(graph, 1, visited) - 1)
