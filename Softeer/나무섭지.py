import sys
from collections import deque


def print_arr(arrs):
    for i in range(len(arrs)):
        for j in range(len(arrs[0])):
            print(arrs[i][j], end=" ")
        print()


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    global n, m, q, ans, nv, gv

    while len(q) != 0:
        px, py, pc = q.popleft()

        for d in range(4):
            nx = dx[d] + px
            ny = dy[d] + py

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 남우일 때
            if pc == 'N':
                if nv[nx][ny] == True or gv[nx][ny] == True or arr[nx][ny] == '#':
                    continue

                # 탈출구를 만나면
                if arr[nx][ny] == 'D':
                    ans = 'Yes'
                    return
                
                nv[nx][ny] = True
                q.append([nx, ny, pc])

            # 유령일 때
            elif pc == 'G':
                if gv[nx][ny] == True:
                    continue
                gv[nx][ny] = True
                q.append([nx, ny, pc])

n, m = list(map(int, input().split()))

arr = []

for _ in range(n):
    arr.append(list(map(str, input().strip())))

other = []

q = deque()
nv = [[False] * m for _ in range(n)]
gv = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'N':
            q.append([i, j, 'N'])
            nv[i][j] = True
        elif arr[i][j] == 'G':
            other.append([i, j, 'G'])
            gv[i][j] = True

q.extend(other)

ans = 'No'
bfs()

print(ans)