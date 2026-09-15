# Variables
age, name = (23, 'Bianca')
print(f'Meu nome é {name} e eu tenho {age} anos.')

age, name = (61, 'Cassia')
print(f'Meu nome é {name} e eu tenho {age} anos.')

# Em Python não existe constante, mas por convenção, variáveis que não devem ser alteradas são escritas em maiúsculas.
ABS_PATH = '/home/user/documents'
DEBUG_MODE = True
STATES = ['SP', 'RJ', 'MG', 'ES']
AMOUNT = 1000.00

print(f'ABS_PATH: {ABS_PATH}', f'DEBUG_MODE: {DEBUG_MODE}', f'STATES: {STATES}', f'AMOUNT: {AMOUNT}', sep='\n')

# Boas práticas no Python
## O padrão de nomes deve ser snake_case para variáveis e funções, PascalCase para classes e UPPER_CASE para constantes.
## Escolher nomes sugestivos e significativos, evitando abreviações e siglas.