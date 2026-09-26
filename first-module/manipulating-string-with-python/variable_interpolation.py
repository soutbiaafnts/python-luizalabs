# -----------------------------------------------------------------
# INTERPOLAÇÃO DE VARIÁVEIS

# Em Python existem 3 formas de interpolar variáveis em strings:
# 1. % -> surgiu na criação da linguagem e atualmente não é mais recomendado seu uso
# 2. Método format
# 3. f strings

name = 'Bianca'
age = 23
occupation = 'Programadora'
language = 'Python'

# -----------------------------------------------------------------
# OLD STYLE -> %

print('> OLD STYLE - % <'.center(50, '-')) 
# %s -> strings, %d -> inteiros, %f -> pontos flutuantes
print('Nome: %s\nIdade: %d anos' %(name, age))

# -----------------------------------------------------------------
# MÉTODO FORMAT

print()
print('> MÉTODO FORMAT - CHAVES <'.center(50, '-'))
print('Nome: {}\nIdade: {} anos'.format(name, age))

print()

print('> MÉTODO FORMAT - CHAVES E ÍNDICE <'.center(50, '-'))
print('Nome: {0}\nIdade: {1} anos'.format(name, age))

print()

print('> MÉTODO FORMAT - NOMEANDO <'.center(50, '-'))
print('Nome: {name}\nIdade: {age} anos'.format(name=name, age=age))

# definindo um dicionário
data = {'name': 'Bianca', 'age': 23}

print()

print('> MÉTODO FORMAT - DICIONÁRIO <'.center(50, '-'))
print('Nome: {name}\nIdade: {age} anos'.format(**data))

# -----------------------------------------------------------------
# MÉTODO F STRING

print()

print('> MÉTODO F STRING <'.center(50, '-'))
print(f'Nome: {name}\nIdade: {age} anos')

# -----------------------------------------------------------------
# FORMATANDO
balance = 45.435

print()

print('> FORMATAÇÃO <'.center(50, '-'))
print(f'Nome: {name}\nIdade: {age} anos\nSaldo: {balance:.2f}')
