# LIS 어떻게 푸는지 알아버렸달까~

from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().strip().split()))
dp = []

for n in arr:
    k = bisect_left(dp, n)
    if len(dp) == k:
        dp.append(n)
    else: # 앞의 요소보다는 크나, dp[-1]보다는 작을 경우, dp[-1]에 더 작은 값으로 대체
        dp[k] = n

print(len(dp))

