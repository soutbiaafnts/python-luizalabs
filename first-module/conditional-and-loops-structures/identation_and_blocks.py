# IDENTAÇÃO
## Identar código é uma forma de manter o código fonte mais legível e manutenível. Mas, em Python, ela exerce um segundo papel:
## através da identação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

# BLOCO DE COMANDO
# As linguagens de programação costumam utilizar caracteres ou palavras reservadas para determinar o início e fim do bloco.
# Em Java e C por exemplo, utilizamos chaves { } para determinar o início e fim do bloco de comando. Em Python, utilizamos a identação.

# UTILIZANDO ESPAÇOS
# Existe uma convenção em Python, que define as boas práticas para escrita de código na linguagem. Nesse documento é indicado utilizar 4 espaços
# em branco por nível de identação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco. Exemplo:

# def withdraw(self, value: float) -> None: #início do bloco do método
#    if self.balance >= value: # início do bloco do if
#        self.balance -= value
#    # fim  do bloco do if
## fim do bloco do método

# : indica o início do bloco (O Python tem um caractere que indica o início, porém, não tem o que indique o fim)

# Prática da aula
def withdraw(value):
    balance = 500

    if balance >= value:
        print('Valor sacado!')
        print('Retire o seu dinheiro na boca do caixa.')
    else:
        print('Saldo insuficiente...')

print('Teste com valor menor do que o saldo:')
withdraw(100)
print('\nTeste com valor maior do que o saldo:')
withdraw(1000)