import java.util.ArrayList;
import java.util.Collections;

class Solution {
    int[] visited;
    String str = "";
    ArrayList<String> list = new ArrayList<String>();
    public void dfs(String current,int count,String[][] tickets ){
        str+= current+",";
        if(count == tickets.length){
           list.add(str);
            return ;
        }

        for(int i=0;i<tickets.length;i++){
            if(visited[i]!=1&&tickets[i][0].equals(current)){
                visited[i]=1; 
                dfs(tickets[i][1],count+1,tickets);
                visited[i]=0;
                str="";
            }
        }
    }
    public String[] solution(String[][] tickets) {
        
        int size=tickets.length;
        visited=new int[size];
        
        for(int i=0;i<size;i++){
            if(tickets[i][0].equals("ICN")){
                visited[i]=1;
                str="ICN,";
                dfs(tickets[i][1],1,tickets);
                visited[i]=0;
            }
        }
        Collections.sort(list);
		String[] answer = list.get(0).split(",");
        return answer;
    }
}