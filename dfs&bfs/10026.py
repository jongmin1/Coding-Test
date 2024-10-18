import copy
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

normal = []

for i in range(N):
    normal.append(list(input().strip()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

lenRow = len(normal)
lenCol = len(normal[0])

odd = copy.deepcopy(normal)

for i in range(lenRow):
    for j in range(lenCol):
        if odd[i][j] == "R":
            odd[i][j] = 'G'
            
def bfs(graph, x, y):
    print(graph)
    que = deque()
    c = graph[x][y]
    que.append((x, y))
    graph[x][y] = 0
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= lenCol or ny >= lenRow:
                continue
            
            if graph[nx][ny] == c:
                graph[nx][ny] = 0
                que.append((nx,ny))

cntNormal = 0
for i in range(lenRow):
    for j in range(lenCol):
        if normal[i][j] != 0:
            bfs(normal, i, j)
            cntNormal += 1
          
cntOdd = 0
for i in range(lenRow):
    for j in range(lenCol):
        if odd[i][j] != 0:
            bfs(odd, i, j)
            cntOdd += 1

print(cntNormal, cntOdd)
