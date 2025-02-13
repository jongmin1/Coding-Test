// 시도 횟수 : 1
// 참고 여부 : 세모
// 사유 : 로직 맞는지 확인 + 조합

import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int M;
    static int[][] grid;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    static Deque<int[]> que;
    static int minTime = Integer.MAX_VALUE;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        grid = new int[N][N];
        List<int[]> two = new ArrayList<>();
        for(int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++){
                grid[i][j] = Integer.parseInt(st.nextToken());
                if(grid[i][j] == 2){
                    two.add(new int[] {i, j});
                    grid[i][j] = 0;    
                }
            }
        }

        que = new ArrayDeque<>();
        ArrayList<ArrayList<int[]>> combs = getCombinations(two, M);
        
        for(ArrayList<int[]> comb : combs){
            que.clear(); 
            for(int[] c : comb){
                que.add(c);
            }    
            int result = bfs();
            if(result != -1) {
                minTime = Math.min(minTime, result);
            }
        }
        
        System.out.println(minTime == Integer.MAX_VALUE ? -1 : minTime - 1);
    }
    
    static ArrayList<ArrayList<int[]>> getCombinations(List<int[]> points, int r) {
        ArrayList<ArrayList<int[]>> result = new ArrayList<>();
        combination(points, new boolean[points.size()], 0, r, result);
        return result;
    }
    
    static void combination(List<int[]> points, boolean[] visited, int start, int r, ArrayList<ArrayList<int[]>> result) {
        if(r == 0) {
            ArrayList<int[]> current = new ArrayList<>();
            for(int i = 0; i < visited.length; i++) {
                if(visited[i]) {
                    current.add(points.get(i));
                }
            }
            result.add(current);
            return;
        }
        
        for(int i = start; i < points.size(); i++) {
            visited[i] = true;
            combination(points, visited, i + 1, r - 1, result);
            visited[i] = false;
        }
    }
    
    static int bfs(){
        int[][] visited = new int[N][N];
        for(int[] virus : que) {
            visited[virus[0]][virus[1]] = 1;
        }
        
        while(!que.isEmpty()){
            int[] now = que.pollFirst();  
            
            for(int i = 0; i < 4; i++){
                int nx = now[0] + dx[i];
                int ny = now[1] + dy[i];
                
                if(nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
                if(grid[nx][ny] == 1) continue;  
                
                if(visited[nx][ny] == 0){
                    que.add(new int[]{nx, ny});
                    visited[nx][ny] = visited[now[0]][now[1]] + 1;
                }
            }
        }
        
        int maxTime = 0;
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                if(grid[i][j] != 1) {  
                    if(visited[i][j] == 0) return -1;  
                    maxTime = Math.max(maxTime, visited[i][j]);
                }
            }
        }
        return maxTime;
    }
}
