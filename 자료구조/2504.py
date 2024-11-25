# 유효한 입력인지 확인하는 것을 아래에서 한꺼번에 했으면 코드 길이 확실히 줄일 수 있었을텐데
# 런타임에러 -> 처리할 때 생각하지 못한 케이스로 입력? 처리? 문제가 발생했을 때 발생할 수 있음

from collections import deque
import sys
input = sys.stdin.readline

arr = list(input().strip())
stack = deque()

lenArr = len(arr)
ans = 0

valid = True
# 유효한 입력인지 확인
for i in arr:
    if i == ')':
        if not stack: 
            valid = False
            break
        t = stack.pop()
        if t == '[' or t == ']':
            valid = False
            break
    elif i == ']':
        if not stack: 
            valid = False
            break
        t = stack.pop()
        if t == '(' or t == ')':
            valid = False
            break
    else:
        stack.append(i)          
if len(stack) > 0: valid = False 

if valid:
    for i in range(lenArr):
        if arr[i] == ')':
            t = stack.pop()
            tempSum = 0
            while t != '(':
                tempSum += t
                t = stack.pop()
            stack.append(2 * (1 if tempSum==0 else tempSum))

        elif arr[i] == ']':
            t = stack.pop()
            tempSum = 0
            while t != '[':
                tempSum += t
                t = stack.pop()
            stack.append(3 * (1 if tempSum==0 else tempSum))
        else: # 닫는 거 제외 다 집어넣기
            stack.append(arr[i])
        
        if i == lenArr-1:
            for j in stack:
                ans += j
else:
    ans = 0
print(ans)