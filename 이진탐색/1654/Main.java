// 랜선 자르기
// 시도 횟수 : 1
// 참고 여부 O
// 사유 : 이진탐색 익숙하지 않아서

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int K = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        
        long[] cable = new long[K];
        
        long max = 0;
        for(int i = 0; i < K; i++){
            cable[i] = Long.parseLong(br.readLine());
            max = Math.max(max, cable[i]);    
        }
        
        long left = 1;
        long right = max;
        long ans = 0;
        while(left <= right){
            long mid = (left + right) / 2;
            
            long countCable = 0;
            for(int i = 0; i < K; i++){
                countCable += cable[i] / mid;
            }
            
            if(countCable < N){
                right = mid - 1;
            }
            else{
                ans = mid;
                left = mid + 1;
            }
        }
        System.out.println(ans);
    }
}
