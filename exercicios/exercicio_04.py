"""Exercício 04.

Média das Notas
Faça um programa que peça quatro notas bimestrais e apresente a média delas.
"""

notas = []

for i in range(1, 5):
    while True:
        try:
            nota = float(input(f"Infome a nota do {i}° bimestre: "))
            break
        except ValueError:
            print("O valor informado deve ser um número")
            continue
    
    notas.append(nota)
    
media = sum(notas) / len(notas)

print(f"A média é: {media}")