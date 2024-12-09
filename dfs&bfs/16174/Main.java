
// visited 안 쓰면 메모리 초과 날 거라고 생각 못했음..
// 그래도 이번 기회에 java로 dfs bfs 돌리는거 조금 더 익숙해짐
import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[][] grid;
    static boolean rst = false;
    static int[] dx = { 1, 0 };
    static int[] dy = { 0, 1 };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        grid = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        BFS();
        if (rst) {
            System.out.print("HaruHaru");
        } else {
            System.out.print("Hing");
        }

        // System.out.print(grid[N-1][N-1]);
    }

    static void BFS() {
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[N][N];

        q.add(new int[] { 0, 0 });
        visited[0][0] = true;

        while (!q.isEmpty()) {
            int[] current = q.poll();
            int x = current[0];
            int y = current[1];

            if (grid[x][y] == -1) {
                rst = true;
                return;
            }

            for (int i = 0; i < 2; i++) {
                int nx = x + dx[i] * grid[x][y];
                int ny = y + dy[i] * grid[x][y];

                if (0 <= nx && nx < N && 0 <= ny && ny < N && !visited[nx][ny]) {
                    q.add(new int[] { nx, ny });
                    visited[nx][ny] = true;
                }

            }
        }

        // System.out.println(x + " " + y);
        // if (grid[x][y] == -1){
        // rst = true;
        // return;
        // }

        // for (int i=0; i<2; i++){
        // int nx = x + dx[i]*grid[x][y];
        // int ny = y + dy[i]*grid[x][y];

        // if (0 <= nx && nx < N && 0 <= ny && ny <N){
        // DFS(nx, ny);
        // }
        // }
    }
}