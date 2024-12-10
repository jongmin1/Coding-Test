import sys
input = sys.stdin.readline

N = int(input().strip())
grid = [list(map(int, input().strip().split())) for _ in range(N)]
ans = 0
numFruit = 0
# 오른쪽 N만큼
# 아래로 N만큼
# 경로 값들 다 list에 저장하고
# max 해서 그 값 더해주기
route = [[], []]
for i in range(N):
    route[0].append(grid[0][i])
for i in range(1, N):
    route[0].append(grid[i][N-1])
# 아래
# 오른쪽
for i in range(N):
    route[1].append(grid[i][0])
for i in range(1, N):
    route[1].append(grid[N-1][i])

a = sum(route[0])+max(route[0])
b = sum(route[1])+max(route[1])
print(max(a, b))
