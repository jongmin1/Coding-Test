from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
for i in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(N+1)
parent = [0]*(N+1)

def dfs(start):
    que = deque()
    que.append(start)
    visited[start] = True
    
    while que:
        now = que.pop()
        
        for v in graph[now]:
            if not visited[v]:
                parent[v] = now
                visited[v] = True
                que.append(v)

dfs(1)

for i in range(2, N+1):
    print(parent[i])
                