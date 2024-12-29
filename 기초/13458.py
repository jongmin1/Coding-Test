# 계산하는 경우 음수가 되는 경우 생각하기! 

import sys
input = sys.stdin.readline

T = int(input())
A = list(map(int, input().split()))
mainAdmin, subAdmin = map(int, input().split())

ans = 0

for i in range(len(A)):
    A[i] -= mainAdmin
    ans += 1

    if A[i] > 0:
        ans += (A[i] + subAdmin - 1) // subAdmin

print(ans)
