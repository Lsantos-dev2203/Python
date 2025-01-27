from pathlib import Path

#define o caminho do arquivo
caminho_arquivo = Path ("meusdados.txt")

#dados pra salvar no arquivo
dados_para_salvar = ["python, c#, delphi"]

#abre o arquivo no modo 'w' (Escrita) e salva os dados 
with caminho_arquivo.open(mode= 'w') as arquivo :
    for item in dados_para_salvar:
        arquivo.write(f"{item}\n")


print("Dados salvos com sucesso")


with caminho_arquivo.open(mode='r') as arquivo:
    dados_lidos = arquivo.readlines()



dados_lidos = [linha.strip() for linha in dados_lidos]

print("Os dados lidos são:", dados_lidos)


