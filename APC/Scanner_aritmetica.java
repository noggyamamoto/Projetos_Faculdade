import java.util.Scanner; // permite utilizar o scanner
public class Scanner_aritmetica {

	public static void main(String[] args) {
		Scanner entrada_usuario = new Scanner(System.in); /* *scanner é
		um objeto e precisa de uma variavel que armazene 
		a entrada do usuário*; *entrada_usuário armazena a entrada*; 
		*system.in permite a entrada e armazena
		na variável*; 
		*/
		System.out.println("Informe o valor de a:");
		double valorA = entrada_usuario.nextDouble();/*
		next define o tipo da variável*/
		System.out.println("Informe o valor de b:");
		double valorB = entrada_usuario.nextDouble();
		System.out.println("Informe o valor de c:");
		double valorC = entrada_usuario.nextDouble();
		System.out.println("Informe o valor de d");
		double valorD = entrada_usuario.nextDouble();
		entrada_usuario.close();
		double expressao = (valorA + valorB) * valorC /(valorD - 3);
		System.out.println("O resultado é: " + expressao);
	}

}
