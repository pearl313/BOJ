import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        String[] arr = new String[n];
        for (int i=0; i < n; i++) {
            arr[i] = br.readLine();
        }

        String ans = "";
        int dist = 0;
        for (int i=0; i < m; i++) {
            int[] dna = new int[4];
            Arrays.fill(dna, 0);
            for (int j=0; j < n; j++) {
                if ((arr[j].charAt(i)) == 'A') {
                    dna[0] += 1;
                } else if ((arr[j].charAt(i)) == 'C') {
                    dna[1] += 1;
                } else if ((arr[j].charAt(i)) == 'G') {
                    dna[2] += 1;
                } else {
                    dna[3] += 1;
                }
            }
            int word = 0;
            int idx = 0;
            for (int k=0; k < 4; k++) {
                if (word < dna[k]) {
                    word = dna[k];
                    idx = k;
                }
            }
            if (idx == 0) {
                ans += "A";
            } else if (idx == 1) {
                ans += "C";
            } else if (idx == 2) {
                ans += "G";
            } else {
                ans += "T";
            }
            dist += n - word;
        }
        System.out.println(ans);
        System.out.println(dist);
    }
}