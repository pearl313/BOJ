import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();
        ArrayList<String> ans = new ArrayList<>();
        for (int i=0; i < word.length() - 2; i++) {
            for (int j=i + 1; j < word.length() - 1; j++) {
                for (int k=j + 1; k < word.length(); k++) {
                    String first = word.substring(0, j);
                    String second = word.substring(j, k);
                    String third = word.substring(k);

                    StringBuffer sb_1 = new StringBuffer(first);
                    String rev_first = sb_1.reverse().toString();

                    StringBuffer sb_2 = new StringBuffer(second);
                    String rev_second = sb_2.reverse().toString();

                    StringBuffer sb_3 = new StringBuffer(third);
                    String rev_third = sb_3.reverse().toString();

                    ans.add(rev_first + rev_second + rev_third);
                }
            }
        }
        Collections.sort(ans);
        System.out.println(ans.get(0));
    }
}