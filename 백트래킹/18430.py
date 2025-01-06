'''
시도 횟수 : 1
참고 여부 : O
이런 유형 처음 풀어봄... dfs 응용 아직 잘 못하는듯
'''

import sys
input = sys.stdin.readline

def solve(x, y, total):
    global ans
    
    if y == M: 
        x += 1
        y = 0
    
    if x == N:  
        ans = max(ans, total)  
        return
    
    solve(x, y + 1, total)
    
    # ㄱ 모양
    if x + 1 < N and y + 1 < M:
        if not visited[x][y] and not visited[x+1][y] and not visited[x][y+1]:
            visited[x][y] = visited[x+1][y] = visited[x][y+1] = True
            solve(x, y + 1, total + (wood[x][y] * 2 + wood[x+1][y] + wood[x][y+1]))
            visited[x][y] = visited[x+1][y] = visited[x][y+1] = False
    
    # ㄴ 모양
    if x + 1 < N and y - 1 >= 0:
        if not visited[x][y] and not visited[x+1][y] and not visited[x][y-1]:
            visited[x][y] = visited[x+1][y] = visited[x][y-1] = True
            solve(x, y + 1, total + (wood[x][y] * 2 + wood[x+1][y] + wood[x][y-1]))
            visited[x][y] = visited[x+1][y] = visited[x][y-1] = False
    
    # ㅢ 모양
    if x - 1 >= 0 and y + 1 < M:
        if not visited[x][y] and not visited[x-1][y] and not visited[x][y+1]:
            visited[x][y] = visited[x-1][y] = visited[x][y+1] = True
            solve(x, y + 1, total + (wood[x][y] * 2 + wood[x-1][y] + wood[x][y+1]))
            visited[x][y] = visited[x-1][y] = visited[x][y+1] = False
    
    # ㅣ_ 모양
    if x - 1 >= 0 and y - 1 >= 0:
        if not visited[x][y] and not visited[x-1][y] and not visited[x][y-1]:
            visited[x][y] = visited[x-1][y] = visited[x][y-1] = True
            solve(x, y + 1, total + (wood[x][y] * 2 + wood[x-1][y] + wood[x][y-1]))
            visited[x][y] = visited[x-1][y] = visited[x][y-1] = False


N, M = map(int, input().split())
wood = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
ans = 0

solve(0, 0, 0)

print(ans)