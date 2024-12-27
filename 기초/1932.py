import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(1, N):
    length = len(arr[i])
    for j in range(length):
        if j == 0:
            arr[i][j] += arr[i-1][j]
        elif j == length-1:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

print(max(arr[-1]))