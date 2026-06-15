"""Exercício 08.

Cálculo de Salário
Elabore um programa que calcule o salário mensal de uma pessoa, com base nas horas
trabalhadas por mês e no valor por hora.
"""

valor_hora = float(input("Informe o valor de sua hora de trabalho: "))

horas_trabalhadas = int(input("Informe quantas horasz trabalha por mês: "))

salario = valor_hora * horas_trabalhadas

print(f"O salário é de: R${salario:.2}")