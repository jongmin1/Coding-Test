// 시도 횟수 : 1
// 참고 여부 : O
// 사유 : 사이클 찾았을 때 처리하는 방법(사이클 순회) 몰랐음

import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[] arr;
    static boolean[] visited;
    static boolean[] cycleChecked;
    static int count;
    static List<Integer> path;
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        
        while(T-- > 0){
            N = Integer.parseInt(br.readLine());
            count = 0;
            
            arr = new int[N+1];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int i = 1; i <= N; i++){
                arr[i] = Integer.parseInt(st.nextToken());
            }
            
            path = new ArrayList<Integer>();
            visited = new boolean[N+1];
            cycleChecked = new boolean[N+1];
            int ans = N;
            for(int i = 1; i <= N; i++){
                if(!visited[i]){
                    dfs(i);
                    // System.out.println(ans + " " + count);
                }
            }
            
            System.out.println(N - count);
            
        }
    }
        
    static void dfs(int x){
        visited[x] = true;
        
        int next = arr[x];
        if(!visited[next]){
            dfs(next);
        }
        else if(!cycleChecked[next]){
            count++;
            for(int i = next; i != x; i = arr[i]){
                count++;
            }
        }
        cycleChecked[x] = true;
    }

}
