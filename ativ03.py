#Exibe ao usuário em uma lista armazenada
notas = []
print(20*'-', ' BOLETIM EWSCOLAR ' ,20*'-')
numero_usuario1 = int(input('Digite uma nota: '))
notas.append(numero_usuario1)

numero_usuario2 = int(input('Digite uma nota: '))
notas.append(numero_usuario2)

numero_usuario3 = int(input('Digite uma nota: '))
notas.append(numero_usuario3)

numero_usuario4 = int(input('Digite uma nota: '))
notas.append(numero_usuario4)

numero_usuario5 = int(input('Digite uma nota: '))
notas.append(numero_usuario5)

#len conta a quantidade de elemento dento de uma lista            
quantidade_notas = len(notas)

#sum irá somar todos os valores da lista
soma = sum(notas)

media = soma / quantidade_notas


print(f'A nota são: {notas}')
print(f'A quantidade de notas: {quantidade_notas}')
print(f'A soma de todas as notas: {soma}')
print(f'A média: {media}')

    #TODO: Situacão
    # Aprovado >=7
    # Recuperação >=5
    # Reprovado

if media >= 7:
    print(f'Aprovado com média {media}')

elif media >=5:
    print(f'Recuperação com média {media}')

else:
    print(f'Reprovado com média {media}')     

  


   