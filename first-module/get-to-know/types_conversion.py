# Inteiro para Float || Float para Inteiro
print('Conversão de tipos numéricos')
print('----------------------------')
cost = 10
print(f'Preço: {cost} | Tipo: {type(cost)}')
cost = float(cost)
print(f'Preço: {cost} | Tipo: {type(cost)}') 
cost = int(cost)

## Conversão por divisão
print('----------------------------')
print('Conversão de tipos numéricos por divisão')
print(f'Preço: {cost} | Tipo: {type(cost)}')
cost = 10 / 2
print(f'Preço: {cost} | Tipo: {type(cost)}')
cost = int(cost)
print(f'Preço: {cost} | Tipo: {type(cost)}') 
cost = cost // 2
print(f'Preço: {cost} | Tipo: {type(cost)}') # assim é possível converter float para inteiro, mas o valor será arredondado para baixo.

# Numérico para String
print('----------------------------')
print('Conversão de tipos numéricos para string')
cost = 10.50
age = 23
print(f'Preço: {cost} | Tipo: {type(cost)}')
print(f'Idade: {age} | Tipo: {type(age)}')
cost = str(cost)
age = str(age)
text = f"[Idade: {age}  Preço: {cost}]" # Não é possível concatenar tipos diferentes, então é necessário converter para string.
print(f'Texto: {text} | Tipo: {type(text)}')

# String para Numérico
print('----------------------------')
print('Conversão de tipos string para numérico')
cost = '10.50'
age = '23'
print(f'Preço: {cost} | Tipo: {type(cost)}')
print(f'Idade: {age} | Tipo: {type(age)}')
cost = float(cost)
age = int(age)
print(f'Preço: {cost} | Tipo: {type(cost)}')
print(f'Idade: {age} | Tipo: {type(age)}')

# Erro de conversão
print('----------------------------')
print('Erro de conversão de tipos')
cost = 'Python'
print(f'Preço: {cost} | Tipo: {type(cost)}')
print(float(cost))