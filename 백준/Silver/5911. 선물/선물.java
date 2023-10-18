import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        long b = scanner.nextInt();

        long[][] present = new long[n][2];

        for (int i = 0; i < n; i++) {
            long p = scanner.nextInt();
            long s = scanner.nextInt();
            present[i][0] = p;
            present[i][1] = s;
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            long[] data = new long[n];
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    data[j] = present[j][0] / 2 + present[j][1];
                } else {
                    data[j] = present[j][0] + present[j][1];
                }
            }

            long total = 0;
            int cnt = 0;
            Arrays.sort(data);

            for (int j=0; j < n; j++) {
                total += data[j];
                if (total > b) {
                    break;
                }
                cnt += 1;
            }
            ans = Math.max(ans, cnt);
        }

        System.out.println(ans);

    }
}