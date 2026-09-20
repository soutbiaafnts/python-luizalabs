# A Estrutura Condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas

# -----------------------------------------------------------------
# ETAPA 3: if ternário - Permite escrever uma condição em uma única linha. Ele é composto por três partes, a primeira
# parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o
# retorno caso a expressão não seja atendida (seja falsa)

balance = 2000.0
withdraw = 500.0

status = 'Sucesso' if balance >= withdraw else 'Falha'

print(f'{status} ao realizar o saque!')