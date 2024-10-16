t = int(input())
n = list(map(int, input().split()))

dp = [1] * t
for i in range(t):
    for j in range(i):
        if n[i] < n[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))