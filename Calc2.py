def calculadora():
    while True:
        print("Selecione a operação desejada:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        escolha = input("Digite o número da operação: ")
        
        if escolha == '0':
            print("Obrigado por usar a calculadora. Adeus!")
            break
        elif escolha in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if escolha == '1':
                resultado = num1 + num2
            elif escolha == '2':
                resultado = num1 - num2
            elif escolha == '3':
                resultado = num1 * num2
            elif escolha == '4':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    print("Erro: Divisão por zero.")
                    continue
            print(f"Resultado: {resultado}")
        else:
            print("Essa opção não existe. Tente novamente.")

if __name__ == "__main__":
    calculadora()
