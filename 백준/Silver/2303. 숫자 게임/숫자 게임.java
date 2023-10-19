import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static String[] card;
    static int winner = 0;
    static int max_v = 0;
    static int[] selected = new int[5];
    static boolean[] visited = new boolean[5];

    public static void recur(int cur, int who) {
        if (cur == 3) {
            int total = 0;
            for (int j:selected) {
                total += j;
            }
            total = total % 10;
            if (max_v <= total) {
                max_v = total;
                winner = who;
            }
            return;
        }
        for (int i=0; i < 5; i++) {
            if (!visited[i]) {
                selected[i] = Integer.parseInt(card[i]);
                visited[i] = true;
                recur(cur + 1, who);
                selected[i] = 0;
                visited[i] = false;
            }
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        for (int i=1; i < n + 1; i++) {
            card = br.readLine().split(" ");
            Arrays.fill(visited, false);
            Arrays.fill(selected, 0);
            recur(0, i);
        }
        System.out.println(winner);
    }
}