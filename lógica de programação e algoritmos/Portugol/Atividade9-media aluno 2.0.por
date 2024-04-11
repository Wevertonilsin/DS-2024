programa
{
	
	funcao inicio()
	{
		inteiro valor
	     real numero_1 , numero_2 , numero_3 , soma , resultado

	      
	     escreva("digite a primeira nota do aluno: ")
	     leia(numero_1)

	     escreva("digite a segunda nota do aluno: ")
	     leia(numero_2)

	     escreva("digite a terceira nota do aluno: ")
	     leia(numero_3)

	     soma= numero_1 + numero_2 + numero_3

	     resultado= soma / 3 

	     escreva("a soma das notas é:", soma ," a media é:", resultado)

	     se(resultado >=7){
	     	escreva("parabens, aprovado!")
	     }
	     senao se(resultado >=3 ){
	     	escreva ("\nvocê está de recuperação!!")
	     }
	     se( resultado <= 3 ) {
	     	escreva ("\naluno foi reprovado.")
	     }
	     
	   }
	}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 737; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */