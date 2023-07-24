import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        List<Integer> list = new ArrayList<>();
        for (int i=0; i < num; i++) {
            list.add(scanner.nextInt());
        }
        int m = Collections.max(list);
        float ans = 0;
        for (int i=0; i < num; i++) {
            float score = list.get(i);
            ans += score/m*100;
        }
        System.out.println(ans/num);
    }
}