import java.util.Scanner;

public class Main {

    public static int cal(String str) {
        int total = 1;
        for (int i=0; i < str.length(); i++) {
            total *= Integer.parseInt(String.valueOf(str.charAt(i)));
        }
        return total;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
	    String num = scanner.next();
        for (int i=1; i < num.length(); i++) {
            String one = num.substring(0, i);
            String two = num.substring(i, num.length());
            if (cal(one) == cal(two)) {
                System.out.println("YES");
                System.exit(0);
            }
        }
        System.out.println("NO");
    }
}