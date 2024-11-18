# 처음 풀어본 냅색 문제, dp를 이렇게 활용하는구나 알 수 있었던 문제

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bag = [[0]*(M+1) for _ in range(N+1)]
things = []

for i in range(N+1):
    things.append(list(map(int, input().split())))

for i in range(1, N+1):
    w = things[i-1][0]
    v = things[i-1][1]
    for j in range(1, M+1):
        if j >= w: # 빈 공간 >= 현재 물건 무게
            # 위에 있는 값 vs 현재 물건 가치+여유무게에서의 최대 가치
            bag[i][j] = max(bag[i-1][j], v + bag[i-1][j-w])
        else:
            bag[i][j] = bag[i-1][j]

print(bag[N][M])


'''
다른 사람 풀이 -> 1차원으로 잘 푼듯..

n,k = map(int,input().split())
dp = [0] *(k+1)
li = []
for i in range(n):
  w,v = map(int,input().split())
  li.append((w,v))

for i in range(n):
  w,v = li[i]
  for j in range(k,w-1,-1):
    dp[j] = max(dp[j],dp[j-w] + v)
print(dp[k])
'''