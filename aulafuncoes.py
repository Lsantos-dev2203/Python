# def saudacao_personalizada(nome):
#     print(f"Olá, {nome}, seja bem vindo !")

# nome = input ("Diga seu nome: ") 
# saudacao_personalizada(nome)   



# def soma(a, b):
#     return a + b

# num1 = int(input("Digite um numero: "))

# num2 = int(input("Digite outro numero: "))

# result = soma(num1, num2)

# print(f"A soma de {num1} e {num2} é: {result}")


def verificar_maioridade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"
    
idade = int(input("Qual a sua idade ?: "))

resultado = verificar_maioridade(idade) 

print(f"Você é {resultado}")
