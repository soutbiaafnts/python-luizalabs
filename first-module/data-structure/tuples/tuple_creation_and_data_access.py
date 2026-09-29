# -----------------------------------------------------------------
# TUPLAS
# Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas são imutáveis 
# enquanto listas são mutáveis. Podemos criar tuplas através da classe tuple, ou colocando valores separados por vírgula
# dentro de parenteses.

print('> Tuplas <'.center(50, '-'))

# como boa prática colocamos uma vírgula no fim para indicar que é um tupla e não precedência
fruits = ("laranja", "pera", "uva",)
letters = tuple("python")
numbers = tuple([1,2,3,4])
country = ("Brasil",)

print(fruits[-1])

# -----------------------------------------------------------------
# TUPLAS ANINHADAS
# Tuplas podem armazenar todos os tipos de objetos em Python, portanto podemos ter tuplas que armazenam outras tuplas.
# Com isso podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna.
print()

print('> Tuplas aninhadas <'.center(50, '-'))

matrix = (
    (1, 'a', 2),
    ('b', 3, 4),
    (6, 5, 'c'),
)

print(matrix[0])
print(matrix[0][0])
print(matrix[0][-1])
print(matrix[-1][-1])

# -----------------------------------------------------------------
# FATIAMENTO
# Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passar
# o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursos deve "pular" no 
# acesso.

print()

print('> Fatiamento <'.center(50, '-'))

tuple = ('p', 'y', 't', 'h', 'o', 'n',)
print(tuple[2:])
print(tuple[:2])
print(tuple[1:3])
print(tuple[0:3:2])
print(tuple[::])
print(tuple[::-1])

# -----------------------------------------------------------------
# ITERAR TUPLAS
# A forma mais comum para percorrer os dados de uma tupla é utilizando o comando for

print()

print('> ITERAR TUPLAS <'.center(50, '-'))

cars = ('gol', 'celta', 'palio',)

for car in cars:
    print(car)

# -----------------------------------------------------------------
# FUNÇÃO ENUMERATE
# Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso podemos usar a função enumerate.

print()

print('> FUNÇÃO ENUMERATE <'.center(50, '-'))

for index, car in enumerate(cars):
    print(f'{index}: {car}')