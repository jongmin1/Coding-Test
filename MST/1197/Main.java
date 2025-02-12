// 시도 횟수 : 1
// 참고 여부 : O
// 사유 : 아직 안 익숙해서 어제 푼 MST 문제 참고해서 품

import java.util.*;
import java.io.*;

class Edge implements Comparable<Edge>{
    int u, v, w;
    
    public Edge(int u, int v, int w){
        this.u = u;
        this.v = v;
        this.w = w;
    }
    
    @Override
    public int compareTo(Edge o){
        return Integer.compare(this.w, o.w);
    }
}

public class Main {
    static int[] rank;
    static int[] parent;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        
        List<Edge> edges = new ArrayList<Edge>();
        for(int i = 0; i < E; i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            edges.add(new Edge(u, v, w));
        }
        
        rank = new int[V+1];
        parent = new int[V+1];
        for(int i = 1; i <= V; i++){
            parent[i] = i;
        }
        
        Collections.sort(edges);
        int totalWeight = 0;
        for(Edge edge : edges){
            if(find(edge.u) != find(edge.v)){
                union(edge.u, edge.v);
                totalWeight += edge.w;
            }
        }
        System.out.println(totalWeight);
    }
    
    static int find(int x){
        if (parent[x] == x) return x;
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
