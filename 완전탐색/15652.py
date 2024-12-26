# 헷갈리네 흠

import sys
input = sys.stdin.readline

def dfs(at, depth):
    if depth == M:
        print(*arr)
        return 
        
    for i in range(at, N):
        arr.append(S[i])
        dfs(i, depth + 1)
        arr.pop()

N, M = map(int, input().split())
S = range(1, N+1)
arr = []
dfs(0, 0)
