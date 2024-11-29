from collections import deque
import sys
input = sys.stdin.readline

arr = list(input().strip())
que = deque()

for i in range(len(arr)):
    que.append(arr[i])
    if i == len(arr)-1:
        break
    if arr[i] == '(':
        if arr[i+1] == '(':
            que.append('1+')
        else:
            que.append('1+1')
    else:
        if arr[i+1] == '(':
            que.append('+')
        else:
            que.append('+1')

for i in que:
    print(i, end="") 