# -----------------------------------------------------------------
# MAIÚSCULAS, MINÚSCULAS E TÍTULO
course = 'pYthon'

# upper() -> converte todos os caracteres para maiúsculo
print(course.upper())

# lower() -> converte todos os caracteres para minúsculo
print(course.lower())

# title() -> converte o primeiro caractere para maiúsculo e todo o restante para minúsculo
print(course.title())

# -----------------------------------------------------------------
# ELIMINANDO ESPAÇOS EM BRANCO
course = '  Python  '

# strip() -> remove espaços em branco tanto na direita quanto na esquerda
print(course.strip())

# strip() -> remove espaços em branco da esquerda
print(course.lstrip())

# strip() -> remove espaços em branco da direita
print(course.rstrip())

# -----------------------------------------------------------------
# JUNÇÕES E CENTRALIZAÇÃO
course = 'Python'

# center() -> centraliza, primeiro parâmetro (número de caracteres que irá ocupar), segundo parâmetro (caractere que ocupa os espaços, opcional)
print(course.center(10, '#'))

# join() -> 'caractere que quer juntar'.join(iterável)
print('.'.join(course))
