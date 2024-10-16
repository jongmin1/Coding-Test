from collections import deque
import sys
input = sys.stdin.readline
            

N = int(input())
ans = []
for i in range(N):
    num = int(input())

    perm = []
    perm.append(list(k for k in range(1, num+1)))
    perm.append(list(map(int, input().split())))
        
    graph = [[] for _ in range(num+1)]
    visited = [0] * (num)
    
    for i in range(1, num+1):
        u = i
        v = perm[1][i-1]
        graph[u].append(v)
        graph[v].append(u)
    
    
    # for i in range(len(graph)):
    #     graph[i] = list(set(graph[i]))
    
    
    def dfs(graph, start):
        que = deque()
        que.append(start)
        
        while que:
            v = que.pop()
            
            if not visited[v]:
                visited[v] = 1
                que.extend(graph[v])
        return visited
    
    c = 0
    visitedSum = 0
    for i in range(1, num+1):
        visited = dfs(graph, i)
        if visitedSum != sum(visited):
            print(visited)
            c += 1
    
    ans.append(c)    
print(ans)