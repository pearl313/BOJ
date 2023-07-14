import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int i=1; i < t + 1; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int[][] num = {{}, {}, {2, 4, 8, 6}, {3, 9, 7, 1}, {4, 6}, {5},
                    {6}, {7, 9, 3, 1}, {8, 4, 2, 6}, {9, 1}, {10}};
            a = a % 10;
            b = b % 4;
            if (a == 1) {
                System.out.println(1);
            } else if (a == 0){
                System.out.println(10);
            } else if (a == 2 || a == 3 || a == 7 || a == 8){
                if (b == 0) {
                    System.out.println(num[a][3]);
                } else {
                    System.out.println(num[a][b - 1]);
                }
            } else if (a == 5 || a == 6 || a == 10) {
                System.out.println(num[a][0]);
            } else {
                b = b % 2;
                if (b == 0) {
                    System.out.println(num[a][1]);
                } else {
                    System.out.println(num[a][b - 1]);
                }
            }
        }
    }
}