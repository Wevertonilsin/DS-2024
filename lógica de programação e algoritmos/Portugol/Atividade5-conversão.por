programa
{
	
	funcao inicio()
	{
		real moeda_r, moeda_d,resultado
		inteiro tipo_moeda
		
		escreva("qual a cotação do dólar? ")
		leia(moeda_d)

		escreva("escolha: \n")
		escreva("[1] - Conventer Dólar para Real \n")
		escreva("[2] - Converter Real para Dólar \n")

		escreva("Digite um numero para conversão")
		leia(tipo_moeda)

		se(tipo_moeda == 1){
			escreva("Qual o valor em Dólar a ser convertido para Real? ")
		}senao{
			escreva("Qual o valor em real a ser convertido para Dólar? ")
			leia(moeda_r)
			resultado = moeda_r / moeda_d
		}
		escreva ("O valor convertido é: $", resultado))
		
		
	
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 605; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */