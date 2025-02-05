// 시도 횟수 : 2
// 참고 여부 : O
// for문 안에 if문 두개 같이 넣는거 헷갈려서 참고함

import java.io.*;
import java.util.*;

class Node {
    int k, x, y;

    public Node(int k, int x, int y) {
        this.k = k;
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static int K;
    static int W;
    static int H;
    static int[][] grid;
    static int[][][] visited;
    static int[] dmx = { 1, -1, 0, 0 };
    static int[] dmy = { 0, 0, 1, -1 };
    static int[] dkx = { -1, -2, -2, -1, 1, 2, 2, 1 };
    static int[] dky = { -2, -1, 1, 2, 2, 1, -1, -2 };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        K = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        W = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        grid = new int[H][W];
        visited = new int[K + 1][H][W];
        for (int i = 0; i < H; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < W; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(bfs());

    }

    static int bfs() {
        Queue<Node> queue = new LinkedList<>();
        visited[0][0][0] = 1;
        queue.offer(new Node(0, 0, 0));

        while (!queue.isEmpty()) {
            Node now = queue.poll();

            int k = now.k;
            int x = now.x;
            int y = now.y;
            for (int i = 0; i < 12; i++) {
                int nk, nx, ny;
                if (i < 4) {
                    nx = x + dmx[i];
                    ny = y + dmy[i];
                    nk = k;
                } else {
                    if (k >= K)
                        continue;
                    nx = x + dkx[i - 4];
                    ny = y + dky[i - 4];
                    nk = k + 1;

                }

                if (nx >= 0 && nx < H && ny >= 0 && ny < W
                        && visited[nk][nx][ny] == 0 && grid[nx][ny] == 0) {
                    visited[nk][nx][ny] = visited[k][x][y] + 1;
                    queue.offer(new Node(nk, nx, ny));
                }

            }
        }

        int ans = Integer.MAX_VALUE;
        for (int i = 0; i <= K; i++) {
            if (visited[i][H - 1][W - 1] != 0) {
                ans = Math.min(ans, visited[i][H - 1][W - 1]);
            }
        }
        return ans == Integer.MAX_VALUE ? -1 : ans - 1;
    }

}