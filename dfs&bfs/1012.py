import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
ans = []

def bfs(graph, x, y, M, N):
    que = deque()
    que.append((x, y))
    graph[x][y] = 0
    cnt = 0
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                que.append((nx, ny))
                cnt += 1
    return cnt

for i in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    for i in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1
    
    t = 0
    for i in range(N):
        for j in range(M):
            if bfs(graph, i, j, M, N) > 0:
                t += 1

    ans.append(t)

print(ans)
