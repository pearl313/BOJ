import java.io.*;

public class Main {

    static boolean check(int t) {
        int tmp = t;
        for (int i=0; i < 3; i++) {
            if (tmp % 10 == 0) {
                return false;
            }
            tmp = tmp / 10 + 1000 * (tmp % 10);
            if (tmp < t) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        int card = 0;
        for (int i=0; i < 4; i++) {
            card += Integer.parseInt(input[i]) * (Math.pow(10, 4 - (i + 1)));
        }
        int temp = card;
        for (int i=0; i < 3; i++) {
            temp = temp / 10 + 1000 * (temp % 10);
            card = Math.min(card, temp);
        }

        int ans = 0;
        for (int t=1111; t < card; t++) {
            if (check(t)) {
                ans += 1;
            }
        }
        System.out.println(ans + 1);
    }
}