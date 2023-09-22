'''
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''

numero_str = input('vou dobrar o número que vc digitar: ')


try:
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float *2:.2f}')
except:
    print(f'Isso não é número')

'''
Em resumo, o programa será lido da esquerda para a direita, de cima para baixo sempre.
o módulo try / except funciona da seguinte forma:
tudo que está dentro do try é executado na ordem padrão do python.
quando alguma excessão acontecer, o python pulará automaticamente para o except
'''