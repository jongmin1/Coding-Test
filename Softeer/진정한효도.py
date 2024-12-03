import sys
input = sys.stdin.readline

grid = []

for i in range(3):
    grid.append(list(map(int, input().strip().split())))

ans = 0
# 가로
for i in range(3):
    temp = []
    for j in range(3):
        temp.append(grid[i][j])
    ans = min(ans, max(temp)-min(temp))
    
# 세로
for i in range(3):
    temp = []
    for j in range(3):
        temp.append(grid[j][i])
    ans = min(ans, max(temp)-min(temp))
    
print(ans)