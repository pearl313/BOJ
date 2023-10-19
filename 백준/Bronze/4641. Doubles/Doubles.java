import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String[] arr = br.readLine().split(" ");
            if (arr.length == 1 && Integer.parseInt(arr[0]) == -1) {
                break;
            }
            int cnt = 0;
            for (int i=0; i < arr.length - 1; i++) {
                for (int j=0; j < arr.length - 1; j++) {
                    if (Integer.parseInt(arr[i]) * 2 == Integer.parseInt(arr[j])) {
                        cnt += 1;
                    }
                }
            }
            System.out.println(cnt);
        }
    }
}