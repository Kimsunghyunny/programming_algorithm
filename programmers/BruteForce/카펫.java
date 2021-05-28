class Solution {
    public int[] solution(int brown, int yellow) {
        
        int x=0, y=0;
        int tmp = (brown-4)/2; // x+y = tmp 이고 x*y= yellow이다.
        for(int i=1; i< tmp; i++) {
            if(i*(tmp-i) == yellow){
                x = i+2;
                y = tmp-i+2;
            }
                
        }
        
        int[] answer = {x,y};
        return answer;
    }
}