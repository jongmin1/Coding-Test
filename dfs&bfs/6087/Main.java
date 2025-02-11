// 문제 이름 : 레이저 통신
// 시도 횟수 : 4
// 참고 여부 : O
// 참고한 부분 : 거울 놓는 방법과 거울별로 방향전환시킨 것들 개수 어떻게 쌓아가는지지
// 느낀점 : 문제를 어렵게 생각할 필요가 없음, 단순화 시켜야함. 3차원으로 bfs 돌리는거 아직 안 익숙함
// 이번 문제도 그냥 방향 전환 몇 번하는지를 생각하고 풀면 괜히 쉽게 느껴지는 것과 같이!

import java.util.*;
import java.io.*;

class Point implements Comparable<Point>{
    int x, y, dir, mirror;
    
    public Point(int x, int y, int dir, int mirror){
        this.x = x;
        this.y = y;
        this.dir = dir;
        this.mirror = mirror;
    }
    
    public int compareTo(Point o){
        return Integer.compare(this.mirror, o.mirror);
    }
}

public class Main {
    static int W;
    static int H;
    static char[][] grid;
    static int[][] visited;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        W = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        
        grid = new char[H][W];
        
        List<int[]> posC = new ArrayList<>();
        for(int i = 0; i < H; i++){
            String line = br.readLine();
            for(int j = 0; j < W; j++){
                grid[i][j] = line.charAt(j);
                if(grid[i][j] == 'C'){
                    posC.add(new int[]{i, j});
                }
            }
        }
        
        int ans = bfs(posC.get(0), posC.get(1));
        System.out.println(ans);
        
    }
    
    
    static int bfs(int[] start, int[] end){
        PriorityQueue<Point> pq = new PriorityQueue<>();
        visited = new int[H][W];
        for(int i = 0; i < H; i++) Arrays.fill(visited[i], Integer.MAX_VALUE);
        pq.add(new Point(start[0], start[1], -1, 0));
        
        while(!pq.isEmpty()){
            Point now = pq.poll();
            
            // System.out.print(now.x);
            // System.out.println(now.y);
            if(now.mirror > visited[now.x][now.y]) continue;
            
            if(now.x == end[0] && now.y == end[1]){
                return visited[end[0]][end[1]];
            }
            
            for(int i = 0; i < 4; i++){
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                
                if(nx < 0 || nx >= H || ny < 0 || ny >= W) continue;
                if(grid[nx][ny] == '*') continue;
                
                if(now.dir != i && now.dir != -1){
                    if(visited[nx][ny] > now.mirror + 1){
                        visited[nx][ny] = now.mirror + 1;
                        pq.add(new Point(nx, ny, i, now.mirror + 1));
                    }
                }
                else{
                    if(visited[nx][ny] > now.mirror){
                        visited[nx][ny] = now.mirror;
                        pq.add(new Point(nx, ny, i, now.mirror));
                    }
                }
            }   
        }
        // System.out.println(Arrays.toString(visited[H-1]));
        return -1;
    }
}
