# 문제에서 주어진 논리 순서대로가 아닌 허점이 무엇인지 생각해보고 
# 다시 한 번 생각하고 코딩하기 

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
recommand = list(map(int, input().split()))

candidate = dict()
for i in range(M):
    # 이미 후보가 등록되어 있다면
    if recommand[i] in candidate:
            candidate[recommand[i]][0] += 1
            
    else:  # 미등록 상태
        # 자리가 있다면
        if len(candidate) < N: # 자리 O
            candidate[recommand[i]] = [1, i]  # [추천수, timestamp]
        else: # 자리가 없다면
            tDict = sorted(candidate.items(), key=lambda x: (x[1][0], x[1][1]))
            tIdx = tDict[0][0]
            del candidate[tIdx]
            candidate[recommand[i]] = [1, i]
    

ans = sorted(candidate.keys())
for i in ans:
    print(i, end=" ")
    
    
'''
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
recommand = list(map(int, input().split()))

candidate = dict()
for i in range(M):
    if len(candidate) < N: # 자리 O
        candidate[recommand[i]] = [1, i]  # [추천수, timestamp]
    else: # 자리 X
        # 이미 보유한 후보
        if recommand[i] in candidate:
            candidate[recommand[i]][0] += 1
        else: # 없어서 추가해야하는 경우
            # 추천 수 적고, timestamp 작은 값 우선적으로 삭제
            tDict = sorted(candidate.items(), key=lambda x: (x[1][0], x[1][1]))
            tIdx = tDict[0][0]
            del candidate[tIdx]
            candidate[recommand[i]] = [1, i]

ans = sorted(candidate.keys())
for i in ans:
    print(i, end=" ")
'''