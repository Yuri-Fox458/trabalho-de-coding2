def menu():
    print("\n" + "=" * 30)
    print("  CALCULADORA")
    print("=" * 30)
    print("1 - somar (+)")
    print("2 - subtrair (-)")
    print("3 - multiplicar (*)")
    print("4 - dividir (/)")
    print("5 - sair")
    print("=" * 30)
    opcao = input("escolha uma operação: ")
    return opcao

def obter_numeros():
    num1 = float(input("digite o primeiro número: "))
    num2 = float(input("digite o segundo número: "))
    return num1, num2

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return None #Aqui é para evitar o erro da divisão por 0
    return a / b

def main():
    while True:
        escolha = menu()

        if escolha == "5":
            print("encerrando calculadora...")
            break

        if escolha in ["1", "2", "3", "4"]:
            n1, n2 = obter_numeros()

            if escolha == "1":
                resultado = somar(n1, n2)
                print(f"Resultado: {n1} + {n2} = {resultado}")

            elif escolha == "2":
                resultado = subtrair(n1, n2)
                print(f"Resultado: {n1} - {n2} = {resultado}")

            elif escolha == "3":
                resultado = multiplicar(n1, n2)
                print(f"Resultado: {n1} * {n2} = {resultado}")

            elif escolha == "4":
                resultado = dividir(n1, n2)
                if resultado is None:
                    print("Erro: nâo é possivel dividir um número por 0!")
                else:
                    print(f"Resultado: {n1} / {n2} = {resultado:.2f}")
        else:
            print("Opção inválida! Por favor, digite um número de 1 a 5.")

main()
