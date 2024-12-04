import sys
input = sys.stdin.readline

N = int(input())
arr = []
ans = []
for i in range(N):
    arr.append(list(map(int, input().strip().split())))

arr.sort(key=lambda x: [x[1], x[0]])
ans.append(arr[0])

for i in range(1, N):
    if arr[i][0] >= ans[-1][1]:
        ans.append(arr[i])
print(len(ans))
