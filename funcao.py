# def saudacao(nome):
#     print(f"Olá, {nome}!")

# saudacao("Luiz")



# def soma (a, b):
#     return a + b


# reultado = soma(3, 6)

# print(reultado)



# def pitagoras (cateto1=None, cateto2=None, hipotenusa=None):
#     if hipotenusa is None:
#         return (cateto1 ** 2 + cateto2 ** 2) ** 0.5
#     elif cateto1 is None:
#         return (hipotenusa ** 2 - cateto2 ** 2) ** 0.5
#     elif cateto2 is None:
#         return (hipotenusa ** 2 - cateto1 ** 2) ** 0.5
#     else:
#         raise ValueError ("Um dos parametros devem ser 'NONE'")


# cateto1 = float(input("Insira o primeiro cateto: "))
# cateto2 = float(input("Insira o segundo cateto: "))

# hipotenusa = pitagoras(cateto1, cateto2)

# print(f"A hipotenusa é: {hipotenusa}")



def fibonacci(n):
    if n <= 0:
        return "Número inválido. Insira um número inteiro positivo."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

# Exemplo de uso:
n = int(input("Digite o número da posição desejada na sequência de Fibonacci: "))
print(f"O {n}º número na sequência de Fibonacci é: {fibonacci(n)}")

 



    