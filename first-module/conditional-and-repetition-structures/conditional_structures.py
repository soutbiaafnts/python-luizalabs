# A Estrutura Condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas

# -----------------------------------------------------------------
# ETAPA 1: if | if-else | elif

LEGAL_AGE = 18
SPECIAL_AGE = 17

print('IF (UM DESVIO)')
age = int(input('Informe sua idade: '))

if age >= LEGAL_AGE:
    print('Maior de idade, pode tirar a CNH')

if age < LEGAL_AGE:
    print('Ainda não pode tirar a CNH.')

# -----------------------------------------------------------------

print('\nIF/ELSE (DOIS DESVIOS)')

if age >= LEGAL_AGE:
    print('Maior de idade, pode tirar a CNH')
else:
    print('Ainda não pode tirar a CNH.')

# -----------------------------------------------------------------

# Não existe um limite de elif, porém evite criar grandes estruturas assim. Elas aumentam a complexidade do código
print('\nIF/ELIF/ELSE (MAIS DE DOIS DESVIOS)')

if age >= LEGAL_AGE:
    print('Maior de idade, pode tirar a CNH')
elif age == SPECIAL_AGE:
    print('Pode fazer as aulas teóricas, mas não fazer as aulas práticas.')
else:
    print('Ainda não pode tirar a CNH.')
