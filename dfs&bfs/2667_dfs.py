# 단지내 집의 수
def dfs(graph, x, y, n, count=[0]):
    if x <= -1 or x >= n or y >= n or y <= -1:
        return False    
    
    if graph[x][y] > 0:
        graph[x][y] = -1
        count[0] += 1
        
        dfs(graph, x-1, y, n, count)
        dfs(graph, x+1, y, n, count)
        dfs(graph, x, y-1, n, count)
        dfs(graph, x, y+1, n, count)
        return count[0]
    
    return count[0]


N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# visited = [False]*(N+1)
result = []
for i in range(N):
    for j in range(N):
        c = [0]
        if graph[i][j] > 0:
            result.append(dfs(graph, i, j, N, c))
            
print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])
    