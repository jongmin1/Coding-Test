// 안전 영역
// 시도 횟수 : 1
// 참고 여부 : X

import java.util.*;
import java.io.*;

class Node{
    int x, y;
    
    public Node(int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static int N;
    static int[][] grid;
    static boolean[][] visited;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        N = Integer.parseInt(br.readLine());
        
        grid = new int[N][N];
        
        int maxHeight = -1;
        for(int i = 0; i < N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++){
                grid[i][j] = Integer.parseInt(st.nextToken());
                maxHeight = Math.max(maxHeight, grid[i][j]);
            }
        }
        
        int maxCount = 0;
        for(int k = 0; k < maxHeight; k++){ // 잠기는 높이에 따라
            int count = 0;
            visited = new boolean[N][N];
            // 안전지대 개수 세기
            for(int i = 0; i < N; i++){
                for(int j = 0; j < N; j++){
                    if(!visited[i][j] && grid[i][j] - k > 0){
                        bfs(i, j, k);   
                        count++;
                    }
                }
            }
            if (count == 0) break;
            maxCount = Math.max(maxCount, count);
        }
        
        // System.out.println(Arrays.toString(grid[N-1]));
        System.out.println(maxCount);
    }
    
    static void bfs(int sx, int sy, int h){
        Deque<Node> que = new ArrayDeque<>();
        visited[sx][sy] = true;
        que.add(new Node(sx, sy));
        
        while(!que.isEmpty()){
            Node now = que.pollFirst();
            
            for(int i = 0; i < 4; i++){
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                
                if(nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
                if(visited[nx][ny] || grid[nx][ny] - h <= 0) continue;
                
                que.add(new Node(nx, ny));
                visited[nx][ny] = true;
            }
        }
    }
}