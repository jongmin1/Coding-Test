# num(int로 바꿔서하면) 되고 command[1] 이 자체로 하면 안 되는 이유 아직 모르겠음
# 그냥 숫자로 주어졌으면 숫자로 바꿔서 하는게 마음 편할듯

import sys
input = sys.stdin.readline

N = int(input().strip())
S = set()

for _ in range(N):
    commands = input().strip().split()

    if len(commands) == 1:
        if commands[0] == "all":
            S = set(list(range(1, 21)))
        else:
            S = set()
    
    else:
        command, num = commands[0], commands[1]
        num = int(num)
        
        if command == "add":
            S.add(num)
        elif command == "remove":
            S.discard(num)
        elif command == "check":
            print(1 if num in S else 0)
        elif command == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)