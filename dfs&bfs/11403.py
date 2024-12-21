import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = [[0]*N for _ in range(N)]
adjList = [[] for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            adjList[i+1].append(j+1)

def bfs(x):
    path = set()
    visited = [0]*(N+1)
    q = deque([x])

    while q:
        x = q.popleft()

        for nx in adjList[x]:
            if not visited[nx]:
                q.append(nx)
                visited[nx] = 1
                path.add(nx)
    return path

for i in range(N):
    p = bfs(i+1)
    for j in range(N):
        if j+1 in p:
            answer[i][j] = 1

for i in range(N):
    for j in range(N):
        print(answer[i][j], end=" ")

    print()