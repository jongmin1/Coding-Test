'''
시도 횟수 : 1
참고 여부 : O
벽부수기랑 헷갈려... 이런 유형 이렇게 푸는구나 하고 알게 됨!
'''

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
grid = [list(input().strip()) for _ in range(N)]

visited = [[-1]*N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    q = deque([(0, 0)])
    visited[0][0] = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if grid[nx][ny] == '1':
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

bfs()
print(visited[N-1][N-1])