'''
시도 횟수 : 2
참고 여부 : O
DP 하...
'''
import sys
input = sys.stdin.readline

n = int(input())
wine = [0]
for _ in range(n):
    wine.append(int(input()))

dp = [0] * (n+1)
dp[1] = wine[1]
if n > 1:
    dp[2] = wine[1] + wine[2]

for i in range(3, n+1):
    # 현재 와인을 마시지 않는 경우
    # 이전까지의 최댓값을 그대로 가져옴
    case1 = dp[i-1]
    
    # 현재 와인을 마시고 이전 와인을 마시지 않는 경우
    case2 = dp[i-2] + wine[i]
    
    # 현재 와인과 이전 와인을 마시고 그 이전 와인은 마시지 않는 경우
    case3 = dp[i-3] + wine[i-1] + wine[i]
    
    dp[i] = max(case1, case2, case3)

print(dp[n])


'''import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))

combs = []
for i in range(1, N+1):
    combs.extend(combinations(range(1, N+1), i))
    
max_val = 0
for comb in combs:
    # 만약 3개의 연속적으로 존재하는 수가 없다면
    cnt = 1
    for i in range(1, len(comb)):
        if comb[i] - comb[i-1] == 1:
            cnt += 1
            if cnt == 3:
                break
        else:
            cnt = 1
            
    if cnt < 3:
        temp_sum = 0 
        for i in comb:
            temp_sum += arr[i-1]
        max_val = max(max_val, temp_sum)

print(max_val)'''