# Loja

def cadastro_cliente(nome, email, telefone):
    with open("clientes.txt", "a") as arquivo:
        arquivo.write(f"{nome};{email};{telefone}\n")
        print(f"Cliente {nome} cadastrado com sucesso!")


def listar_clientes():
    try:
        with open("clientes.txt", "r") as arquivo:
            clientes = arquivo.readlines()
            if not clientes:
                print("Nenhum cliente cadastrado!")
            else:
                print("Clientes cadastrados:")
                for cliente in clientes:
                    nome, email, telefone = cliente.strip().split(";")
                    print(f"Nome: {nome}, Email: {email}, Telefone: {telefone}")
    except FileNotFoundError:
            print("Arquivo de clientes não encontrado!")            


#manipular o arquivo
def salvar_em_arquivo(dados, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        for item in dados:
            arquivo.write(f"{item}\n")
    
def ler_dados_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            return arquivo.readlines()
    except FileNotFoundError:
        return [] 



cadastro_cliente ("Luiz" , "luizteste@gmail.com" , "123456789")
cadastro_cliente ("Pedro", "pedroteste@hotmail.com", "987654321")

listar_clientes()