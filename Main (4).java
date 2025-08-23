import java.io.*;
import java.util.Scanner;


public class Main {

    public static void main(String[] args) {

        double numero = 10; 


        if (numero > 0) {
            System.out.println("El número " + numero + " es positivo.");
        } else if (numero == 0) {
            System.out.println("El número es cero, no es positivo ni negativo.");
        } else {
            System.out.println("El número " + numero + " no es positivo.");
        }
    }
}
