# -----------------------------------------------------------------
# MÉTODOS DA CLASSE TUPLA

# [].count
print('> [].count <'.center(50, '-'))

colors = ('vermelho', 'azul', 'verde', 'azul',)

print(colors.count('vermelho'))
print(colors.count('azul'))
print(colors.count('verde'))

# [].index -> primeira ocorrência do objeto
print()
print('> [].index <'.center(50, '-'))

print(f'Qual o índice da palavra (azul): {colors.index('azul')}')
print(f'Qual o índice da palavra (vermelho): {colors.index('vermelho')}')

# len -> tamanho da tupla
print()
print('> len <'.center(50, '-'))

print(f'Tupla: {colors}')
print(f'Tamanho da tupla: {len(colors)}')