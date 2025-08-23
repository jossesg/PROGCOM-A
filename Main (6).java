import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);


        System.out.print("Ingresa una contraseña: ");
        String password = sc.nextLine();

        boolean longitud = password.length() > 8;
        boolean tieneNumero = false;
        boolean tieneMayuscula = false;


        for (int i = 0; i < password.length(); i++) {
            char c = password.charAt(i);
            if (Character.isDigit(c)) {
                tieneNumero = true;
            }
            if (Character.isUpperCase(c)) {
                tieneMayuscula = true;
            }
        }


        if (longitud && tieneNumero && tieneMayuscula) {
            System.out.println("La contraseña es válida ✅");
        } else {
            System.out.println("La contraseña no cumple con los requisitos ");
        }

        sc.close();
    }
}
