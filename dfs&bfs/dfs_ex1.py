''' 이코테 Python 음료수 얼려먹기 '''
def dfs(graph, x, y, n, m):
    if x < 0 or x >= n or y < -1 or y >= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        dfs(graph, x-1, y, n, m)
        dfs(graph, x+1, y, n, m)
        dfs(graph, x, y-1, n, m)
        dfs(graph, x, y+1, n, m)
        return True
    return False

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
result = 0
for i in range(n):
    for j in range(m):
        if dfs(graph, i, j, n, m) == True:
            result += 1

print(result)