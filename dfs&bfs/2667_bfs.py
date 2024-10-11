from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y, n):
    que = deque()
    que.append((x, y)) 
    
    count = 0
    while que:
        nx, ny = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <= -1 or nx >= n or ny >= n or ny <= -1:
                continue
            
            if graph[nx][ny] > 0:
                count += 1
                graph[nx][ny] = -1
                que.append((nx, ny))
                               
    return count


N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] > 0:
            for k in range(N):
                print(graph[k])
            result.append(bfs(graph, i, j, N))
            print()
            
print(len(result))
for i in result:
    print(i)
    
        
