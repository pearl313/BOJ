import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t;
        t = scanner.nextInt();
        for (int i=1; i < t + 1; i++){
            String word = scanner.next();
            System.out.println(String.valueOf(word.charAt(0)) + String.valueOf(word.charAt(word.length()-1)));
        }
    }
}