# 처음 푼 2차원 배열에서의 dp

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
grid = []
for i in range(N):
    grid.append(list(map(int, input().strip().split())))

dp = list([0]*(N+1) for _ in range(N+1))
for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + grid[i-1][j-1]
      

for i in range(M):
    x1, y1, x2, y2 = map(int, input().strip().split())
    ans = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(ans)