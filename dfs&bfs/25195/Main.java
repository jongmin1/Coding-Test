import java.util.*;
import java.io.*;

public class Main {
    static ArrayList<Integer>[] arr;
    static ArrayList<Integer> gomgom = new ArrayList<>();
    static boolean check = false;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());

        arr = new ArrayList[N + 1];
        for (int i = 0; i < N + 1; i++) {
            arr[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a].add(b);
        }

        st = new StringTokenizer(br.readLine());
        int S = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < S; i++) {
            int a = Integer.parseInt(st.nextToken());
            gomgom.add(a);
        }
        // System.out.print(gomgom.get(0));
        DFS(1);
        System.out.print(check ? "yes" : "Yes");
    }

    static void DFS(int cur) {
        if (check || gomgom.contains(cur))
            return;
        if (arr[cur].size() == 0) {
            check = true;
            return;
        }

        for (int next : arr[cur]) {
            DFS(next);
        }
    }
}