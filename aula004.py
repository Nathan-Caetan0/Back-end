#====================================
#AULA 004 - Estruturas de Controle
#====================================

#1. SWITCH CASE (SE... SENÃO SE... SENÃO)
#==========================================

print("=== SWITCH CASE COM IF/ELIF/ELSE ===\n")

#Exemplo 1: Escolher uma cor
cor = input("Escolha uma cor (vermelho, azul, verde): ")

if cor == "vermelho":
    print("Você escolheu VERMELHO!")
elif cor == "azul":
    print("Você escolheu AZUL!")
elif cor == "verde":
    print("Você escolheu VERDE!")
else:
    print("Cor desconhecida!")

if cor == "vermelho" or cor=="verde" or cor=="azul":
    print(f"Você escolheu {cor.upper()}!")
else:
    print("Cor desconhecida!")



print()

#Exemplo 2: Verificar nota
nota = int(input("Digite a nota (0-10): "))

if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Bom!")
elif nota >= 5:
    print("Satisfatório!")
else:
    print("Insuficiente!")


if nota >= 5 and nota < 7:
    print("Satisfatório!")
elif nota >= 9 and nota<=10:
    print("Excelente!")
elif nota <5 and nota>=0:
    print("Insuficiente!")
elif nota >=7 and nota <9:
    print("Bom!")
elif nota<0 or nota>10:
    print("Erro!")
else:
    print("Nota não reconhecida!")

print()

#Exemplo 3: SWITCH/CASE (Python 3.10+)
print("=== SWITCH CASE COM MATCH/CASE ===\n")

dia = int(input("Digite o número do dia (1-7): "))

match dia:
    case 1:
        print("Segunda-feira")
    case 2:
        print("Terça-feira")
    case 3:
        print("Quarta-feira")
    case 4:
        print("Quinta-feira")
    case 5:
        print("Sexta-feira")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Dia inválido!")

print()


#2. LAÇO FOR (REPETIÇÃO COM QUANTIDADE DEFINIDA)
#=================================================

print("=== LAÇO FOR ===\n")

# Exemplo 1: Contar de 1 a 5
print("Contando de 1 a 5:")
for numero in range(1, 11):
    print(numero)


print()

# Exemplo 2: Repetir uma frase
print("Repetindo uma frase:")
for i in range(3):
    print(f"Olá, turma! (laço {i})")

print()

#Exemplo 3: Usar variável para contar
print("Tabuada do 2:")
for numero in range(1, 11):
    resultado = 2 * numero
    print(f"2 x {numero} = {resultado}")

print()


#3. LAÇO WHILE (REPETIÇÃO ENQUANTO CONDIÇÃO FOR VERDADEIRA)
#===========================================================

print("=== LAÇO WHILE ===\n")

# Exemplo 1: Contagem simples
print("Contando de 1 até 5 com while:")
numero = 1
while numero <= 5:
    print(numero)
    numero = numero + 1

print()

# Exemplo 2: Repetir com condição
print("Repetindo enquanto a condição é verdadeira:")
contador = 0
while contador < 3:
    print(f"Executando... {contador}")
    contador = contador + 1

print()

# 4. FUNÇÃO RANGE()
# =================

print("=== FUNÇÃO RANGE() ===\n")

# Exemplo 1: range(5) - do 0 ao 4
print("range(5) - números de 0 a 4:")
print(list(range(5)))

print()

# Exemplo 2: range(1, 6) - do 1 ao 5
print("range(1, 6) - números de 1 a 5:")
print(list(range(1, 6)))

print()

# Exemplo 3: range(0, 10, 2) - de 2 em 2
print("range(0, 10, 2) - números pares de 0 a 9:")
print(list(range(0, 10, 2)))

print()


# 5. FORMATAÇÃO DE STRINGS
# ========================

print("=== FORMATAÇÃO DE STRINGS ===\n")

# Exemplo 1: Simples
nome = "Maria"
idade = 16
print(f"Meu nome é {nome} e tenho {idade} anos")

print()

# Exemplo 2: Com números decimais
preco = 19.99
print(f"O produto custa R$ {preco:.2f}")

print()

# Exemplo 3: Usando format()
mensagem = "Olá {}, bem-vindo(a)!"
print(mensagem.format("João"))

print()

# Exemplo 4: Concatenação simples
saudacao = "Bom dia " + nome
print(saudacao)