import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int jimin = Integer.parseInt(input[1]);
        int hansoo = Integer.parseInt(input[2]);
        
        int cnt = 0;
        while (jimin != hansoo) {
            jimin -= jimin / 2;
            hansoo -= hansoo / 2;
            cnt += 1;
        }
        System.out.println(cnt);
    }
}