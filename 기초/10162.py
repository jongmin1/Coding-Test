import sys
input = sys.stdin.readline

N = int(input())
A, B, C = 0, 0, 0

while N >= 300:
    N = N - 300
    A += 1

while N >= 60:
    N = N - 60
    B += 1

while N >= 10:
    N = N - 10
    C += 1

if N == 0:
    print(A, B, C)
else:
    print(-1)