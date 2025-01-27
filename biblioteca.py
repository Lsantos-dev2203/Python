from pathlib import Path


caminho_do_arquivo = Path ("cliente_biblioteca.txt")

nome = input("Digite seu nome: ")
telefone = input("Digite seu telefone: ")
numero_do_cartao = input("Digite o numero do cartao: ")

with caminho_do_arquivo.open(mode= 'a') as arquivo :
    arquivo.write(f"{nome}; {telefone}; {numero_do_cartao}\n")

print("Cliente salvo com sucesso")
