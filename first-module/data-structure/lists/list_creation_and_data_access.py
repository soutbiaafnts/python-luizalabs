# -----------------------------------------------------------------
# LISTAS
# Elas podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas utilizando o construtor 
# list, a função range ou colocando valores separados por vírgula dentro de colchetes. Listas são objetos mutáveis,
# portanto podemos alterar seus valores após a criação.

print('> CRIAÇÃO <'.center(50, '-'))

fruits = ['laranja', 'maçã', 'uva']

print(fruits)

fruits = [] # é possível declarar uma lista vazia

print(fruits)

letters = list('python') # cada letra é um elemento

print(letters)

numbers = list(range(10)) # cada número é um elemento

print(numbers)

car = ['Ferrari', 'F8', 4200000, 2020, 2900, 'São Paulo', True]

print(car)

# -----------------------------------------------------------------
# ACESSO DIRETO
# A lista é uma sequência, portanto podemos acessar seus dados utilizando índices. Contamos o índice de determinada
# sequência a partir do zero.
print()

print('> ACESSO DIRETO <'.center(50, '-'))

print(numbers[5])

# -----------------------------------------------------------------
# ÍNDICES NEGATIVOS
# Sequências suportam indexação negativa. A contagem começa em -1.
print()

print('> ÍNDICES NEGATIVOS <'.center(50, '-'))

print(numbers[-1]) # último item da lista

# -----------------------------------------------------------------
# LISTAS ANINHADAS
# As listas podem armazenar todos os tipos de objetos Python, portanto podemos ter listas que armazenam outras listas.
# Com isso podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna.

print()

print('> LISTAS ANINHADAS <'.center(50, '-'))

matrix = [ 
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c'],
]

print(matrix[0])
print(matrix[0][0])
print(matrix[0][-1])
print(matrix[-1][-1])

# -----------------------------------------------------------------
# FATIAMENTO
# Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta 
# passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve 
# 'pular' no acesso.

print()

print('> FATIAMENTO <'.center(50, '-'))

list = ['p', 'y', 't', 'h', 'o', 'n']

print(list)
print(list[2:])
print(list[:2])
print(list[1:3])
print(list[0:3:2])
print(list[::])
print(list[::-1])

# -----------------------------------------------------------------
# ITERAR LISTAS
# A forma mais comum para percorrer os dados de uma lista é utilizando o comando for

print()

print('> ITERAR LISTAS <'.center(50, '-'))

cars = ['gol', 'celta', 'palio']

for car in cars:
    print(car)

# -----------------------------------------------------------------
# FUNÇÃO ENUMERATE
# Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso podemos usar a função enumerate.

print()

print('> FUNÇÃO ENUMERATE <'.center(50, '-'))

for index, car in enumerate(cars):
    print(f'{index}: {car}')

# -----------------------------------------------------------------
# COMPREENSÃO DE LISTAS
# A compressão de lista oferece uma sintaxe mais curta quando você deseja: criar uma nova lista com base nos valores 
# de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista 
# existente

print()

print('> COMPREENSÃO DE LISTAS - FILTRO <'.center(50, '-'))

print('> Versão 01 (sem comprehension):')
numbers = [1, 30, 21, 2, 9, 65, 34]
even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(f'Números: {numbers}')
print(f'Números pares: {even_numbers}')
print(f'Números ímpares: {odd_numbers}')

print()

print('> Versão 02 (com comprehension):')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [retorno for iteração if condição]
even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 != 0]

print(f'Números: {numbers}')
print(f'Números pares: {even_numbers}')
print(f'Números ímpares: {odd_numbers}')

print()

print('> COMPREENSÃO DE LISTAS - MODIFICAÇÃO <'.center(50, '-'))

print('> Versão 01 (sem comprehension):')
numbers = [1, 30, 21, 2, 9, 65, 34]
square = []

for number in numbers:
    square.append(number ** 2)

print(f'Números: {numbers}')
print(f'Quadrado: {square}')

print()

print('> Versão 02 (com comprehension):')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = [number ** 2 for number in numbers]

print(f'Números: {numbers}')
print(f'Quadrado: {square}')
