
import sys
input = sys.stdin.readline

def is_valid(x, y, num):
    # 가로줄 체크
    for i in range(9):
        if grid[x][i] == num:
            return False
    
    # 세로줄 체크
    for i in range(9):
        if grid[i][y] == num:
            return False
    
    # 3x3 박스 체크
    start_x = (x // 3) * 3
    start_y = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_x + i][start_y + j] == num:
                return False
    return True

def solve(depth):
    if depth == len(zeros):
        return True
    
    x, y = zeros[depth]
    for num in range(1, 10):
        if is_valid(x, y, num):
            grid[x][y] = num
            solve(depth + 1) 
            grid[x][y] = 0
    return False

grid = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if grid[i][j] == 0]

solve(0)

for row in grid:
    print(*row)

'''import sys
input = sys.stdin.readline

grid = [list(map(int, input().split())) for _ in range(9)]

arr = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6),  (6, 0), (6, 3), (6, 6)]
all_zero_pos = []
for x, y in arr:
    nums = set()
    zero_pos = []
    for i in range(3):
        for j in range(3):
            nums.add(grid[x+i][y+j])
            if grid[x+i][y+j] == 0:
                zero_pos.append((x+i, y+j))
                all_zero_pos.append((x+i, y+j))
    non = [i for i in range(1, 10) if not i in nums]
    
    if len(non):
        grid[zero_pos[0][0]][zero_pos[0][1]] = non[0]
        all_zero_pos.remove(zero_pos[0])

for x, y in all_zero_pos:
    row = []
    col = []
    for i in range(9):
        row.append(grid[x][i])
        col.append(grid[i][y])
    for i in range(1, 10):
        if not i in row and not i in col:
            grid[x][y] = i

for i in grid:
    print(*i) '''

            
            