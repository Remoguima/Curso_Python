# utilizando operadores de comparação, receba dois valores do usuario e retorne uma mensagem dizendo qual valor é maior


primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")


if primeiro_valor > segundo_valor:
    print(
        f'{primeiro_valor=} é maior '
        f'do que {segundo_valor=}'
    )
if primeiro_valor < segundo_valor:
        print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )
if primeiro_valor == segundo_valor:
    print(f'Os valores são iguais!')
