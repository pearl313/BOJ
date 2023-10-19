import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();
        for (int i=1; i < word.length(); i++) {
            String first = word.substring(0, i);
            String second = word.substring(i);
            
            int total1 = 1;
            for (int j=0; j < first.length(); j++) {
                total1 *= Integer.parseInt(String.valueOf(first.charAt(j)));
            }

            int total2 = 1;
            for (int j=0; j < second.length(); j++) {
                total2 *= Integer.parseInt(String.valueOf(second.charAt(j)));
            }
            if (total1 == total2) {
                System.out.println("YES");
                System.exit(0);
            }
        }
        System.out.println("NO");
    }
}