#Exibir ao usuario os dois numeros
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

#Compara os dois numeros e imprimir o resultado
if numero1 > numero2:
    print(f"O primeiro número é ({numero1}) é maior que o segundo número ({numero2}).")
elif numero2 > numero1:
    print(f"O segundo número é ({numero2}) é maiopr que o primeiro número ({numero1}).")   
else:
    print(f"Os dois números são iguais ({numero1}).")     