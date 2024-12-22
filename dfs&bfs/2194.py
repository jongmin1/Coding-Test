# 장애물 확인하는 부분에 따라 시간초과 뜸
# 아래는 부분합으로 장애물 위치 파악하는 방법...

from collections import deque
import sys
input = sys.stdin.readline

N, M, A, B, K = map(int, input().split())

# 1) 장애물 정보를 2차원 배열 board에 표시
board = [[0]*M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

# 시작점, 끝점 입력
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
sx, sy, ex, ey = sx-1, sy-1, ex-1, ey-1

# 2) prefix sum(누적합) 배열 만들기
prefix_sum = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        prefix_sum[i][j] = (prefix_sum[i-1][j] 
                            + prefix_sum[i][j-1] 
                            - prefix_sum[i-1][j-1] 
                            + board[i-1][j-1])

def obstacle_in_area(x1, y1, x2, y2):
    """(x1,y1) ~ (x2,y2) 범위 내 장애물 개수 반환"""
    return (prefix_sum[x2][y2]
            - prefix_sum[x1-1][y2]
            - prefix_sum[x2][y1-1]
            + prefix_sum[x1-1][y1-1])

# 3) BFS 설정
visited = [[-1]*M for _ in range(N)]
visited[sx][sy] = 0
q = deque([(sx, sy)])

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

while q:
    x, y = q.popleft()
    # 도착점 체크
    if x == ex and y == ey:
        print(visited[x][y])
        break
    
    # 4) 인접 칸 확인
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 범위 확인 (A x B 영역이 모두 격자 내부인지)
        if 0 <= nx and nx + A - 1 < N and 0 <= ny and ny + B - 1 < M:
            if visited[nx][ny] == -1:
                # prefix_sum으로 장애물 확인
                if obstacle_in_area(nx+1, ny+1, nx+A, ny+B) == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
else:
    # while문이 break로 종료되지 않으면 -1 출력
    print(-1)



'''from collections import deque
import sys
input = sys.stdin.readline

# 행, 열, 유닛행, 유닛열, 장애물 설치 위치
N, M, A, B, K = map(int, input().split())

obstacle = []
for i in range(K):
    obstacle.append(list(map(int, input().split())))


start = list(map(int, input().split()))
end = list(map(int, input().split()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False] * M for _ in range(N)]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 0

    while q:
        x, y = q.popleft()

        if x == end[0]-1 and y == end[1]-1:
            print(visited[end[0]-1][end[1]-1])
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 유닛이 grid 안에 있고
            if 0 <= nx and nx + A - 1 < N and 0 <= ny and ny + B - 1 < M and not visited[nx][ny]:
                # 장애물 안 겹치면
                if checkObstacle(nx, ny):
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    print(-1)
    return

def checkObstacle(nx, ny):
    for o in obstacle:
        if nx <= o[0]-1 <= nx + A - 1 and ny <= o[1]-1 <= ny + B - 1:
            return False
    return True

bfs(start[0]-1, start[1]-1)


'''