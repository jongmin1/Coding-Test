'''
시도 횟수 : 2
참고 여부 : O
시간초과 -> 여러 명령어 들어있는 문제는 시간초과 안 걸리려면 이렇게 풀어야하는구나!
'''
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cmds = list(input().strip())
    N = int(input())
    arr_input = input().strip()[1:-1]
    if arr_input:
        arr = deque(map(int, arr_input.split(",")))
    else:
        arr = deque()
    
    is_reversed = False
    is_error = False
    
    for cmd in cmds:
        if cmd == "R":
            is_reversed = not is_reversed
        if cmd == "D":
            if len(arr) == 0:
                is_error = True
                break
            if is_reversed:
                arr.pop()
            else:
                arr.popleft()
    
    if is_error:
        print("error")
    else:
        if is_reversed:
            arr.reverse()    
        print("[" + ",".join(map(str,arr)) + "]")
    