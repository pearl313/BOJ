import java.util.*;
    
class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        
        int start = 0;
        
        while (true) {
            int[] arr = new int[num];
            int temp = start;
            for (int i=0; i < num; i++) {
                arr[i] = temp;
                temp += 1;
            }
            if (Arrays.stream(arr).sum() == total) {
                for (int i=0; i < num; i++) {
                    answer[i] = arr[i];
                }
                break;
            } else if (Arrays.stream(arr).sum() < total) {
                start += 1;
            } else {
                start -= 1;
            }
        }
        
        return answer;
    }
}