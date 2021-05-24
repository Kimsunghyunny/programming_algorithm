package Main;
class Solution {
    
    int answer = 0;
    public int solution(int[] numbers, int target) {
        dfs(numbers, target, 0, 0);
        return answer;
    }
    
    public void dfs(int[] numbers, int target, int idx, int sum) {
        if(idx == numbers.length) {
            if(sum == target){
                answer++;
            }
            return;
        }
        
        sum += numbers[idx];
        dfs(numbers,target,idx+1,sum);
        sum -= 2*numbers[idx];
        dfs(numbers,target,idx+1,sum);      
    }
}



/*
class Solution {
    static int answer = 0;
    public int solution(int[] numbers, int target) {
        
        dfs(numbers, target, 0);
        
        return answer;
    }
    
    public void dfs(int[] numbers, int target, int index) {
        int sum = 0;
        if(index == numbers.length) {
            
            for(int num: numbers) 
                sum += num;
            
            if(target == sum)
                answer++;
            
            return;
        }
        
        numbers[index] *= 1;
        dfs(numbers, target, index+1);

        numbers[index] *= -1;
        dfs(numbers, target, index+1);
        
    }
}
*/