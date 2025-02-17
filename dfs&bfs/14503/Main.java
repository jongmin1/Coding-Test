// 로봇청소기
// 시도 횟수 : 1
// 참고 여부 : 세모
// 디버깅 귀찮아서 그냥 지피티에 확인하고 제출함
// ny <= M 이런 타이포 있는거 빼고 특별히 문제있는 부분은 없었음
// DFS로 더 편히 풀 수 있었는데 조건 그냥 갖다 적용해서 코드가 길어짐.

import java.util.*;
import java.io.*;

class Node {
    int x, y, d;

    public Node(int x, int y, int d) {
        this.x = x;
        this.y = y;
        this.d = d;
    }

    @Override
    public String toString() {
        return "x: " + x + " y: " + y + " d: " + d;
    }
}

public class Main {
    static int N;
    static int M;
    static int[][] grid;
    static boolean[][] visited;
    static int count;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int sx = Integer.parseInt(st.nextToken());
        int sy = Integer.parseInt(st.nextToken());
        int sd = Integer.parseInt(st.nextToken());

        grid = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        bfs(sx, sy, sd);

        System.out.println(count);
    }

    static void bfs(int x, int y, int d) {
        Deque<Node> que = new ArrayDeque<>();
        visited = new boolean[N][M];
        que.add(new Node(x, y, d));
        visited[x][y] = true; 

        while (!que.isEmpty()) {
            Node now = que.pollFirst();

            // 현재 칸이 청소되지 않은 경우, 청소
            if (grid[now.x][now.y] == 0) {
                count++;
                grid[now.x][now.y] = 2; // 청소 완료 표시
            }

            boolean toClean = false;
            for (int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];

                if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;

                if (grid[nx][ny] == 0 && !visited[nx][ny]) {
                    toClean = true;
                    break;
                }
            }

            if (!toClean) {
                // 후진할 수 있다면
                int back = (now.d + 2) % 4;
                int nx = now.x + dx[back];
                int ny = now.y + dy[back];

                if (nx >= 0 && ny >= 0 && nx < N && ny < M && grid[nx][ny] != 1) {
                    que.add(new Node(nx, ny, now.d));
                } else {
                    return;
                }
            } else {
                // 반시계 방향으로 회전
                int i = (now.d + 3) % 4;

                // 한 칸 전진 가능하면 이동
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];

                if (nx >= 0 && ny >= 0 && nx < N && ny < M && grid[nx][ny] == 0 && !visited[nx][ny]) {
                    que.add(new Node(nx, ny, i));
                    // visited[nx][ny] = true; // 이동할 때 방문 처리
                } else {
                    que.add(new Node(now.x, now.y, i)); // 방향만 변경
                }
            }
        }
    }
}
