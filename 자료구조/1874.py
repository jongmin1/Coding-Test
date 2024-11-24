# 구현은 쉬웠으나 문제 이해가 어려웠음... 문해력이 문제인가 흠..

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

rst = []
que = deque([0])
currentMax = 0
for i in  arr:    
    while currentMax < i:
        que.append(currentMax + 1)
        currentMax += 1 
        rst.append('+')
    if que[-1] == i: 
        que.pop()
        rst.append('-')
        
if len(que) > 1:
    print("NO")
else:
    for i in rst:
        print(i)