# As estruturas de repetição são utilizadas para repetir um trecho de código por um determinado número de vezes. 
# Esse número pode ser conhecido previamente ou determinado através de ua expressão lógica.

# -----------------------------------------------------------------
# WHILE: é usado para repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos o número 
# exato de vezes que nosso bloco de código deve ser executado.
print('\nWHILE')

option = -1
while option != 0:
    option = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n: '))

    if option == 1:
        print('Sacando...')
    elif option == 2:
        print('Exibindo extrato...')

# -----------------------------------------------------------------
# WHILE/ELSE
print('\nWHILE/ELSE')

option = -1
while option != 0:
    option = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n: '))

    if option == 1:
        print('Sacando...')
    elif option == 2:
        print('Exibindo extrato...')
else: # não é muito utilizado
    print('Obrigada por usar nosso sistema bancário, até logo!')