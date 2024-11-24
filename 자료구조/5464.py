# 바로 컷!

from collections import deque
import sys
input = sys.stdin.readline

# N : 주차 공간의 수
# M : 차량 수
N, M =map(int, input().split()) 

# 주차 공간들의 단위 무게당 요금
s = [int(input()) for _ in range(N)]

# 각 차량의 무게
W = [int(input()) for _ in range(M)]

idx = [0]*2001 # 차량 주차한 위치

wating = deque()
occupied = [0]*(N)
totalRate = 0
for i in range(2*M):
    command = int(input())
    if command > 0:
        wating.append(command)
    
        cnt = 0
        while cnt < N:  # 자리 있는지 확인
            if occupied[cnt] == 0:
                break
            cnt += 1
            
        if cnt < N: # 자리 있으면
            target = wating.popleft()
            totalRate += s[cnt] * W[target-1]
            occupied[cnt] += 1
            idx[target] = cnt
    else:
        c = idx[abs(command)] # 차 뺄 자리
        occupied[c] = 0 # 차 빼기
        if wating:
            target = wating.popleft()
            totalRate += s[c] * W[target-1]
            occupied[c] += 1
            idx[target] = c

print(totalRate)