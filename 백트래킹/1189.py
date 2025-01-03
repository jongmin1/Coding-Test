import sys
input=sys.stdin.readline

R, C, K=map(int,input().split())
graph=[ list(input().rstrip()) for _ in range(R) ] 

answer=0

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
def DFS(x, y, count):
    global answer

    if count == K and x == 0 and y == C - 1:
        answer+=1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < R and 0<= ny < C and graph[nx][ny]=='.':
                graph[nx][ny]='T'
                DFS(nx, ny, count + 1) 
                graph[nx][ny]='.'

graph[R-1][0] = 'T'
DFS(R-1, 0, 1)
print(answer)

'''import sys
from collections import deque
input = sys.stdin.readline

R, C, K = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    global path_length
    stack = deque([(x, y, 1)])
    visited = [[False]*C for _ in range(R)]
    visited[x][y] = True
    
    while stack:
        x, y, dist = stack.pop()
        if dist == K:
            if x == 0 and y == C - 1:
                path_length += 1    
                continue 
        
        for i in range(4):
            nx = x + dx[i]
            ny = x + dy[i]
            
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != "T" and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny, dist + 1))
                visited[nx][ny] = False    
    

path_length = 0
dfs(R - 1, 0)
print(path_length)
'''