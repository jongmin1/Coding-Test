import heapq as hq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, K = map(int, input().split())
distance = [INF]*100001

def dijkstra(start):
    distance[start] = 0
    q = []
    hq.heappush(q, (0, start))
    
    while q:
        dist, now = hq.heappop(q)
        if distance[now] < dist:
            continue
        for n in (now*2, now-1, now+1):
            if n < 0 or n > 100000:
                continue
            
            cost = dist
            if n != now*2:
                cost += 1
            
            if cost < distance[n]:
                distance[n] = cost
                hq.heappush(q, (cost, n))
                
dijkstra(N)
print(distance[K])
