'''
Formatação basica de strings
s - string
d e i - int
f - float
.<numero de casas decimais>f
x e X = hexadecimal
(> ou < ou ^)(quantidade)(caractere de preenchimento)
> - esquerda
< - direita
sinal - + ou -
ex.: 0>-100,.1f
conversion flags - !r !s !a
'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >20}')
print(f'{variavel: >20}.')
print(f'{variavel: ^20}.')
print(f'{1000.1583904927343928}')
print(f'{1000.1583904927343928:.1f}')
print(f'{1234:0=+80,.1f}')