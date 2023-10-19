import java.util.*;
import java.io.*;

public class Main {
    static int answer = 0;
    static int ans = 0;
    public static void cal(String[] arr, int hap) throws IOException {
        int total = 1;
        for (String i:arr) {
            total *= Integer.parseInt(i);
        }
        ans += total;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] blossom = br.readLine().split(" ");

        for (int a=1; a < n - 2; a++) {
            for (int b=a+1; b < n - 1; b++) {
                for (int c=b+1; c < n; c++) {
                    String[] arr1 = Arrays.copyOfRange(blossom, 0, a);
                    String[] arr2 = Arrays.copyOfRange(blossom, a, b);
                    String[] arr3 = Arrays.copyOfRange(blossom, b, c);
                    String[] arr4 = Arrays.copyOfRange(blossom, c, blossom.length);

                    ans = 0;
                    cal(arr1, ans);
                    cal(arr2, ans);
                    cal(arr3, ans);
                    cal(arr4, ans);
                    answer = Math.max(ans, answer);
                }
            }
        }
        System.out.println(answer);
    }
}
