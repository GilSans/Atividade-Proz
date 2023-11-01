import datetime

def obter_ano_nascimento():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento (1922-2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Ano fora do intervalo permitido")
        except ValueError:
            print("Entrada inválida. Digite um ano válido.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    return ano_atual - ano_nascimento

nome_completo = input("Digite seu nome completo: ")
ano_nascimento = obter_ano_nascimento()
idade = calcular_idade(ano_nascimento)

print(f"Olá, {nome_completo}! Você completou ou completará {idade} anos em 2022.")
