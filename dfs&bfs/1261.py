'''
시도 횟수 : 1
참고 여부 : X
어제 푼거랑 동일한 코드라...
'''

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]
visited = [[-1]*(M) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque([(0, 0)])
    visited[0][0] = 0
    
    while q:
        x, y = q.popleft()
        
        if x == N-1 and y == M-1:
            return
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                if grid[nx][ny] == "0":
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                elif grid[nx][ny] == "1":
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

bfs()
print(visited[N-1][M-1])