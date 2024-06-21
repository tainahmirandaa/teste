lista = []
menor = maior = 0
for i in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
    
print(f'Você digitou os valores {lista}')
print(f'O maior valor é {maior} na posição ', end='')
for n, v in enumerate(lista):
    if v == maior:
        print(f'{n + 1}... ', end='')
print(f' e o menor valor é {menor} na posição ', end='')
for n, v in enumerate(lista):
    if v == menor:
        print(f'{n + 1}... ', end='')
