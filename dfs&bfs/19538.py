'''
문제 이해
1. 루머를 퍼트릴 때, 연결된 노드로 전달할 거야
2. 연결된 모든 노드의 과반수가 루머를 믿고 있어야 나도 믿을거야
    -> 내가 루머를 믿지 않으니 다른 사람에게 전달도 안 할거야
    -> 나랑 이어진 노드들 방문할 필요 없어
=> 루머를 동시에 여러 곳에 퍼트릴건데, 각 노드는 주변의 과반수 이상이 루머를 믿고 있어야 같이 루머를 퍼트릴거임
=> 관리해야할 거는 루머를 믿을(주변 과반수 이상이 루머를 믿고있는) 노드와 더 루머 전달 시간 더 줄일 수 있는지 
'''

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = []
network = [set() for _ in range(N+1)]
for i in range(1, N+1):
    graph.append(list(map(int, input().split())))
    for c in graph[-1]:
        if c == 0: continue
        network[i].add(c)
        network[c].add(i)

M = int(input())
start = list(map(int, input().strip().split()))

dist = [[-1, 0] for _ in range(N+1)]
for i in start:
    dist[i][1] = N  # 주변에 믿는 사람 수 
    dist[i][0] = 0  # 루머 받는데 걸린 시간

def bfs():
    q = deque(start)
    
    while q:
        x = q.popleft()
        
        for nx in network[x]:
            dist[nx][1] += 1

            # 주변에 믿는 사람이 과반수 이상이면
            if len(network[nx])/2 <= dist[nx][1]:
                # 아직 루머 전달 못받았거나 직전 먼 거리로 전달받은거라면 
                if dist[nx][0] == -1 or dist[nx][0] > dist[x][0] + 1:
                    dist[nx][0] = dist[x][0] + 1
                    q.append(nx)
bfs()

print(" ".join(map(str, [d[0] for d in dist[1:]])))