// 소셜 네트워킹 어플리케이션
// 시도 횟수 : 1
// 참고 여부 : O
// 참고 이유 : 유니온 파인드 최적화 코드 까먹었음

import java.util.*;
import java.io.*;

public class Main {
    static int[] parent;
    static int[] rank;
    
    static int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }
    
    static boolean union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);
        
        if (rootA == rootB) {
            return false;
        } 
        
        if (rank[rootA] < rank[rootB]) {
            parent[rootA] = rootB;
        } else if (rank[rootA] > rank[rootB]) {
            parent[rootB] = rootA;
        } else {
            parent[rootB] = rootA;
            rank[rootA]++;
        }
        return true;
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder(); 
        
        int T = Integer.parseInt(br.readLine());
        int count = 1;
        while (T-- > 0) {
            int numUser = Integer.parseInt(br.readLine());
            int E = Integer.parseInt(br.readLine());

            parent = new int[numUser];
            rank = new int[numUser];
            for (int i = 0; i < numUser; i++) {
                parent[i] = i;
                rank[i] = 0; 
            }

            for (int i = 0; i < E; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                union(u, v);
            }

            int K = Integer.parseInt(br.readLine());
            sb.append("Scenario ").append(count++).append(":\n");

            for (int i = 0; i < K; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine()); 
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                
                if (find(x) == find(y)) {
                    sb.append(1).append("\n");
                } else {
                    sb.append(0).append("\n");
                }
            }
            sb.append("\n");
        }
        
        System.out.print(sb);
    }
}
