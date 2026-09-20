print('WHILE/BREAK:')
while True:
    number = int(input('Informe um número: '))

    if number == 10:
        break

    print(number)
    
print('\nFOR/BREAK:')
for number in range(100):
    if number == 10:
        break

    print(number, end=' ')

print('\n\nFOR/CONTINUE:')
for number in range(100):
    if number % 2 == 0:
        continue

    print(number, end=' ')

# Em resumo, break interrompe a execução quando a condição é atingida e o continue pula a execução