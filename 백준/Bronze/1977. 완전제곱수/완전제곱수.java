import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());

        int total = 0;
        int min_v = 0;
        for (int i=m; i < n + 1; i++) {
            for (int k=1; k < (Math.sqrt(i) + 1); k++) {
                if (k * k == i) {
                    total += i;
                    if (min_v == 0) {
                        min_v = i;
                    }
                }
            }
        }
        if (total == 0 && min_v == 0) {
            System.out.println(-1);
        } else {
            System.out.println(total);
            System.out.println(min_v);
        }
    }
}