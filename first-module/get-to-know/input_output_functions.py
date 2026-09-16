name = input('Informe seu nome: ')
last_name = input('Informe seu sobrenome: ')
print(name, last_name) # ao usar o print() com mais de um argumento, o padrão é separar os argumentos com espaço.
print(name, last_name, end='...\n') # o end() é usado para definir o que será exibido no final da linha.
print(name, last_name, sep='#') # o sep() é usado para definir o que será exibido entre os argumentos, por padrão é um espaço.