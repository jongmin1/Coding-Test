# write 함수 사용하면1580ms -> 576ms로 단축됨

from collections import deque
import sys
input = sys.stdin.readline
write = sys.stdout.write  

N = int(input())
que = deque()
order = []  # 0: append, 1: appendleft

# Collect input efficiently
for _ in range(N):
    command = input().split()
    t = int(command[0])

    if t == 1:
        que.append(command[1])
        order.append(0)
    elif t == 2:
        que.appendleft(command[1])
        order.append(1)
    elif t == 3 and que:
        if order.pop() == 0:
            que.pop()
        else:
            que.popleft()

# Print output efficiently
if que:
    write(''.join(que) + '\n')
else:
    write('0\n')