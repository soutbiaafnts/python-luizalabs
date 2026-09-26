# -----------------------------------------------------------------
# FATIAMENTO DE STRING
# É uma técnica utilizada para retornar substrings (parte da string original), informando início (start), fim (stop) e
# passo (step): [start: stop[, step]].

name = 'Bianca de Castro Aguiar Fontes'

print(name[0]) # primeiro caractere
print(name[-1]) # último caractere
print(name[:6]) # do início até o sexto caractere
print(name[7:]) # do sétimo caractere até último
print(name[10:16]) # entre o décimo e o décimo sexto caractere
print(name[10:16:2]) # o mesmo intervalo anterior, porém de dois em dois
print(name[:]) # string completa
print(name[::-1]) # espelhar a string