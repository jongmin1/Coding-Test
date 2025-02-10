// 시도 횟수 : 1
// 참고 여부 : O
// 참고 이유 : 냅색 잘 몰라서

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] hp = new int[N+1];
        for(int i = 1; i <= N; i++){
            hp[i] = Integer.parseInt(st.nextToken());
        }
        
        st = new StringTokenizer(br.readLine());
        int[] joy = new int[N+1];
        for(int i = 1; i <= N; i++){
            joy[i] = Integer.parseInt(st.nextToken());
        }
        
        // System.out.println(Arrays.toString(L));
        int[][] dp = new int[N+1][100];
        for(int i = 0; i < 100; i++){
            dp[0][i] = 0;
        }
        for(int i = 0; i <= N; i++){
            dp[i][0] = 0;
        }
        
        for(int i = 1; i <= N; i++){
            for(int j = 1; j <= 99; j++){
                if(hp[i] > j){
                    dp[i][j] = dp[i-1][j];   
                }
                else{
                    dp[i][j] = Math.max(dp[i-1][j], joy[i] + dp[i-1][j - hp[i]]);
                }
            }
        }
        
        System.out.println(dp[N][99]);
         
    }
    
}