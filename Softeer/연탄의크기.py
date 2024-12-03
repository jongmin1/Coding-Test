# 문제 이해를 잘못해서 틀린 문제.. 문제 이해 좀 더 꼼꼼히 하기

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().strip().split()))

ans = 0
for i in range(2, 101):
    cnt = 0
    for j in range(N):
        if arr[j] % i == 0:
            cnt += 1
    ans = max(ans, cnt)
print(ans)