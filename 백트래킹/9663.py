# 백트랙킹 기본 문제... 난 몰랐다..

import sys
input = sys.stdin.readline
N = int(input())
row = [0]*N

def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x - i):
            return 0
    return 1

def queen(x):
    if x == N:
        return 1

    cnt = 0
    for i in range(N):
        row[x] = i
        if check(x):
            cnt += queen(x+1)
    return cnt

print(queen(0))