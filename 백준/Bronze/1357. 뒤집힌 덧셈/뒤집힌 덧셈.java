import java.util.*;
import java.lang.StringBuffer;

public class Main {
    public static Integer change(String a) {
        StringBuffer reverse = new StringBuffer(a).reverse();
        return Integer.valueOf(String.valueOf(reverse));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        int y = scanner.nextInt();
        x = change(String.valueOf(x));
        y = change(String.valueOf(y));
        System.out.println(change(String.valueOf(x + y)));
    }
}