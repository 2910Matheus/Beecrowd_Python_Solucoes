"""
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
"""
valores = input().split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

valores1 = a,b,c
valoresl = sorted(valores1)

for num in valoresl:
    print(num)

print()

for num1 in valores:
    print(num1)
