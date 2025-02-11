// 시도 횟수 : 4
// 참고 여부 : O
// 틀린 이유 : 시간 초과뜸
// 배운점 : 조건문 상반되는건 공통으로 뽑아서 if, else로 처리하고 나머지 조건 확인해야 함

import java.util.*;
import java.io.*;

class Node{
    int x, y, b;
    
    public Node(int x, int y, int b){
        this.x = x;
        this.y = y;
        this.b = b;
    }
}

public class Main {
    static int N;
    static int M;
    static int K;
    static char[][] grid;
    static int[][][] visited;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        
        grid = new char[N][M];
        
        for(int i = 0; i < N; i++){
            String line = br.readLine();
            for(int j = 0; j < M; j++){
                grid[i][j] = line.charAt(j);
            }
        }
        // for(int i = 0; i < N; i++){
            // System.out.println(Arrays.toString(grid[i]));
        // }
        
        visited = new int[N][M][K+1];
        
        System.out.println(bfs(0, 0));
        
    }
    
    static int bfs(int sx, int sy) {
        Queue<Node> que = new LinkedList<>();
        que.add(new Node(sx, sy, 0));
        
        // 모든 상태를 0으로 초기화
        for(int i = 0; i < N; i++)
            for(int j = 0; j < M; j++)
                Arrays.fill(visited[i][j], 0);
                
        visited[sx][sy][0] = 1;
        
        while(!que.isEmpty()) {
            Node now = que.poll();
            
            if(now.x == N-1 && now.y == M-1) {
                return visited[now.x][now.y][now.b];
            }
            
            for(int i = 0; i < 4; i++) {
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                
                if(nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
                
                // 벽이 아닌 경우
                if(grid[nx][ny] == '0') {
                    if(visited[nx][ny][now.b] == 0) {
                        visited[nx][ny][now.b] = visited[now.x][now.y][now.b] + 1;
                        que.add(new Node(nx, ny, now.b));
                    }
                }
                // 벽인 경우
                else if(now.b < K) {
                    if(visited[nx][ny][now.b + 1] == 0) {
                        visited[nx][ny][now.b + 1] = visited[now.x][now.y][now.b] + 1;
                        que.add(new Node(nx, ny, now.b + 1));
                    }
                }
            }
        }
        return -1;
    }
}