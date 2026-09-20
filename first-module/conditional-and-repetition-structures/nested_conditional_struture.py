# A Estrutura Condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas

# -----------------------------------------------------------------
# ETAPA 2: if aninhado - Podemos criar estruturas condicionas aninhadas, para isso basta adicionar estruturas
# if/elif/else dentro do bloco de código de estruturas if/elif/else.

normal_account = False
university_account = False
special_account = True

balance = 2000.0
withdraw = 1500.0
special_check = 450.0

if normal_account:
    if balance >= withdraw:
        print('Saque realizado com sucesso!')
    elif withdraw <= (balance + special_check):
        print('Saque realizado com uso do cheque especial!')
    else:
        print('Não foi possível realizar o saque!')
elif university_account:
    if balance >= withdraw:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente!')
elif special_account:
    print('Conta especial selecionada!')
else:
    print('Não foi possível reconhecer o seu tipo de conta, entre em contato com o seu gerente!')