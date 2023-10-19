import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int c = Integer.parseInt(input[1]);
        int[] time = new int[n];
        for (int i=0; i < n; i++) {
            time[i] = Integer.parseInt(br.readLine());
        }

        int cnt = 0;
        for (int i=1; i < c + 1; i++) {
            boolean temp = false;
            for (int j:time) {
                if (i % j == 0) {
                    temp = true;
                }
            }
            if (temp) {
                cnt += 1;
            }
        }
        System.out.println(cnt);
    }
}