// 파티티
// 시도 횟수 : 1
// 참고 여부 : O
// 사유 : 다익스트라 continue 조건 헷갈렸고, 돌아가는 거 확인 안 했었음음
import java.util.*;
import java.io.*;

class Node implements Comparable<Node>{
    int v, w;
    
    public Node(int v, int w){
        this.v = v;
        this.w = w;
    }
    
    @Override
    public int compareTo(Node o){
        return Integer.compare(this.w, o.w);
    }
}

class Main {
    static int N;
    static int M;
    static int X;
    static List<ArrayList<Node>> graph;
    static int[] dist;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 입력
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());
        
        graph = new ArrayList<>();
        for(int i = 0; i <= N; i++){
            graph.add(new ArrayList<Node>());
        }
        
        for(int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph.get(u).add(new Node(v, w));
        }
        
        for(int i = 1; i <= N; i++){
            Collections.sort(graph.get(i));
            // for (Node node : graph.get(i)) {
            //     System.out.print("{" + i + "," + node.v + "," + node.w + "} ");
            // }
            // System.out.println();
        }
        
        // 다익스트라로 돌려서 각각이 X가는데 얼마나 걸리는지 확인
        int longest = 0;
        dijkstra(X);
        int[] fromX = dist.clone();
        for(int i = 1; i <= N; i++){
          
            dijkstra(i);
            int distance = dist[X] + fromX[i];
            longest = Math.max(longest, distance);
            // System.out.println(dist[X] + fromX[i]);
            // System.out.println(Arrays.toString(dist));
        }
        System.out.println(longest);
    }

    static void dijkstra(int x){
        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        dist = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        pq.add(new Node(x,0));
        dist[x] = 0;

        while(!pq.isEmpty()){
            Node now = pq.poll();

            if(dist[now.v] < now.w) continue;
            // System.out.println(dist[now.v] + " " + now.v);

            for(Node next : graph.get(now.v)){
                if(dist[next.v] > dist[now.v]+next.w){
                    dist[next.v] = dist[now.v]+next.w;
                    pq.add(new Node(next.v, dist[next.v]));
                }
            }
        }

    }
}
