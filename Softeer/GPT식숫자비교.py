import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    t = str(input().strip())
    if '.' in t:
        a, b = map(int, t.split('.'))
        arr.append([a, b])
    else:
        arr.append([int(t), -1])

arr.sort(key=lambda x:[x[0], x[1]])

for i in arr:
    if i[1] == -1:
        print(i[0])
    else:
        print(f'{i[0]}.{i[1]}')