# dfs가 크로스로 인접한 노드들에 대한 방문을 진행하지 못함
# dfs로 백트랙킹하는거 (특정 조건에 해당하는 노드들만!)
# 완전 탐색 문제 중 dfs, bfs, dijkstra로 풀어야하는 거 정리해놓기


from itertools import combinations
import sys
from collections import deque
input = sys.stdin.readline

graph = [input().strip() for _ in range(5)]

combs = list(combinations(range(25), 7))

# 1. S가 4개 이상인 조합 찾기
# 0 1 2 3 4 
# 5 6 7 8 9
# x: num//5, y: num%5
path = []
for comb in combs:
    som = 0
    for c in comb:
        if graph[c//5][c%5] == "S":
            som += 1
        if som == 4:
            break
    if som >= 4:
        path.append(comb)

# 2. 조합이 bfs로 연결되어 있는건지 확인하기기
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, comb):
    visited = [[False]*5 for _ in range(5)]
    toVisit= [ (c//5, c%5) for c in comb]
    q = deque([(x, y)])
    visited[x][y] = True
    
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and (nx, ny) in toVisit:
                visited[nx][ny] = True
                q.append((nx, ny))
    
    return cnt == 7


ans = 0
for comb in path:
    if bfs(comb[0]//5, comb[0]%5, comb):
        ans += 1
        
print(ans)

''' 첫번째 시도
import sys
from collections import deque
input = sys.stdin.readline

graph = [input().strip() for _ in range(5)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    stack = deque([(x, y, [(x, y)], 1)])  
    cnt = 0  

    while stack:
        x, y, path, depth = stack.pop()

        if depth == 7:
            som = sum(1 for a, b in path if graph[a][b] == "S")
            if som >= 4:  
                cnt += 1
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in path:
                stack.append((nx, ny, path + [(nx, ny)], depth + 1))

    return cnt

ans = 0
for i in range(5):
    for j in range(5):
        ans += dfs(i, j)

print(ans)
'''