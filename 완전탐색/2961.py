# combinations 사용에 조금 더 익숙해질 수 있었던 것 경험
# (0,)

from itertools import combinations
import sys
input = sys.stdin.readline
INF = 1e9

N = int(input())
ingredients = [list(map(int, input().split())) for _ in range(N)]

rst = INF
for i in range(1, N + 1):
    idx = list(combinations(list(range(N)), i))
    for food in idx:
        a = 1 # 신맛 
        b = 0 # 쓴맛
        for k in range(i):
            a *= ingredients[food[k]][0]
            b += ingredients[food[k]][1]
        if abs(a-b) < rst:
            rst = abs(a-b)
print(rst)