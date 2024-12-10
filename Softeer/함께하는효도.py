from collections import deque
from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(N)]
posofFriends = [list(map(int, input().strip().split())) for _ in range(M)]
visited = [[False]*N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, time):
    global score
    visited[x][y] = 1
    score += grid[x][y]
    
    if time == 3:
        return 
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
                
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:               
            dfs(nx, ny, time+1)
            
       

perms = list(permutations(posofFriends, M))  # [([1, 2], [2, 3]), ([2, 3], [1, 2])]
ans = 0
for perm in perms:  # ([1, 2], [2, 3]) & ([2, 3], [1, 2])
    totalScore = 0
    visited = [[0]*N for _ in range(N)]
    for i, j in perm: # grid[0][1] 에서 2번 이동, grid[1][2]에서 2번 이동
        score = 0
        dfs(i-1, j-1, 0)
        totalScore += score
    ans = max(ans, totalScore)
print(ans)


import sys
from itertools import permutations

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
pos = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(m)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# DFS를 통한 최대 점수 계산
def dfs(x, y, depth, score, visited):
    if depth == 4:  # 깊이가 4일 때 종료 (자기 포함 4칸 탐색)
        return score
    
    max_score = score
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[nx][ny]:
            visited[nx][ny] = True
            max_score = max(max_score, dfs(nx, ny, depth + 1, score + grid[nx][ny], visited))
            visited[nx][ny] = False
    return max_score

# 최적 경로 및 점수 계산
def get_max_score(perm):
    visited = [[False] * n for _ in range(n)]
    total_score = 0

    for x, y in perm:
        visited[x][y] = True
        total_score += dfs(x, y, 1, grid[x][y], visited)  # 자기 자신 포함 시작
        visited[x][y] = False  # 다른 경로에서도 사용 가능하도록 초기화
    
    return total_score

# 모든 순열에 대해 점수 계산
result = 0
for perm in permutations(pos, m):
    result = max(result, get_max_score(perm))

print(result)
