"""Exercício 03.

Soma de Dois Números
Desenvolva um programa que solicite dois números ao usuário e mostre o resultado da soma
desses números.
"""

soma = 0

for i in range(1, 3):
    while True:
        try:
            numero = float(input(f"Digite o numero {i}: "))
            break
        except ValueError:
            print("O valor informado deve ser um número")
            continue
    
    soma += numero
    
print(f"A soma dos dois numeros é: {soma}")