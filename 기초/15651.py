from itertools import product
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]
ans = product(arr, repeat=M)

for i in ans:
    print(" ".join(list(map(str, i))))