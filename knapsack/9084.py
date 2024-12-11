# dp 쉽지 않네... 다음에 모아서 싹 한 번에 복습해야지..

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())
    
    dp = [0]*(M+1)
    dp[0] = 1
    for coin in arr:
        for j in range(1, M+1):
            if j >= coin:
                dp[j] += dp[j-coin]
    print(dp[M])    
    