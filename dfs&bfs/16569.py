from collections import deque
import sys
input = sys.stdin.readline

M, N, V = map(int, input().strip().split())
X, Y = map(int, input()) # 재상이 위치

height = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(V+1)]

for i in range(V):
    x, y, t = map(int , input())
    graph[] 
