import java.util.*;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> doble = new ArrayList<>();
        for (int i = 1; i <= 5; i++) {
            doble.add(i * 2);
        }
        System.out.println("doble de cada numero del 1 al 5:");
        System.out.println(doble);
    }
}