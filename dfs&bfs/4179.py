from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
maze = [list(input().strip()) for _ in range(R)]


fire = deque()
jihoon = deque()
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            jihoon.append((i, j, 0)) 
            maze[i][j] = '.' 
        elif maze[i][j] == 'F':
            fire.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while jihoon:
        fire_size = len(fire)
        for _ in range(fire_size):
            x, y = fire.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if maze[nx][ny] == '.':  
                        maze[nx][ny] = 'F'
                        fire.append((nx, ny))
        
        jihoon_size = len(jihoon)
        for _ in range(jihoon_size):
            x, y, time = jihoon.popleft()
            
            if x == 0 or x == R-1 or y == 0 or y == C-1:
                return time + 1
                
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if maze[nx][ny] == '.':  
                        maze[nx][ny] = 'J'  
                        jihoon.append((nx, ny, time + 1))
    
    return "IMPOSSIBLE"

print(bfs())