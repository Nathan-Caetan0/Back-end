"""Exercício 16.

Loja de Tintas (Simples)
Faça um programa para uma loja de tintas.
O programa deve solicitar o tamanho em metros quadrados da área a ser pintada.
Considere que cada litro de tinta cobre uma área de 7 metros quadrados e que a tinta é
vendida em latas de 18 litros, custando R$ 570,00 cada.
Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total.
"""

import math

while True:
    try:
        metros = float(input("Informe quantos metros quadrados você precisa pintar: "))
        if metros <= 0:
            print("O número de metros deve ser maior que 0!")
            continue
        
        break
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número positivo.")
        continue

litros_tinta = metros / 7
n_latas = math.ceil(litros_tinta / 18)
valor_pagar = n_latas * 570.00

print(f"Você vai precisar de {n_latas} latas de tinta")
print(f"Total: R${valor_pagar:.2f}")