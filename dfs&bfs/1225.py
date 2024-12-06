# 앞으로 dfs는 자바로 풀 것...

from collections import deque
import sys
input = sys.stdin.readline

def dfs(adj, x):
    stack = deque([(x, 1)])
    visited = set()
    maxDepth = 0
    
    while stack:
        node, depth = stack.pop()
        if not node in visited:
            visited.add(node)
            maxDepth = max(maxDepth, depth)
            
            for neighbor in adj[node]:
                if not neighbor in visited:
                    stack.append((neighbor, depth + 1))
            
    return maxDepth
                    

N, M = map(int, input().strip().split())
adjList = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().strip().split())
    adjList[b].append(a)

rst = []
for i in range(1, N+1):
    rst.append([i, dfs(adjList, i)])
    
md = max(rst, key=lambda x:x[1])[1]
max_node = [node[0] for node in rst if node[1] == md]
for i in max_node:
    print(i, end=" ")