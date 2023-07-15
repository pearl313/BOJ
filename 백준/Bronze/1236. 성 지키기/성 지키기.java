import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        String[][] arr = new String[n][m];
        int row = 0;
        for (int i=0; i < n; i++) {
            arr[i] = scanner.next().split("");
            if (Arrays.asList(arr[i]).contains("X")) {
                continue;
            }
            row += 1;
        }
        int col = 0;
        for (int i=0; i < m; i++) {
            boolean ok = false;
            for (int j=0; j < n; j++) {
                if (arr[j][i].equals("X")) {
                    ok = true;
                }
            }
            if (ok) {
                continue;
            }
            col += 1;
        }
        System.out.print(Math.max(row, col));
    }
}
