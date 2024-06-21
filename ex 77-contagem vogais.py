lista = ('arroz', 'feijao', 'carne', 'paçoca', 'frango', 'banana', 'maça')
for i in lista:
    print(f'\nNa palavra {i.upper()} temos as vogais ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
