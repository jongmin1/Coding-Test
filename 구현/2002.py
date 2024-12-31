'''
시도 횟수 : 3
참고 여부 : O
비슷한 유형 나오면 이렇게 풀자! 맞겠지~ 풀지 말고 계속 반례 생각하면서 하기
'''

import sys
input = sys.stdin.readline

N = int(input())
before = [input().strip() for _ in range(N)]
after = [input().strip() for _ in range(N)]

entryOrder = dict()
for i in range(N):
    entryOrder[before[i]] = set(before[:i])
exitOrder = dict()
for i in range(N):
    exitOrder[after[i]] = set(after[:i])
    
ilegal = set()
for car in after:
    check = exitOrder[car] - entryOrder[car]
    if check:
        ilegal.update(check)
        
print(len(ilegal))