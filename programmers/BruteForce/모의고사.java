import java.util.ArrayList;

class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        
        int[] a = {1,2,3,4,5};
        int[] b = {2,1,2,3,2,4,2,5};
        int[] c = {3,3,1,1,2,2,4,4,5,5};
        
        int[] count = new int[3];
        
        int tmp = 0;
        for(int i=0; i<answers.length; i++) {
            int answerTmp = answers[tmp];
            if(a[(tmp%5)] == answerTmp)
                count[0]++;
            if(b[(tmp%8)] == answerTmp)
                count[1]++;
            if(c[(tmp%10)] == answerTmp)
                count[2]++;
            tmp++;
        }
        
        int maxScore = Math.max(Math.max(count[0],count[1]),count[2]);
        ArrayList<Integer> list = new ArrayList<Integer>();
    
        if(maxScore == count[0]) list.add(1);
        if(maxScore == count[1]) list.add(2);
        if(maxScore == count[2]) list.add(3);
        
        answer = new int[list.size()];
        
        for(int i=0; i<answer.length; i++) {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}