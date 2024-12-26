# https://maximum-curry30.tistory.com/371

import sys
input = sys.stdin.readline

def isValid(mid):
    divide = 1
    pmax = arr[0]
    pmin = arr[0]
    
    for i in arr:
        pmax = max(pmax, i)
        pmin = min(pmin, i)
        
        # 조건 깨지면 새로 시작
        if pmax - pmin > mid:
            divide += 1
            pmax = i
            pmin = i
    return M >= divide
    
    
N, M = map(int, input().split())
arr = list(map(int, input().split()))

right = max(arr)
left = 0
ans = right

while left <= right:
    mid = (left + right) // 2
    
    if isValid(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1
 
print(ans)