from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = []

for i in range(len(arr)-1, -1, -1):
    k = bisect_left(dp, arr[i])
    if k == len(dp):
        dp.append(arr[i])
    else:
        dp[k] = arr[i]
        
print(N-len(dp))
