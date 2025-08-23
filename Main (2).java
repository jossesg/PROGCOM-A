import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.print("Ingresa el primer número: ");
        int num1 = entrada.nextInt();

        System.out.print("Ingresa el segundo número: ");
        int num2 = entrada.nextInt();

        if (num1 > num2) {
            System.out.println("El mayor es: " + num1);
        } else if (num2 > num1) {
            System.out.println("El mayor es: " + num2);
        } else {
            System.out.println("Ambos números son iguales.");
        }

        entrada.close();
    }
}