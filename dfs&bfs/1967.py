# 노드 간 최장 거리 구할 때, 시간초과 안 뜨려면 dfs에서 한 번 돌리고
# 거기서 가장 먼 노드에서 dfs 한 번 더 돌려야 함을 알게 됨 

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [ [] for _ in range(N+1)]

for _ in range(N-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dfs(x):
    stack = deque([(x, 0)])
    visited = [-1]*(N + 1)
    visited[x] = 0
    
    while stack:
        x, w = stack.pop()
        
        for nx, nw in graph[x]:
            if visited[nx] < 0:
                visited[nx] = visited[x] + nw
                stack.append((nx, nw))
                
    return visited            

temp = dfs(1)
start = temp.index(max(temp))

ans = dfs(start)
print(max(ans))