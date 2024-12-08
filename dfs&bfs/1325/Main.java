import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static ArrayList<Integer>[] arr;
    static boolean visited[];
    static int maxValue;
    static int cntArr[];

    static void DFS(int x) {
        visited[x] = true;
        for (int i : arr[x]) {
            if (visited[i])
                continue;
            cntArr[i]++;
            DFS(i);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        visited = new boolean[N + 1];
        cntArr = new int[N + 1];

        arr = new ArrayList[N + 1];
        for (int i = 0; i < N + 1; i++)
            arr[i] = new ArrayList<Integer>();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(bf.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a].add(b);
        }

        for (int i = 1; i < N + 1; i++) {
            visited = new boolean[N + 1];
            DFS(i);
        }

        for (int i = 1; i < N + 1; i++) {
            maxValue = Math.max(maxValue, cntArr[i]);
        }

        for (int i = 1; i < N + 1; i++)
            if (maxValue == cntArr[i])
                System.out.print(i + " ");

    }
}