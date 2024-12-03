from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    stack = deque([(x, y)])
    grid[x][y] = 0
    
    while stack:
        x, y = stack.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
                
            if grid[nx][ny] == 1:
                grid[nx][ny] = 0
                stack.append((nx, ny))
    
    
T = int(input())
for i in range(T):
    M, N, K = map(int, input().strip().split())
    grid = [[0]*M for _ in range(N)]

    for i in range(K):
        b, a = map(int, input().strip().split())
        grid[a][b] = 1

    cnt = 0
    for j in range(N):
        for k in range(M):
            if grid[j][k] == 1:
                dfs(j, k)
                
                cnt += 1
    
    print(cnt)


'''
from collections import deque
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    grid[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1:
            dfs(nx, ny)
    
    
T = int(input())
for i in range(T):
    M, N, K = map(int, input().strip().split())
    grid = [[0]*M for _ in range(N)]

    for i in range(K):
        b, a = map(int, input().strip().split())
        grid[a][b] = 1

    cnt = 0
    for j in range(N):
        for k in range(M):
            if grid[j][k] == 1:
                dfs(j, k)
                
                cnt += 1
    
    print(cnt)

'''