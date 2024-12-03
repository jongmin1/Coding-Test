from itertools import combinations
from bisect import bisect_left
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

arr.sort()

for i in range(M):
    a = int(input().strip())
    if a in arr:
        num = bisect_left(arr, a)
        ans = len(list(combinations(range(num), 1))) * len(list(combinations(range(N-num-1), 1)))
        print(ans)
    else:
        print(0)