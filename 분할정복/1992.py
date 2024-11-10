# 쿼드 트리의 일방적인 풀이법을 설명한 문제라고 이해함

import sys
input = sys.stdin.readline

N = int(input())
video = [list(map(int, input().strip())) for _ in range(N)]

color = -1
def sol(x, y, n):
    color = video[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != video[i][j]:
                print("(", end="")
                m = n//2
                sol(x, y, m)
                sol(x, y+m, m)
                sol(x+m, y, m)
                sol(x+m, y+m, m)
                print(")", end="")
                return
    print(color, end="")

sol(0, 0, N)