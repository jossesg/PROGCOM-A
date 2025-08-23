import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.print("Ingresa la calificación (0-100): ");
        int calificacion = entrada.nextInt();

        if (calificacion >= 60) {
            System.out.println("Aprobado ");
        } else {
            System.out.println("Reprobado ");
        }

        entrada.close();
    }
}
