n1 = float(input('Digite a sua altura em m: '))
n2 = float(input('Digite o seu peso em kg: '))
imc = n2 / (n1 * n1)
print(f'Seu IMC é: {imc}')
if imc > 30.0:
    print('Cuidado com a sua saúde!')
elif imc < 18.4:
    print('Cuidado com a sua saúde!')
else:
    print('Tudo ok!')
