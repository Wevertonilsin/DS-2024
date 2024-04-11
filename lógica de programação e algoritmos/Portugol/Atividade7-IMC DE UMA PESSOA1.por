programa
{
	
	funcao inicio()
	{
		real altura
		real peso
		real IMC

		escreva("digite sua altura:") 
		leia(altura)

		escreva("digite seu peso")
		leia(peso)

		IMC= peso/(altura*altura)
		
		escreva("seu IMC é : ", IMC)
		escreva("\naltura unfirmada: ", altura)
		escreva("\npeso informado: ", peso)
		
	}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 317; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */