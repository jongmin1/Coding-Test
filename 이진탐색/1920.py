N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()
A = set(A)
for i in B:
    if i in A:
        print(1)
    else:
        print(0)