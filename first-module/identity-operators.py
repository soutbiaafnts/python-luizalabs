# Operadores de Identidade:
# são operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição de memória, ou seja, se são o mesmo objeto.

course = 'Curso de Python'
course_name = course
balance, limit = 200, 200
print('Variáveis em primeiro estado:')
print('Curso:', course)
print('Nome do curso:', course_name)
print('Saldo:', balance)
print('Limite:', limit, '\n')

print('Operador IS:')
print('Curso é nome do curso?', course is course_name) # True

print('Operador IS NOT:')
print('Curso não é nome do curso?', course is not course_name) # False

print('Operador IS:')
print('Saldo é limite?', balance is limit) # True

balance, limit = 1000, 500
print('Operador IS:')
print('Saldo é limite?', balance is limit) # False