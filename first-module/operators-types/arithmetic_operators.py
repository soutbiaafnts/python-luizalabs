product_1 = 20
product_2 = 10

print(product_1 + product_2) # soma
print(product_1 - product_2) # subtração
print(product_1 / product_2) # divisão
print(product_1 // product_2) # divisão inteira
print(product_1 * product_2) # multiplicação
print(product_1 % product_2) # resto da divisão
print(product_1 ** product_2) # exponenciação

# o parentes dita a ordem em que a operação será realizada, caso não haja, a ordem de precedência é: 
# 1º exponenciação, 2º multiplicação e divisão, 3º soma e subtração.
x = (10 + 5) * 4
y = (10 / 2) + (25 * 2) - (2 ** 2)
print(x)
print(y)