import java.util.Scanner;

public class Idade {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite sua idade:");
		int idade = entrada.nextInt();
		entrada.close();
		System.out.println(idade < 60 ? "Você é jovem!" : 
			"Você é idoso.");

	}

}
