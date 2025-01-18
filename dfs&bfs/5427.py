'''
시도 횟수 : 2
참고 여부 : X
처음에 깜박하고 조건에 visited 추가하지 않아서 메모리 초과
'''

import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def valid(a, b):
    return 0 <= a < N and 0 <= b < M 
    

def bfs(now, fire):
    q_fire = fire
    q = now
    
    visited = [[False]*M for _ in range(N)]
    visited[now[0][0]][now[0][1]] = True
    
    while q:
        len_fire = len(fire)
        for _ in range(len_fire):
            fx, fy = q_fire.popleft()
            for i in range(4):
                nfx = fx + dx[i]
                nfy = fy + dy[i]
                
                if valid(nfx, nfy) and grid[nfx][nfy] == ".":
                    q_fire.append((nfx, nfy))
                    grid[nfx][nfy] = "*"
            
        len_q = len(q)
        for _ in range(len_q):
            x, y, depth = q.popleft()
            
            if x == 0 or x == N-1 or y == 0 or y == M-1:
                return depth + 1
                    
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if valid(nx, ny) and grid[nx][ny] == "." and not visited[nx][ny]:
                    q.append((nx, ny, depth + 1))
                    visited[nx][ny] = True
    return "IMPOSSIBLE"


T = int(input())
for i in range(T):
    M, N = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]
    
    now = deque()
    fire = deque()
    # 불꽃 위치 및 출발 위치 확인
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "@":
                now.append((i, j, 0))
            if grid[i][j] == "*":
                fire.append((i, j))
    print(bfs(now, fire))