// 시도 횟수 : 1
// 참고 여부 : X

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());
        
        int[] time = new int[N+1];
        int[] point = new int[N+1];
        for(int i = 1; i <= N; i++){
            st = new StringTokenizer(br.readLine());
            time[i] = Integer.parseInt(st.nextToken());
            point[i] = Integer.parseInt(st.nextToken());
        }
        
        int[][] dp = new int[N+1][T+1];
        
        for(int i = 1; i <= N; i++){
            for(int j = T; j >= 0; j--){
                if(time[i] <= j ){
                    dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-time[i]] + point[i]);
                }
                else{
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        System.out.println(dp[N][T]);
    }
}
