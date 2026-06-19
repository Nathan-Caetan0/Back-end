"""Exercício 14.

Multa por Excesso de Pesca
Você foi contratado pela Secretaria de Meio Ambiente para criar um sistema que ajude na
fiscalização da pesca em reservas naturais.
De acordo com a legislação local, pescadores têm um limite de captura de 50 quilos de
peixes por dia para evitar a superexploração.
Para cada quilo excedente, é imposta uma multa de R$ 4,00.
Seu programa deve:
    a. Solicitar a quantidade total de peixes pescados (em quilos) por um pescador em
        um único dia;
    b. Calcular e exibir qualquer excesso de peso além do limite permitido de 50
        quilos;
    c. Se houver excesso, calcular e exibir o valor da multa que o pescador deve
        pagar.
"""

def calc_multa(quilos):
    return quilos * 4.00

while True:
    try:
        kg_pescados = float(input("Informe quantos quilos foram pescados: "))

        if kg_pescados < 0:
            print("Entrada inválida. Por favor, digite um número positivo.")
            continue
        
        break

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        continue
    
kg_excedidos = kg_pescados - 50

if kg_excedidos > 0:
    print("Quilos maximos exedidos!")
    valor_pagar = calc_multa(kg_excedidos)
    print(f"Você excedeu {kg_excedidos}kg do limite, você fui multado em R${valor_pagar:.2f}")

else:
    print("Você está dentro do limite diário!")