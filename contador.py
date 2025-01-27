# Dicionário para armazenar os produtos e suas quantidades
estoque = {}

print("Leitor de código de barras ativo. Digite os códigos de barras e pressione Enter.")
print("Pressione Enter sem digitar nada para finalizar.")

while True:
    # Lê o código de barras do terminal
    codigo_barra = input("Escaneie o código de barras: ").strip()
    
    # Verifica se o usuário pressionou Enter sem digitar nada (sinal para sair)
    if codigo_barra == "":
        break
    
    # Adiciona ou incrementa o produto no estoque
    if codigo_barra in estoque:
        estoque[codigo_barra] += 1
    else:
        estoque[codigo_barra] = 1
    
    print(f"Produto {codigo_barra} registrado. Quantidade: {estoque[codigo_barra]}")

print("\nContagem final de produtos:")
for produto, quantidade in estoque.items():
    print(f"Produto: {produto}, Quantidade: {quantidade}")
