import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

grid = [sum(list(map(int, input().split()))) for _ in range(N)]

attackLine = []
for i in range(2):
    a, b = map(int, input().split())
    for j in range(a-1, b):
        if grid[j] > 0:
            grid[j] -= 1

print(sum(grid))
