# contador = 10

# while contador < 0 :
#     print(contador)
#     contador -= 1

#     print ("Feliz aniversario")

    


senha_correta = 'python123'
tentativa = ''

print('Bem vindo! Por favor insira a sua senha.')

while tentativa != senha_correta:
    tentativa = input('Senha: ')
    
    if tentativa != senha_correta:
        print('Senha incorreta. Tente novamente.')

print('Senha correta! Acesso liberado')    




