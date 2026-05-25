def mostrar_menu():
    for index,(name, func) in enumerate(actions, start=1):
        print(f"{index}. {name}")
        
def input_numeros():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            break
        except ValueError:
            print("Erro! Digite um número válido.")
    
    while True:
        try:
            num2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Erro! Digite um número válido.")
    
    return num1, num2

def adicao():
    print("========================")
    print("Adição")
    print("========================")
    
    num1, num2 = input_numeros()
    
    resultado = num1 + num2
    
    print(f"\nResultado: {resultado}\n")
    
def subtracao():
    print("========================")
    print("Subtração")
    print("========================")
    
    num1, num2 = input_numeros()
    
    resultado = num1 - num2
    
    print(f"\nResultado: {resultado}\n")
    
def multiplicacao():
    print("========================")
    print("Multiplicação")
    print("========================")
    
    num1, num2 = input_numeros()
    
    resultado = num1 * num2
    
    print(f"\nResultado: {resultado}\n")
    
def divisao():
    print("========================")
    print("Divisão")
    print("========================")
    
    num1, num2 = input_numeros()
    
    if num2 == 0:
        print("\nErro! Não é possível dividir por zero.\n")
        return
    
    resultado = num1 / num2
    
    print(f"\nResultado: {resultado}\n")

def sair_sistema():
    print("Saindo...")
    exit()

actions = [
    ("Adição", adicao),
    ("Subtração", subtracao),
    ("Multiplicação", multiplicacao),
    ("Divisão", divisao),
    ("Sair do sistema", sair_sistema)
]


while True:
    print("========================")
    print("Calculadora")
    print("========================")
    
    mostrar_menu()
    print("========================")
    
    try:
        opcoes = int(input("Escolha uma opção (1-5): "))
        
        if opcoes < 1 or opcoes > 5:
            print("Erro! Escolha uma opção entre 1 e 5.\n")
            continue
        
        actions[opcoes - 1][1]()
        
    except ValueError:
        print("Erro! Digite um número inteiro de 1 a 5.\n")
        continue
    except IndexError:
        print("Erro! Opção inválida.\n")
        continue