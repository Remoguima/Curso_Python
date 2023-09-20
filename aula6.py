# Conversão ou coerção de tipos
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool

print('1',type('1')) # retorno será str

print(int('1'), type(int('1'))) # retorno sera int

# como pythopn é uma linguagem de tipagem forte, as conversões implicitas não funcionam.
# logo o operador + pode ser usado para somar ou concatenar valores caso o tipo de dado não seja compativel.

print('a' + 1) # Nesse caso ele retorna um erro pois não pode concatenar string com int

print('a' + str(1)) # nesse caso, como o 1 está sendo convertido para str, o python concatena e o resultado será "a1"
