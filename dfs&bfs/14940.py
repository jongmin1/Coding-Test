# 갈 필요 없는 곳에 대한 케이스는 생각하지 않음
# 안전하게 싹다 하기! 참 아쉽네...

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
map = [[-1]*M for _ in range(N)]

dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1] 

def bfs(x, y):
    que = deque()
    que.append((x, y))
    map[x][y] = 0
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if map[nx][ny] == -1:
                if graph[nx][ny] == 1:
                    que.append((nx, ny))
                    map[nx][ny] = map[x][y] + 1
                    
                elif graph[nx][ny] == 0:
                    map[nx][ny] = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            bfs(i, j)
            
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(0, end=' ')  # 만약 들어가지 못한 곳이지만, 그 안에 0이 있으면 그거 -1로 찍혀있음
        else:
            print(map[i][j], end=' ')
    print()