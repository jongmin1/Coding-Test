'''
시도 횟수 : 1
참고 여부 : O
백트랙킹 익숙해지자! 고려해야할 경우부터 생각해보면 그래도 감 잡는데 도움될듯
1. 계란 깨기 끝난 경우
2. 계란 깨려는데 손에 든 계란 깨져있는 경우
3. 안 깨져있어 다른 계란 깰 수 있는 경우
4. 다 깨져서 깰 계란 없는 경우우
'''

import sys
input = sys.stdin.readline

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]

def backtrack(idx, eggs):
    global max_broken
    if idx == N:
        cnt = sum(1 for durability, _ in eggs if durability <= 0)
        max_broken = max(max_broken, cnt)
        return
    
    if eggs[idx][0] <= 0:
        backtrack(idx + 1, eggs)
        return
    
    all_broken = True
    for i in range(N):
        if idx == i or eggs[i][0] <= 0:
            continue
        
        all_broken = False
        
        eggs[i][0] -= eggs[idx][1]
        eggs[idx][0] -= eggs[i][1]    

        backtrack(idx + 1, eggs)
        
        
        eggs[i][0] += eggs[idx][1]
        eggs[idx][0] += eggs[i][1]
        
    if all_broken: # 모든 계란이 깨진 경우우
        backtrack(idx + 1, eggs)
    
max_broken = 0
backtrack(0, eggs)

print(max_broken)