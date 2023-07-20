import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        List<Integer> list = new ArrayList<>();
        for (int i=1; i<n + 1; i++) {
            if (n % i != 0) {
                continue;
            }
            list.add(i);
        }
        if (k > list.size()) {
            System.out.println(0);
        } else {
            System.out.println(list.get(k-1));
        }
    }
}