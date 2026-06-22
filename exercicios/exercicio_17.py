"""Exercício 17.

Loja de Tintas (Otimizada)
Faça um programa para uma loja de tintas.
O programa deve solicitar o tamanho em metros quadrados da área a ser pintada.
Considere que cada litro de tinta cobre uma área de 7 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 570,00 ou em galões de 3,5 litros, que
custam R$ 130,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em
3 situações:
    a. Comprar apenas latas de 18 litros;
    b. Comprar apenas galões de 3,5 litros;
    c. Uma combinação de ambos de forma que o custo seja minimizado.
Adicione 10% de folga à quantidade de tinta a ser comprada e arredonde os valores de
forma que somente latas cheias sejam vendidas.
"""

import math

def calc_latas(litros_tinta):
    if litros_tinta < 18:
        total_latas = math.ceil(litros_tinta / 3.5)
        
        return total_latas
    else:
        n_latas_grandes = litros_tinta / 18
        resto = litros_tinta % 18
        
        if resto:
            n_latas_pequenas = resto / 3.5
        
        return n_latas_grandes, n_latas_pequenas if n_latas_pequenas else None

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