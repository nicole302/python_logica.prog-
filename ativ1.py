lista = [5,8,2,9,1]
print(lista)

lista.sort()
print(f"ordem crescente {lista}")

lista.sort(reverse=True)
print(f"ordem decrecente {lista}")

lista.append(7)
lista.insert(1, 3)
print("alteração 1",lista)

lista.insert(0, 10)
lista.remove(9)
print("altaração 2",lista)

del lista[1:4]
print("alteração 3", lista)