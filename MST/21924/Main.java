// 시도 횟수 : 1
// 참고 여부 : O
// 이유 : 처음 풀어본 MST
// 크루스칼: 정렬 -> 가중치 낮은 간선부터 하나씩 넣기

import java.util.*;
import java.io.*;

class Edge implements Comparable<Edge>{
    int u, v;
    long cost;
    
    public Edge(int u, int v, long cost){
        this.u = u;
        this.v = v;
        this.cost = cost;
    }
    
    @Override
    public int compareTo(Edge o){
        return Long.compare(this.cost, o.cost);
    }
}

public class Main {
    static int N;
    static int M;
    static int[] parent;
    static int[] rank;
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        parent = new int[N+1];
        rank = new int[N+1];
        for(int i = 1; i <= N; i++){
            parent[i] = i;
            rank[i] = 0;
        }
        
        long totalCost = 0;
        List<Edge> edges = new ArrayList<Edge>();
        for(int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            totalCost += c;
            edges.add(new Edge(u, v, c));
        }
        
        Collections.sort(edges);
        long mstCost = 0;
        int connectedEdges = 0;
        
        for(Edge edge : edges){
            if(find(edge.u) != find(edge.v)){
                union(edge.u, edge.v);
                mstCost += edge.cost;
                connectedEdges ++;    
            }
        }
        
        boolean isConnected = true;
        int root = find(1);
        for(int i = 2; i <= N; i++){
            if(find(i) != root){
                isConnected = false;
                break;
            }
        }
        
        if( !isConnected || connectedEdges != N-1 ){
            System.out.println(-1);
        }
        else{
            System.out.println(totalCost - mstCost);
        }
        
    }
    
    static int find(int x){
        if(parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }
    
    static void union(int a, int b){
        int rootA = find(a);
        int rootB = find(b);
        
        if(rootA == rootB) return;
        
        if(rank[rootA] < rank[rootB]){
            parent[rootA] = rootB;
        }
        else if(rank[rootA] > rank[rootB]){
            parent[rootB] = rootA;
        }
        else{
            parent[rootB] = rootA;
            rank[rootA]++;
        }
    }
}