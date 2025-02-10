import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    # 범위를 벗어나거나 구멍('H')을 만나면 0 반환
    if x < 0 or x >= N or y < 0 or y >= M or board[x][y] == 'H':
        return 0
    
    # 이미 방문한 곳을 다시 방문하면 사이클이 존재하므로 무한 반복
    if visited[x][y]:
        print(-1)
        sys.exit()
    
    # 이미 계산된 값이 있다면 그 값을 반환
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    
    # 현재 칸의 숫자
    num = int(board[x][y])
    
    # 4방향으로 이동
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx = x + dx * num
        ny = y + dy * num
        
        dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    
    visited[x][y] = False
    return dp[x][y]

# 입력 받기
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# DP 테이블과 방문 체크 배열 초기화
dp = [[-1] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# (0, 0)에서 시작
print(dfs(0, 0))
