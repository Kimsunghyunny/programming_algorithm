package Main;
class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        
        boolean[] check = new boolean[n];
        
        for(int i=0; i<n; i++) {
            if(!check[i]) {
                dfs(i, computers, check);
                answer++;
            }
        }
        
        return answer;
    }
    
    public boolean[] dfs(int i, int[][] computers, boolean[] check) {
        check[i] = true;
        
        for(int j=0; j<computers.length; j++) {
            if(i!=j && check[j] == false && computers[i][j] == 1){
                check = dfs(j, computers, check);
            }
        }
        return check;
    }
    
}