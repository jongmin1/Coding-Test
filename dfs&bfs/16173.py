'''
시도 횟수 : 2
참고 여부 : X
visited 사용 안 해도 될 거 같아도 쓰자. 겹치면 메모리 초과 뜸
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0]
dy = [0, 1]

def bfs(x, y):
    q = deque([(x, y)])
    visited = [[False]*N for _ in range(N)]
    while q:
        x, y = q.popleft()
        if (x, y) == (N-1, N-1):
            return True
        
        for i in range(2):
            nx = x + dx[i]*grid[x][y]
            ny = y + dy[i]*grid[x][y]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
    
    return False

if bfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")
                
   