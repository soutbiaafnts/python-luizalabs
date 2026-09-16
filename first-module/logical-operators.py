# Operadores Lógicos 
## São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Quando um operador lógico
## é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos, exemplo:
## op_comparacao + op_logico + op_comparacao... N...

print('Regras:')
print('True and True = True')
print('True and False = False')
print('False and True = False')
print('False and False = False')
print('True or True = True')
print('True or False = True')
print('False or True = True')
print('False or False = False')


# Operador AND (E)
balance = 1000
withdraw = 200
limit = 100

print('\nOperador AND:')
print(balance >= withdraw and withdraw <= limit) # True and False = False

# Operador OR (OU)
print('\nOperador OR:')
print(balance >= withdraw or withdraw <= limit) # True or False = True

# Operador NOT (NÃO)
print('\nOperador NOT:')
print(not balance >= withdraw) # not True = False
emergency_contacts = []
print(not 1000 > 1500) # not False = True
print(not emergency_contacts) # not False = True
print(not 'saque 1500;') # not True = False
print(not '') # not False = True

# Parênteses
## Podemos utilizar parênteses para definir a ordem de precedência dos operadores lógicos, exemplo
balance = 1000
withdraw = 250
limit = 200
special_account = True

print('\nParênteses:')
expression_1 = balance >= withdraw and withdraw <= limit or special_account and balance >= withdraw
print(expression_1) # True and False or True and True = False or True = True

expression_2 = (balance >= withdraw and withdraw <= limit) or (special_account and balance >= withdraw)
print(expression_2) # (True and False) or (True and True) = True

normal_account_with_enough_balance = (balance >= withdraw and withdraw <= limit)
special_account_with_enough_balance = (special_account and balance >= withdraw)
expression_3 = normal_account_with_enough_balance or special_account_with_enough_balance
print(expression_3) # False or True = True