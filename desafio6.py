lista = []
 
numero1 = input('Digite o primeiro numero: ')
numero2 = input('Digite o segundo numero: ')
numero3 = input('Digite o terceiro numero: ')
numero4 = input('Digite o quarto numero: ')

lista.append(numero1)
lista.append(numero2)
lista.append(numero3)
lista.append(numero4)


lista.sort()
print(f'O menor numero é {lista[0]}')
print(f'O maior numero é {lista[-1]}')
