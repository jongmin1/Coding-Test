from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
dist = [[0]*M for i in range(N)]

for i in range(N):
    graph.append(list(map(str, input().strip())))
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    que = deque()
    que.append((x, y))
    visited = [[-1]*M for i in range(N)]
    visited[x][y] = 0
    lenRoute = 0
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            if graph[nx][ny] == 'L' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))
                lenRoute = max(lenRoute, visited[nx][ny])
    return lenRoute

rst = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            if  1 <= i < N-1 and 1 <= j < M-1:
                if graph[i-1][j] == "L" and graph[i+1][j] == "L":
                    continue
                if graph[i][j-1] == "L" and graph[i][j+1] == "L":
                    continue
            rst = max(rst, bfs(i, j))

print(rst)