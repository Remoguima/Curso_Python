'''
fatiamento de strings com len
012345678
Olá mundo
-987654321
Fatiamento [inicio:fim:passo] [::]
obs. a função retorna a qtd de caracter da str
'''


variavel = '0123456789'
print(variavel[0:5])  # inicia no 0 e vai até o 5

print(variavel[0:5:2])  # inicia no 0 e vai até o 5 pulando de 2 em 2

print(variavel[::-1])  # inicia no ultimo caractere e vai até o primeiro