// 공유기 설치(파라미터 서치)
// 시도 횟수 : 1
// 참고 여부 : 세모
// 사유 : 그렇게 풀면 되는지 확인해봄. 
// 헷갈렸던 부분 : 간격이 일정하지 않고 어디는 3, 어디는 4, 이렇게 찍힐 수도 있단 생각을함
// 근데 이러한 부분은 그냥 첫번째꺼 설치 고정해두면 남는 칸은 뒤에 몰려있어서, 어차피 인접한 것의 최소 거리 구할 땐 고려할 필요 없게 됨

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        
        int[] houses = new int[N];
        
        for(int i = 0; i < N; i++){
            houses[i] = Integer.parseInt(br.readLine());
        }
        
        Arrays.sort(houses);
        
        int left = 1;
        int right = houses[N-1] - houses[0];
        int ans = 0;
        while(left <= right){
            int interval = (left + right) / 2;
            
            if(possible(houses, C, interval)){
                // System.out.println(interval);
                ans = interval;
                left = interval + 1;
            }
            else{
                right = interval -1;
            }
        }
        System.out.print(ans);
    }
    
    static boolean possible(int[] h, int c, int interval){
        int count = 1;
        int pre = h[0];
        // 직전에 설치한 것과 interval 만큼 차이가 나면서
        for(int i = 1; i < h.length; i++){
            if( h[i] - pre >= interval ){
                pre = h[i];
                count++;    
            }
        }
        return count >= c ? true : false;
    }
}
