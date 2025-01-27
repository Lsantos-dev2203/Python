nome = input("Qual o seu nome ?: ")

Lista_nomes=[]


#print (f"Ola, {nome} ! Seja bem vindo!")

if nome == '' :
    print("Por favor, insira seu nome.")
    nome = input('Qual o seu nome? : ')
    print(f"Ola, {nome}!")
    Lista_nomes.append(nome)


else: 
    print(f"Ola, {nome}!");
    {
        print(f"Seja bem vindo, {nome}!")
    }
    Lista_nomes.append(nome)


print("A lista de nomes cadastrados é : ", Lista_nomes)

