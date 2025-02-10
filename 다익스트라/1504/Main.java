// 시도 횟수 : 3
// 참고 여부 : O
// 틀린 이유 : 
// -> 두 경로가 존재하지 않을 수도 있는 경우 고려 안 함
// -> 졸리다고 문제 끝까지 안 읽어서, -1 출력해야하는 경우 고려 안 함
// 느낀점 : 쉽다고 생각해도 두 번 의심하기 . 문제 잘 읽기...

import java.util.*;
import java.io.*;

class Node implements Comparable<Node>{
    int v;
    int w;
    
    public Node(int v, int w){
        this.v = v;
        this.w = w;
    }
    
    @Override
    public int compareTo(Node o){
        return this.w - o.w;
    }
}

public class Main {
    static int N;
    static int E;
    static List<ArrayList<Node>> graph;
    static int[] dist;
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        
        graph = new ArrayList<>();
        
        for(int i = 0; i <= N; i++){
            graph.add(new ArrayList<Node>());
        }
        
        for(int i = 0; i < E; i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            
            graph.get(u).add(new Node(v, w));
            graph.get(v).add(new Node(u, w));
        }
        
        st = new StringTokenizer(br.readLine());
        int v1 = Integer.parseInt(st.nextToken());
        int v2 = Integer.parseInt(st.nextToken());
        
        // 1. V -> V1 -> V2 -> Vn
        // V -> V1 
        
        boolean valid = true;
        dist = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dijkstra(1);
        int vtoV1 = dist[v1];
        if(vtoV1 == Integer.MAX_VALUE) valid = false;
        // V1 -> V2
        dist = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dijkstra(v1);
        int v1toV2 = dist[v2];
        if(v1toV2 == Integer.MAX_VALUE) valid = false;
        // V2 -> Vn
        dist = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dijkstra(v2);
        int v2toVn = dist[N];
        if(v2toVn == Integer.MAX_VALUE) valid = false;
        
        int route1 = valid ? vtoV1 + v1toV2 + v2toVn : Integer.MAX_VALUE;
        
        // 2. V -> V2 -> V1 -> Vn
        // V -> V2 
        valid = true;
        dist = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dijkstra(1);
        int vtoV2 = dist[v2];
        if(vtoV2 == Integer.MAX_VALUE) valid = false;
        // V2 -> V1
        dist = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dijkstra(v2);
        int v2toV1 = dist[v1];
        if(v2toV1 == Integer.MAX_VALUE) valid = false;
        // V1 -> Vn
        dist = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dijkstra(v1);
        int v1toVn = dist[N];
        if(v1toVn == Integer.MAX_VALUE) valid = false;
        
        int route2 = valid ? vtoV2 + v2toV1 + v1toVn : Integer.MAX_VALUE;
        
        if(route1 == Integer.MAX_VALUE && route2 == Integer.MAX_VALUE){
            System.out.println(-1);
        }
        else{
            System.out.println(Math.min(route1, route2));
        }
    }
    
    static void dijkstra(int x){
        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        dist[x] = 0;
        pq.add(new Node(x, 0));
        
        while (!pq.isEmpty()){
            Node now = pq.poll();
            
            if(dist[now.v] < now.w) continue;

            for(Node next : graph.get(now.v)){
                if(dist[next.v] >  dist[now.v] + next.w){
                    dist[next.v] = dist[now.v] + next.w;
                    pq.offer(new Node(next.v, dist[next.v]));
                }
            }
        } 
    }
}