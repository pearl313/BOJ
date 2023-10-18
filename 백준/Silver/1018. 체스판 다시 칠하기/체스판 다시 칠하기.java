import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        List<String> board = new ArrayList<String>();
        for (int i=0; i<n; i++){;
            board.add(br.readLine());
        }

        ArrayList<ArrayList<Boolean>> check = new ArrayList<>();

        for (int i=0; i < n; i++) {
            ArrayList<Boolean> check_i = new ArrayList<>();
            for (int j=0; j < m; j++){
                if (board.get(i).charAt(j) == 'W') {
                    check_i.add(true);
                } else {
                    check_i.add(false);
                }
            }
            check.add(check_i);
        }

        int min_v = 64;
        for (int i=0; i < n - 7; i++) {
            for (int j=0; j < m - 7; j++){
                int cnt = 0;
                boolean color = check.get(i).get(j);

                for (int a = 0; a < 8; a++) {
                    for (int b=0; b < 8; b++) {
                        if (check.get(i + a).get(j + b) != color) {
                            cnt += 1;
                        }
                        color = !color;
                    }
                    color = !color;
                }
                int[] val = {min_v, cnt, 64- cnt};
                Arrays.sort(val);
                min_v = val[0];

            }
        }
        System.out.println(min_v);
    }
}