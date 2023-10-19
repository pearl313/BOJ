import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayList<String[]> input = new ArrayList<>();
        for (int i=0; i < n; i++) {
            input.add(br.readLine().split(" "));
        }

        int[] rank = new int[n];
        Arrays.fill(rank, 0);
        for (int i=0; i < n; i++) {
            int num = 1;
            for (int j=0; j < n; j++) {
                if (Integer.parseInt(input.get(i)[0]) < Integer.parseInt(input.get(j)[0])
                && Integer.parseInt(input.get(i)[1]) < Integer.parseInt(input.get(j)[1])) {
                    num += 1;
                }
            }
            rank[i] = num;
        }
        String ans = "";
        for (int i:rank) {
            ans += Integer.toString(i);
            ans += " ";
        }
        System.out.println(ans.substring(0, ans.length() - 1));
    }
}