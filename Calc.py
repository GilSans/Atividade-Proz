def calculadora(num1, num2, operacao):
    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4:
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero."
    else:
        resultado = 0  # Operação inválida
    
    return resultado