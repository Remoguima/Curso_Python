# Utilizando a função input para coletar dados do usuário

nome = input('Qual seu nome? ') #o programa só continua se o usuario apertar enter
print(f'O seu nome é {nome}')


numero1 = input('Digite um número: ')
numero2 = input('Digite outro número: ')

int_numero_1 = int(numero1)
int_numero_2 = int(numero2)

print(f'A soma é: {int_numero_1 + int_numero_2}')