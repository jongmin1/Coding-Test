import heapq as hq
import sys
input = sys.stdin.readline
INF = int(1e9)

def main():
    V, E = map(int, input().split())
    K = int(input())
    
    graph = [[] for i in range(V+1)]
    distance = [INF]*(V+1)
    
    for i in range(E):
        u, v, w = map(int, input().split())  # u -> v, w: 비용
        graph[u].append((v, w))  
   
    
    def dijkstra(start):
        q = []
        hq.heappush(q, (0, start))
        distance[start] = 0
        
        while q:
            dist, now = hq.heappop(q)   # dist: 지금까지의 최단거리, now: 현재 방문한 정점
            if distance[now] < dist:  # 현재 노드의 최단거리 < 현재 정점으로 넘어오는데 든 거리
                continue          # 이미 최단 거리 구한 노드이므로
            
            for v, w in graph[now]: 
                cost = dist + w    # 현재 정점까지 걸린 거리 + 갈 거리 
                if cost < distance[v]:
                    distance[v] = cost
                    hq.heappush(q, (cost, v))
            
    dijkstra(K)
    
    for num in range(1,V+1):
        if distance[num] == INF:
            print("INF")
        else:
            print(distance[num])
            
if __name__ == '__main__':
    main()