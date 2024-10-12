import heapq as hq
import sys
input = sys.stdin.readline
INF = int(1e9)

V = int(input())
B = int(input())

graph = [[] for i in range(V+1)]
distance = [INF] * (V+1)
prev = [0]*(V+1)

for i in range(B):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dep, arrive = map(int, input().split())

 
def dijkstra(start):
    q = []
    hq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = hq.heappop(q)
        if distance[now] < dist:
            continue
        
        for v, w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                prev[v] = now
                hq.heappush(q, (cost, v))

dijkstra(dep)

path = [arrive]
temp = arrive
while (temp != dep):
    temp = prev[temp]
    path.append(temp)

path.reverse()

print(distance[arrive])
print(len(path))
for i in path:
    print(i, end=" ")