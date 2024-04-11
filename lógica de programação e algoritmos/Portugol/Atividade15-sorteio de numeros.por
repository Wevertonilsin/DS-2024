programa{
	inclua biblioteca Util --> u
	funcao inicio(){
		logico condicao
		inteiro numero
		condicao = verdadeiro

		enquanto(condicao){
			numero = u.sorteia(1,100)
			escreva(numero, "\n")
			se(numero == 1 ){
				condicao = falso}
			}
		
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 215; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */