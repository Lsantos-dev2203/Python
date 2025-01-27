# # Criando uma lista vazia de nomes
# nomes = []

# # Loop para adicionar nomes à lista
# while True:
#     nome = input("Digite um nome para adicionar à lista (ou 'sair' para encerrar): ")
#     if nome.lower() == "sair":
#         break
#     nomes.append(nome)
#     print(f"'{nome}' foi adicionado à lista!")

# # Exibindo a lista final
# print("\nLista de nomes:")
# print(nomes)




Produtos = []

while True:
    produto = input("Digite um produto (ou 'sair' para encerrar): ")
    if produto.lower() == "sair":
        break
    try:
        preco = float(input("Digite o preço do produto: "))
        Produtos.append((produto, preco))
        print(f"'{produto}' foi adicionado à lista com o preço de: R$ {preco:.2f}!")
    except ValueError:
        print("Por favor, digite um valor numérico para o preço.")

# Salvando a lista em um arquivo de texto
with open("produtos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Lista de Produtos:\n")
    for item in Produtos:
        arquivo.write(f"Produto: {item[0]}, Preço: R$ {item[1]:.2f}\n")

print("\nLista de produtos salva no arquivo 'produtos.txt'.")

print(Produtos)


