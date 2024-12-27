# 직전에 푼 트리의 지름과 입력 받는 거 말고 크게 다른 거 없는듯!
# 근데 티어가 g4 -> g2로 오른 이유가 뭐지 흠 

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [ [] for _ in range(N+1)]
for i in range(N):
    arr = list(map(int, input().split()))
    
    for j in range(1, len(arr)-1, 2):
        graph[arr[0]].append((arr[j], arr[j+1]))

def dfs(x):
    stack = deque([(x, 0)])
    visited = [-1]*(N+1)
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
