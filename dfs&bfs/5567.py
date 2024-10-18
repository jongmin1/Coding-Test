from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(graph)
visited = [0] * (N+1)
# dist의 거리가 2 이하인 노드의 개수 세기

dist = [0]*(N+1)

def dfs(start):
    que = deque()
    que.append(start)
    visited[start] = 1
    c = 0
    
    while que:
        v = que.pop()
        
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = 1
                que.append(i)
                c += 1
                dist[i] =  c

dfs(1) 
print(visited)       

print(visited)
        
        