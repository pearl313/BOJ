import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
//        1. 가능한 세자리 수 다 찾아놓고
        ArrayList<String> candidate = new ArrayList<>();
        for (int i=111; i < 1000; i++) {
            if (Integer.toString(i).contains("0")) {
                continue;
            } else if (Integer.toString(i).charAt(0) == Integer.toString(i).charAt(1) || Integer.toString(i).charAt(0) == Integer.toString(i).charAt(2)
                    || Integer.toString(i).charAt(1) == Integer.toString(i).charAt(2)) {
                continue;
            }
            candidate.add(Integer.toString(i));
        }
//        2. 모든 후보 돌면서, 입력 받은 수랑 비교하기
        for (int i=0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            String num = input[0];
            int strike = Integer.parseInt(input[1]);
            int ball = Integer.parseInt(input[2]);
            ArrayList<String> ans = new ArrayList<>();
            for (int j=0; j < candidate.size(); j++) {
                int cnt_s = 0;
                int cnt_b = 0;
                for (int k=0; k < 3; k++) {
                    if (candidate.get(j).charAt(k) == num.charAt(k)) {
                        cnt_s += 1;
                    } else {
                        if (candidate.get(j).contains(String.valueOf(num.charAt(k)))) {
                            cnt_b += 1;
                        }
                    }
                }
                if (cnt_s == strike && cnt_b == ball) {
                    ans.add(candidate.get(j));
                }
            }
            candidate = ans;
        }
        System.out.println(candidate.size());

//        3. 그때마다 스트라이크 / 볼 구하고
//        4. 입력 받은 스트라이크 / 볼 값이랑 동일하면 정답 후보에 넣기
//        5. 정답 후보는 계속 갱신
    }
}