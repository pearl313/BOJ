import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for (int i=1; i < n+1; i++){
            System.out.println(" ".repeat(n - i) + "*".repeat(2 * i - 1));
        }
    }
}