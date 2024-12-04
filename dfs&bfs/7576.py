# 출발점이 다르고 bfs 한 번에 돌릴 때 

from collections import deque
import sys
input = sys.stdin.readline
INF = 1e9

M, N = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(N)]
box = [[0]*M for _ in range(N)]


que = deque()
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            que.append([i, j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while que:
    x, y = que.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
            
        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
            grid[nx][ny] = grid[x][y] + 1
            que.append([nx, ny])

def calDay():
    ans = 0
    for i in grid:
        for tomato in i:
            if tomato == 0:
                return -1
            ans = max(ans, tomato)
    return ans-1
print(calDay())