// 시도횟수: 1
// 참고 여부: O
// 사유 : MST 잘 몰라서 봄
// 헷갈린 점: A국가 -> B국가 이동하는 비행기 1이 B국가 -> C국가로 이동할 때도 사용될 수 있을거라고 생각함. 이게 일반적이지 않다는데 흠...
// 저런 조건 없으면 모든 간선 수 = 노드 수 - 1
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int T = Integer.parseInt(br.readLine());
        while(T-- > 0){
            StringTokenizer st = new StringTokenizer(br.readLine());
            
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            for(int i = 0; i < M; i++){
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
            }
            System.out.println(N -1);
        }
    }
}