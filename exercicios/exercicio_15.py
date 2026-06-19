"""Exercício 15.

Cálculo de Salário com Descontos
Escreva um programa que solicite ao usuário o valor que ele ganha por hora e o número
de horas trabalhadas no mês.
Calcule e mostre o salário bruto, os valores descontados para o Imposto de Renda (11%),
o INSS (8%) e o sindicato (5%), além do salário líquido (salário bruto - descontos).
Mostre os dados para o usuário conforme a tabela abaixo:
    (+) Salário bruto: R$
    (-) IR (11%): R$
    (-) INSS (8%): R$
    (-) Sindicato (5%): R$
    (-) Descontos: R$
    (=) Salário líquido: R$
"""

valor_hora = float(input("Informe o valor de sua hora de trabalho: "))

horas_trabalhadas = int(input("Informe quantas horasz trabalha por mês: "))

salario_bruto = valor_hora * horas_trabalhadas

salario_liquido = salario_bruto

descontos = [
    {
        "nome": "IR",
        "porcentagem": 11
    },
    {
        "nome": "INSS",
        "porcentagem": 8
    },
    {
        "nome": "Sindicato",
        "porcentagem": 5
    }
]

for desconto in descontos:
    valor = salario_bruto * (desconto["porcentagem"] / 100)
    
    salario_liquido -= valor
    
print(f"(+) Salário bruto: R$ {salario_bruto:.2f}")

for desconto in descontos:
    valor = salario_bruto * (desconto["porcentagem"] / 100)
    print(f"(-) {desconto['nome']} ({desconto['porcentagem']}%): R$ {valor:.2f}")
    
print(f"(-) Descontos: R$ {salario_bruto - salario_liquido:.2f}")
print(f"(=) Salário líquido: R$ {salario_liquido:.2f}")