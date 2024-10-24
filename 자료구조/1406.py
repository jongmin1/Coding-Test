# 느낀점: stack을 이렇게도 사용할 수 있구나에 대한 관점을 키울 수 있었음
# 명령어를 처리할 때 stack을 많이 이용하는거 같음.
from collections import deque
import sys
input = sys.stdin.readline

string = list(input().strip())
N = int(input())

command = []
forw = deque(string)
backw = deque()

for i in range(N):
    command.append(list(map(str, input().split())))
    if command[i][0] == 'L' and forw:
        backw.appendleft(forw.pop())
    if command[i][0] == 'D' and backw:
        forw.append(backw.popleft())
    if command[i][0] == 'B' and forw:
        forw.pop()
    if command[i][0] == 'P':
        forw.append(command[i][1])

'''시간초과
cur = len(string)
for i in range(N):
    command.append(list(map(str, input().split())))
    if command[i][0] == 'L' and cur > 0:
        cur -= 1
    if command[i][0] == 'D' and cur < len(string):
        cur += 1
    if command[i][0] == 'B' and cur > 0:
        del string[cur-1]
        cur -= 1
    if command[i][0] == 'P':
        string.insert(cur, command[i][1])
        cur += 1
'''

for i in string:
    print(i, end="")