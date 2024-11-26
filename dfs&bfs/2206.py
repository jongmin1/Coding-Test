# 똑같은 코드인데 왜 pypy3로 하면 더 빠르지...
# 어떤 벽을 부셔야할지 모르는데 이렇게 해도 되나라는 생각이 들었는데
# bfs의 동작에 대한 이해가 부족했던 것 같음. 이번 기회에 그래도 약간은 자신감이 생긴듯..?
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    que = deque()
    visited[0][0][0] = 1
    que.append([0, 0, 0])
    
    while que:
        x, y, w = que.popleft()
        
        # 선착순으로 가장 먼저 들어오는 친구
        if x == N-1 and y == M-1:
            return visited[x][y][w]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:         
                # 방문한 적 없고, 다음 경로에 벽이 없는 경우 
                # 벽 부셨던 경로는 w=1 고정, 부시지 않았던 경로는 0으로
                if visited[nx][ny][w] == 0 and graph[nx][ny] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    que.append([nx, ny, w])
                    
                # 벽을 부신 적 X, 벽을 부셔야 하는 경우 (벽을 처음 마주한 경우)
                if w == 0 and graph[nx][ny] == 1:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    que.append([nx, ny, 1])
            
    return -1
    
print(bfs())