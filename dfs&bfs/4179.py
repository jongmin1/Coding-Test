import sys
from collections import deque
input = sys.stdin.readline

R, C =map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start, fire):
    fire_queue = deque(fire)  # 불의 위치로 초기화
    visited = [[False] * C for _ in range(R)]
    
    # 불의 전파
    while fire_queue:
        x, y = fire_queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == ".":
                grid[nx][ny] = "F"  # 불이 전파된 곳
                fire_queue.append((nx, ny))

    # 주인공의 BFS
    player_queue = deque([start])
    visited[start[0]][start[1]] = True
    depth = 0
    
    while player_queue:
        depth += 1
        for _ in range(len(player_queue)):  # 현재 깊이의 모든 노드 처리
            x, y = player_queue.popleft()
            
            if x == 0 or x == R-1 or y == 0 or y == C-1:
                print(depth)
                return
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                    if grid[nx][ny] == ".":
                        visited[nx][ny] = True
                        player_queue.append((nx, ny))
    
    print("IMPOSSIBLE")

now = []
fire = []    
for i in range(R):
    for j in range(C):
        if grid[i][j] == "J":
            now = (i, j)
        if grid[i][j] == "F":
            fire.append((i, j))

bfs(now, fire)