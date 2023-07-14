import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);
        String first = scanner.next();
        String second = scanner.next();
        String third = scanner.next();

        String[] color = {"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};
        System.out.println(Integer.parseInt(String.valueOf(Arrays.asList(color).indexOf(first)) + String.valueOf(Arrays.asList(color).indexOf(second))) * Math.round(Math.pow(10, Arrays.asList(color).indexOf(third))));
    }
}