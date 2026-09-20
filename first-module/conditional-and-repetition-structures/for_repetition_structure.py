# As estruturas de repetição são utilizadas para repetir um trecho de código por um determinado número de vezes. 
# Esse número pode ser conhecido previamente ou determinado através de ua expressão lógica.

# -----------------------------------------------------------------
# FOR: é usado para percorrer um objeto iterável. Faz sentido usar 'for' quando sabemos o número exato de vezes que
# nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.

VOWELS = 'AEIOU'

print('FOR: utilizando iterável')

text = input('Informe um texto: ')
for letter in text:
    if letter.upper() in VOWELS:
        print(letter, end='')

print() # adiciona uma quebra de linha

# -----------------------------------------------------------------
# FOR/ELSE
print('\nFOR/ELSE: utilizando iterável')

text = ''

for letter in text:
    if letter.upper() in VOWELS:
        print(letter, end='')
else: # não é muito comum de usar
    print()
    print('Executa no final do laço.')

# -----------------------------------------------------------------
# RANGE: é uma função built-in do Python, ela é usada para produzir uma sequência de número inteiros a partir de um 
# início (inclusivo) para um fim (exclusivo), Se usarmos range(i, j) será produzido: i, i+1, i+2, i+3, ..., j-1. 
# Ela recebe 3 argumentos: stop_value (obrigatório), start_value (opcional) e step_value (opcional).

# range(stop_value) -> range object (é o padrão)
# range(start_value, stop_value) -> range object (gera a sequência com base nos valores de início e término)
# range(start_value, stop_value, step_value) -> range object (gera uma sequência incrementando o valor de início 
# usando o valor do passo até atingir o valor de término)

# print(range(4), '') # não exibe os números
# print(list(range(4))) # exibe os números
# print(list(range(0, 10))) # exibe os números

print('\nFOR: utilizando função built-in range')
for number in range(0, 11):
    print(number, end=' ')

print('\nTabuada do 5:')
for number in range(0, 51, 5): # step: 5 em 5 
    print(number, end=' ')

