n1 = int(input('Digite o número que você deseja descobrir a tabuada: '))
n2 = int(input('Digite por qual número você deseja começar: '))
n3 = int(input('Digite em qual número deseja parar: '))
for i in range (n2, n3+1):
    print(n1*i)