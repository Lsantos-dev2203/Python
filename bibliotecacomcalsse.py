"""
Sistema de Biblioteca para gerenciar livros, permitindo adicionar, listar e salvar em arquivos de texto.
"""

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def mostrar_informacoes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano de Publicação: {self.ano}"


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return
        for livro in self.livros:
            print(livro.mostrar_informacoes())

    def salvar_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            for livro in self.livros:
                arquivo.write(f"{livro.mostrar_informacoes()}\n")
        print(f"Livros salvos no arquivo {nome_arquivo} com sucesso!")


def main():
    bibliotecas = Biblioteca()

    while True:
        print("\nBem-vindo à Biblioteca!")
        print("1 - Adicionar Livro")
        print("2 - Listar Livros")
        print("3 - Salvar Livros em Arquivo")
        print("0 - Sair")
        escolha = int(input("Digite a opção: "))

        if escolha == 1:
            titulo = input("Digite o nome do livro: ")
            autor = input("Digite o nome do autor: ")
            ano = int(input("Digite o ano de publicação: "))
            livro = Livro(titulo, autor, ano)
            bibliotecas.adicionar_livro(livro)
            print("Livro adicionado com sucesso!")
        elif escolha == 2:
            print("\nLista de livros:")
            bibliotecas.listar_livros()
        elif escolha == 3:
            nome_arquivo = input("Digite o nome do arquivo: ")
            bibliotecas.salvar_arquivo(nome_arquivo)
        elif escolha == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
