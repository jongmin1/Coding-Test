# 두고보자..

import sys
input = sys.stdin.readline
INF = 1e9

N = int(input())
liquid = list(map(int, input().strip().split()))
liquid.sort()

start, a, b = 0, 0, 0
end = N - 1
closest_sum = INF

while start < end:
    t = liquid[start] + liquid[end]
    
    if abs(t) < closest_sum:
        closest_sum = abs(t)
        a, b = liquid[start], liquid[end]
        if t == 0:
            break
    
    if t < 0:
        start += 1
    else:
        end -= 1
    
print(a, b)