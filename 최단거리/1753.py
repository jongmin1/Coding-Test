import sys
import heapq as hq
import sys
input = sys.stdin.readline
INF = int(1e9) 

def main():
    V,E = map(int, input().split())
    K = int(input())
    
    graph = [[] for _ in range(V+1)]
    distance = [INF] * (V+1)

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v,w)) 

    def dijkstra(start):
        queue = []
        hq.heappush(queue, (0,start)) 
        distance[start] = 0

        while queue:
            dist, now = hq.heappop(queue)
            if distance[now] < dist: 
                continue

            for v,w in graph[now]:
                cost = dist + w 
                if cost < distance[v]:
                    distance[v] = cost
                    hq.heappush(queue,(cost,v))

    dijkstra(K)

    for num in range(1,V+1):
        if distance[num] == INF:
            print("INF")
        else:
            print(distance[num])


if __name__ == '__main__':
    main()