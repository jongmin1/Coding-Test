// 스도쿠쿠
// 시도 횟수 : 3
// 참고 여부 : O
// 사유 : 벡트랙킹 오랜만에 풀어서 감 잃었었던 것 같음. 그리고 너무 생각 안 하려는거 같은데 정신차리기.

import java.util.*;
import java.io.*;

class Point{
    int x, y;
    
    public Point(int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static int[][] grid;
    static ArrayList<Point> zeros;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        grid = new int[9][9];
        zeros = new ArrayList<>(); 
        for(int i = 0; i < 9; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < 9; j++){
                grid[i][j] = Integer.parseInt(st.nextToken());
                if(grid[i][j] == 0) zeros.add(new Point(i, j));
            }    
        }
        
        sudoku(0);
    }
    
    static boolean check(int x, int y, int num){
        
        // 가로, 세로
        for(int i = 0; i < 9; i++){
            if(grid[i][y] == num || grid[x][i] == num){
                return false;
            }
        }
        
        // 3*3
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                if(grid[(x/3)*3 + i][(y/3)*3 + j] == num){
                    return false;
                }
            }
        }
        
        return true;
    }
    
    static void sudoku(int depth){
        if(depth == zeros.size()){
            StringBuilder sb = new StringBuilder();
            for(int i = 0; i < 9; i++){
                for(int j = 0; j < 9; j++){
                    sb.append(grid[i][j] + " ");
                }
                sb.append("\n");
            }
            System.out.print(sb);
            System.exit(0);
        }
        
        Point zero = zeros.get(depth);
        for(int i = 1; i < 10; i++){
            if(check(zero.x, zero.y, i)){
                grid[zero.x][zero.y] = i;
                sudoku(depth+1);   
                grid[zero.x][zero.y] = 0;
            }
        }
    }
}