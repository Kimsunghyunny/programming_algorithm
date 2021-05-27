import java.util.Arrays;

class Solution {
    public long solution(int n, int[] times) {
        
        long answer = 0;
        
        Arrays.sort(times); // 심사관 시간 정렬
        
        long st = 0;
        long en = (long) n * times[times.length-1];
        
        while(st <= en) {
            System.out.println("en = "+en+"     ");
            long mid = (st + en) /2;
            long sum =  0;
            
            System.out.println("mid = " + mid);
            
            for(int i=0; i<times.length; i++) {
                sum += mid / times[i];
                System.out.println(sum);
            }
            if(sum >= n) { 
                en = mid-1;
                answer = mid;
            }
            else { // 심사해야할 사람들을 모두 심사 하지 못함
                st = mid+1;
            }
        }
        return answer;
    }
}