import java.util.*;
import java.io.*;

public class Main {
    static int M;
    static int N;
    static char[][] grid;
    static boolean[][] visited;
    static int cntW = 0;
    static int cntB = 0;
    static int cnt = 0;
    static int nx = 0;
    static int ny = 0;

    static int dx[] = { 1, -1, 0, 0 };
    static int dy[] = { 0, 0, 1, -1 };

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        N = Integer.parseInt(st.nextToken()); // 가로
        M = Integer.parseInt(st.nextToken()); // 세로

        grid = new char[M][N];
        visited = new boolean[M][N];
        for (int i = 0; i < M; i++) {
            String str = bf.readLine();
            for (int j = 0; j < N; j++) {
                grid[i][j] = str.charAt(j);
            }
        }
        // System.out.println(grid[0][0] + " " + grid[M-1][N-1]);

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (!visited[i][j]) {
                    DFS(i, j, grid[i][j]);
                    if (grid[i][j] == 'W') {
                        cntW += cnt * cnt;
                    } else {
                        cntB += cnt * cnt;
                    }
                    cnt = 0;
                }
            }
        }
    }

    static void DFS(int x, int y, char color) {
        visited[x][y] = true;
        cnt += 1;

        for (int i = 0; i < 4; i++) {
            nx = x + dx[i];
            ny = y + dy[i];

            if (inRange(nx, ny) && visited[nx][ny] && grid[nx][ny] == color) {
                DFS(nx, ny, color);
            }
        }
        System.out.print(cntW + " " + cntB);
    }

    static boolean inRange(int x, int y) {
        return (0 <= x && x < M && 0 <= y && y < N);
    }
}