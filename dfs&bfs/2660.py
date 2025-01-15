'''
시도 횟수 : 2
참고 여부 : O
최단거리는 BFS! 이거 최단거리였는데 너무 생각 없이 품ㅠ
'''

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

while 1:
    a, b = map(int, input().split())
    
    if a == -1:
        break
    
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(x):
    queue = deque([(x, 0)])
    visited = [-1]*(N+1)
    visited[x] = 0
    
    while queue:
        x, depth = queue.popleft()
        
        for nx in graph[x]:
            if visited[nx] == -1:
                queue.append((nx, depth+1))
                visited[nx] = depth+1
    
    return max(v for v in visited[1:] if v != -1)
    
ans = [0]*(N+1)
for i in range(1, N+1):
    ans[i] = bfs(i)

candidate = []
min_val = min(ans[1:])
for i in range(1, N+1):
    if ans[i] == min_val:
        candidate.append(i)

print(min_val, len(candidate))
for i in candidate:
    print(i, end=" ")    
                  