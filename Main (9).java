import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int saldo = 1000; 


        System.out.print("Ingresa el monto a retirar: ");
        int monto = sc.nextInt();


        if (monto <= saldo && monto > 0) {
            System.out.println("Operación exitosa . Retiraste $" + monto);
            saldo -= monto;
            System.out.println("Tu nuevo saldo es: $" + saldo);
        } else {
            System.out.println("Operación denegada . Fondos insuficientes o monto inválido.");
        }

        sc.close();
    }
}
