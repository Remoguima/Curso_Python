# Utilizando f-strings para formatação de texto.

# para utilizar a f-string, utilizar a seguinte estrutura:
# f'sua string aqui'
# dentro de uma f-string é possivel utilizar variáveis de forma mais simples, colocando a variavel entre chaves { }

nome = 'Matheus'
altura = 1.75
peso = 102
imc = peso / altura**2


# print(nome , 'tem' ,altura,' de altura, pesa ',peso,' quilos e seu imc é:',imc)
texto = f'{nome} tem {altura:.2f} de altura, pesa {peso} quilos e seu imc é: {imc:.2f}'  
print(texto)