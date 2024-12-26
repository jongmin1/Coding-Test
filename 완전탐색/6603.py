# 완전 탐색 라이브러리 안 쓰고!

import sys
input = sys.stdin.readline

def dfs(depth, index):
    if depth == 6:
        print(*arr)
        return
    
    for i in range(index, K):
        arr.append(S[i])
        dfs(depth + 1, i+ 1)
        arr.pop()


while 1:
    
    T = list(map(int, input().split()))
    
    K = T[0]
    S = T[1:]
    
    if K == 0:
        break
    
    arr = []
    dfs(0, 0)
    
    print()