# Operadores de Associação:
# são operadores utilizados para verificar se um valor está presente em uma sequência (como listas, tuplas, dicionários, conjuntos ou strings).

course = 'Curso de Python'
fruits = ['laranja', 'uva', 'limão']
withdrawals = [1500, 100]

print('Variáveis em primeiro estado:')
print('Curso:', course)
print('Frutas:', fruits)
print('Saques:', withdrawals, '\n')

print('Operador IN:')
print('Python está no curso?', 'Python' in course) # True
print('Maçã não está em frutas?', 'maçã' not in fruits) # True
print('200 está em saques?', 200 in withdrawals) # False