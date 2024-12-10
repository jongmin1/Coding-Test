# myDict = {'A':1, 'C':2, 'B':0}

# print(myDict.get('A'))

# print(myDict.get('A'))
# print(myDict.get('C'))
# print(myDict.get('C', 0))

# print(myDict.items())
# print(myDict.keys())
# print(myDict.values())

# print(sorted(myDict.items(), key=lambda x:x[1]))


# my_set.discard(value)
# my_dict.pop(key_to_remove, None) 

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input())
grid = [list(map(int, input().strip().split())) for _ in range(N)]
pos = [list(map(int, input().strip().split())) for _ in range(M)]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 3초 동안(3번 움직일 수 있는 거)
def dfs():
    visited = [[0]*N for _ in range(N)]
    path = []
    total = 0
    
    while stack:
        x, y = stack.pop()
        visited[x][y] = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and (nx, ny) not in path:
                visited[nx][ny] = 1
                total += grid[nx][ny]
                path.append()
                stack.append((nx, ny))
    return 

# dfs를 누구 먼저 돌릴거냐   
total = 0
stack = deque()
for i in pos:
    stack.append(i)
ans = dfs()

stack = deque()
pos.reverse()
for i in pos:
    stack.append(i)
ans = max(ans, dfs())

print(ans)