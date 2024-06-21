lista = ('lapis', 1.75,
'caderno', 20,
'caneta', 2.20,
'estojo', 9.80,
'mochila', 150, 
'régua', 12.60)

print('-' * 40)
print(f'{'Listagem de preços':^40}')
print('-' * 40)

for posic in range(0, len(lista)):
    if posic % 2 == 0:
         print(f'{lista[posic]:.<30}', end='')
    else:
         print(f'R${lista[posic]:>7.2f}')
print('-' * 40)
