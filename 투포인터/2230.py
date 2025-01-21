'''
시도 횟수 : 3
참고 여부 : X
앞으로 inf는 float('inf')로 처리하자.
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()

left = 0
right = 1
ans = float('inf')
while right < N:
    diff = arr[right] - arr[left]
    if diff == M:
        ans = diff
        break
    elif diff > M: 
        ans = min(ans, diff)
        left += 1
    else:
        right += 1
  
print(ans)      