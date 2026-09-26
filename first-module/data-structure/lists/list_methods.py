# -----------------------------------------------------------------
# MÉTODOS DA CLASSE LISTA

# [].append -> adiciona de um em um, no fim da lista
print('> [].append <'.center(50, '-'))

list = []
print(list)

list.append(1)
print(list)

list.append('Python')
print(list)

list.append([40, 30, 20])
print(list)

# [].clear
print()
print('> [].clear <'.center(50, '-'))

print(list)
list.clear()
print(list)

# [].copy
print()
print('> [].copy <'.center(50, '-'))

list.append(1)
list.append('Python')
list.append([40, 30, 20])

list_copy = list.copy()
print(f'Lista: {list}\nCópia: {list_copy}')
print(f'Id da lista: {id(list)}\nId da cópia: {id(list_copy)}')

# [].count
print()
print('> [].count <'.center(50, '-'))

colors = ['Vermelho', 'Azul', 'Verde', 'Azul']
print(colors)
print(f'Quanta vezes (Vermelho): {colors.count('Vermelho')}')
print(f'Quanta vezes (Azul): {colors.count('Azul')}')
print(f'Quanta vezes (Verde): {colors.count('Verde')}')

# [].extend -> adiciona vários de uma vez (não elimina valores duplicados)
print()
print('> [].extend <'.center(50, '-'))

languages = ['python', 'js', 'c']
print(languages)

languages.extend(['java', 'csharp'])
print(languages)

# [].index -> primeira ocorrência do objeto
print()
print('> [].index <'.center(50, '-'))

print(f'Qual o índice da palavra (java): {languages.index('java')}')
print(f'Qual o índice da palavra (python): {languages.index('python')}')

# [].pop -> remove o último elemento da lista (as listas, por padrão, são organizadas em pilha)
print()
print('> [].pop <'.center(50, '-'))

print(languages)
languages.pop()
print(languages)
languages.pop()
print(languages)
languages.pop()
print(languages)
languages.pop(0) # define o índice que será removido
print(languages)

# [].remove -> remove a primeira ocorrência do objeto passado como parâmetro
print()
print('> [].remove <'.center(50, '-'))

languages = ['python', 'js', 'c']
languages.extend(['java', 'csharp'])

print(languages)
languages.remove('c')
print(languages)

# [].reverse -> transpõe a lista
print()
print('> [].reverse <'.center(50, '-'))

languages.append('c')
print(languages)
languages.reverse()
print(languages)