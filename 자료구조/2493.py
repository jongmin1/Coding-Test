from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
towers =list(map(int, input().split()))

r = [0]*N

'''
시간 초과 뜰 코드
for i in range(N-1, -1, -1):
    for j in range(i-1, -1, -1):
        if towers[i] <= towers[j]:
            r[i] = j+1
            break
'''

stack = []
for i in range(N-1, -1, -1):
    while stack and towers[stack[-1]] < towers[i]:
        r[stack.pop()] = i + 1
    stack.append(i)

for i in r:
    print(i, end=" ")