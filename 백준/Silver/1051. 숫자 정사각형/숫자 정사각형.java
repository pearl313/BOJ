import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
        for (int i=0; i < n; i++) {
            String[] input_n = br.readLine().split("");
            ArrayList<Integer> temp = new ArrayList<>();
            for (int j=0; j < input_n.length; j++) {
                temp.add(Integer.parseInt(input_n[j]));
            }
            arr.add(temp);
        }

        int max_v = 0;
        for (int i=0; i < n; i++) {
            for (int j=0; j < m; j++) {
                for (int k=0; k < Math.min(n, m); k++) {
                    if (i + k < n && j + k < m) {
                        if ((arr.get(i).get(j) == arr.get(i).get(j + k)) &&
                                (arr.get(i).get(j + k) == arr.get(i + k).get(j)) &&
                                (arr.get(i + k).get(j) == arr.get(i + k).get(j + k)) &&
                                (arr.get(i).get(j) == arr.get(i + k).get(j + k))) {
                            int temp = (k + 1) * (k + 1);
                            if (max_v < temp) {
                                max_v = temp;
                            }
                        }
                    }
                }
            }
        }
        System.out.println(max_v);
    }
}