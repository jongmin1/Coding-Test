# dp 어렵네 흠

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().split())))
    
    if N == 1:
        print(max(stickers[0][0], stickers[1][0]))
        continue
    
    stickers[0][1] += stickers[1][0]
    stickers[1][1] += stickers[0][0]
    
    for j in range(2, N):
        stickers[0][j] += max(stickers[1][j-1], stickers[1][j-2])
        stickers[1][j] += max(stickers[0][j-1], stickers[0][j-2])
    
    print(max(stickers[0][N-1], stickers[1][N-1]))