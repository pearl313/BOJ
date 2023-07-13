import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while(true){
            int m = scanner.nextInt();
            int t = scanner.nextInt();
            if (m==0 && t ==0){
                System.exit(0);
            } else {
                System.out.println(m + t);
            }
        }
    }
}