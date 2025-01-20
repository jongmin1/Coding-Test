'''
시도 횟수 : 1
참고 여부 : X
'''
import sys
import heapq as hq
input = sys.stdin.readline

T = int(input())
q = []
for _ in range(T):
    a = int(input())
    if a == 0:
        if q:
            print(abs(hq.heappop(q)))
        else:
            print(0)
    else:
        hq.heappush(q, -a)