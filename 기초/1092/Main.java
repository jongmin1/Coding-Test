// 시도 횟수 : 1
// 참고 여부 : O
// ArrayList, Collections 사용법 + 멘탈 나가서 그냥 보고 품

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        Integer[] crane = new Integer[N];
        for (int i = 0; i < N; i++) {
            crane[i] = Integer.parseInt(st.nextToken());
        }

        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        List<Integer> box = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            box.add(Integer.parseInt(st.nextToken()));
        }

        Arrays.sort(crane, Collections.reverseOrder());
        Collections.sort(box, Collections.reverseOrder());

        if (box.get(0) > crane[0]) {
            System.out.println(-1);
            return;
        }

        int time = 0;
        while (!box.isEmpty()) {
            int index = 0;
            for (int i = 0; i < N; i++) {

                if (index >= box.size())
                    break;

                while (index < box.size()) {
                    if (crane[i] >= box.get(index)) {
                        box.remove(index);
                        break;
                    }
                    index++;
                }
            }
            time++;
        }
        System.out.println(time);
    }
}
