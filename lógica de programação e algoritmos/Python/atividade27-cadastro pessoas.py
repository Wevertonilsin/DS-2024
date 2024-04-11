from click import clear

def adicionar_pessoa():
    nome = input('Digite o seu nome: ')
    email = input('Digite o seu email: ')

    with open('pessoa.txt', 'a') as arquivo:
        arquivo.write(f'{nome},{email}\n')

        print("pessoa cadastrada com sucesso!!!")


adicionar_pessoa()

def listar_pessoas():
    with open('pessoa.txt', 'r') as arquivo:
        print('Pessoas cadastradas:')
        for linha in arquivo:
            nome, email = linha.strip().split(',')
            print(f'Nome: {nome},Email: {email}')

#adicionar_pessoas()
listar_pessoas()
