# -----------------------------------------------------------------
# STRING DE MÚLTIPLAS LINHAS || STRINGS TRIPLAS
# As strings de múltiplas linhas são definidas informando 3 aspas simples ou duplas durante a atribuição. Elas podem 
# ocupar várias linhas do código, e todos os espaços em branco são incluídos na string final

name = 'Bianca'

message = f'''
Olá, meu nome é {name}!
Eu estou aprendendo Python.'''

print(message)

print()

print(
    '''
    =============== MENU ===============

    1 - Depositar
    2 - Sacar
    0 - Sair

    ====================================

    Obrigada por usar nosso sistema!
''')