'''
시도 횟수 : 3
참고 여부 : O
두 수의 합 -> 투포인터 (처음에 combinations, 두번째는 dfs)
'''
from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
X = int(input())

arr.sort()
cnt = 0
left = 0
right = N-1
while left < right:
    temp = arr[left] + arr[right]
    if temp == X:
        cnt += 1
        left += 1
        right -= 1
    elif temp < X:
        left += 1
    else:
        right -= 1

print(cnt)