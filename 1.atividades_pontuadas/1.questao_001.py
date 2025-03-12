import os
os.system("clear")

#Faça um algoritmo que leia A,B,C e imprimar na tela
#se a soma A + B é menor, caso ao contrario, imprima
#A + B é maior que C

#Entrada
a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))
c = int(input("Informe o terceiro número: "))
soma = a + b


#Solicitando Dados

if soma < c:
    print(f" A + B é menor que C")
elif soma > c:
    print(f" A + B é maior que C")
else:
    print("Opção Inválida.")