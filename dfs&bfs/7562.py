'''
시도 횟수 : 2
참고 여부 : O
이번에도 move 값 잘못 선언함... 이런 실수하지 않게 항상 더블 체크할 것!
'''
import sys
from collections import deque
input = sys.stdin.readline

move = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

def bfs(x, y, x_dest, y_dest, n):
    q = deque([(x, y, 0)])
    visited[x][y] = True
    
    while q:
        x, y, depth = q.popleft()
        
        if (x, y) == (x_dest, y_dest):
            return depth
        
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                q.append((nx, ny, depth+1))
                visited[nx][ny] = True

T = int(input())
for _ in range(T):
    l = int(input())
    now = list(map(int, input().split()))
    dest = list(map(int, input().split()))
    visited = [[False]*l for _ in range(l)]
    
    print(bfs(now[0],now[1], dest[0], dest[1], l))

