"""
from click import clear

letra = 's'

nome = []
valor = []
descricao = []
quantidade = []


while letra == 's':
    clear()
    nome = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: '))
    descricao = input('Digite a descrição do produto: ')
    quantidade = int(input('Digite a quantidade: '))

    nome.append(nome)
    valor.append(valor)
    descricao.append(descricao)
    quantidade.append(quantidade)

    letra = input('Deseja continuar? [s/n]')

clear()
opcao = input('Deseja exibir os produtos [sim/nao]')
if opcao == 'sim':
    print('nome do produto  \t valor do produto \t quantidade  \t descricao do produto ' )
    for i in range(0, len(nome)):
        print(f'{nome[i]} \t\t {valor[i]} \t\t\t {quantidade[i]} \t\t {descricao[i]}')

opcao = input('Deseja deletar os produtos [sim/nao]')
if opcao == 'sim':
    opcao = int(input('Qual registro deseja deletar?'))
    nome.pop(opcao)
    valor.pop(opcao)
    descricao.pop(opcao)
    quantidade.pop(opcao)
"""

from click import clear

letra = 's'

nome = []
valor = []
descricao = []
quantidade = []
adicionar_pessoa = []

while letra == 's':
    clear()
    nome = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: '))
    descricao = input('Digite a descrição do produto: ')
    quantidade = int(input('Digite a quantidade: '))

    nome.append(nome)
    valor.append(valor)
    descricao.append(descricao)
    quantidade.append(quantidade)

    letra = input('Deseja continuar? [s/n]')

clear()
opcao = input('Deseja exibir os produtos [sim/nao]')
if opcao == 'sim':
    print('nome do produto  \t valor do produto \t quantidade  \t descricao do produto ' )
    for i in range(0, len(nome)):
        print(f'{nome[i]} \t\t {valor[i]} \t\t\t {quantidade[i]} \t\t {descricao[i]}')

opcao = input('Deseja deletar os produtos [sim/nao]')
if opcao == 'sim':
    opcao = int(input('Qual registro deseja deletar?'))
    nome.pop(opcao)
    valor.pop(opcao)
    descricao.pop(opcao)
    quantidade.pop(opcao)

