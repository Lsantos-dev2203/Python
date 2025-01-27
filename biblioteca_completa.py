from pathlib import  Path

caminho_do_cliente = Path("clientes_biblioteca.txt")

caminho_livro = Path("livros_clientes.txt")

try:
    with caminho_do_cliente.open() as arquivo:
        linhas = arquivo.readlines()
        numero_cartao = len(linhas) + 1
        print(f"Novo cliente cadastrado com cartão {numero_cartao}")

except FileNotFoundError:
    numero_cartao = 1
    print("Arquivo de clientes não encontrado, criando um novo...")

nome = input("Digite seu nome: ")
telefone = input("Digite seu telefone: ")

with caminho_do_cliente.open(mode='a') as arquivo:
    arquivo.write(f"{nome}; {telefone}; {numero_cartao}\n")

print(f"Cliente cadastrado com sucesso! Seu numero de cartão é : {numero_cartao}")    

numero_cartao = int(input("Digite o numero do cartao: "))

try:
    with caminho_do_cliente.open() as arquivo:
        linhas = arquivo.readlines()
        encontrou = False
        for linha in linhas:
            numero_cartao, livros = linha.strip().split(', ', 1)
            if int(numero_cartao) == numero_cartao:
                print (f"Livros pegos: {livros}")
                encontrou = True
        if not encontrou:
            print("Nenhum livro encontrado nesse numero de cartão!!")
except FileNotFoundError:
    print("Nenhum registro encontrado")    

# livros =  input("Digite o nome dos livroes escolhidos (Separados por virgula): ")

# with caminho_livro.open(mode='a') as arquivo:
#     arquivo.write(f"{numero_cartao}; {livros}\n")

#     print(f"Livros adicionados com sucesso!")