# 재귀 쉽지 않네... 익수하지 않아서 그런듯
# 수도 코드 짜듯이 짜는게 도움이 되는듯 하다...

import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)] 

rst = [0, 0]
def sol(x, y, n):
    color = grid[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != grid[i][j]:
                m = n//2
                sol(x, y, m) 
                sol(x, y+m, m) 
                sol(x+m, y, m) 
                sol(x+m, y+m, m) 
                return 
                
    if color == 0:
        rst[0] += 1
    else:
        rst[1] += 1 
        
sol(0, 0, N)
print(rst[0])
print(rst[1])