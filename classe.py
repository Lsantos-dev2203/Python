import datetime as datetime


class livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self. autor = autor
        self.ano_publicacao = ano_publicacao

    def info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano de Publicação: {self.ano_publicacao}"
    
    def idade_do_livro(self):
        ano_atual = datetime.now().year
        return ano_atual - self.ano_publicacao
    

livro1 = livro("A Game of Thrones", "George R. R. Martin", 1996)

print(livro1.info())

print(f"Idade do livro: {livro1.idade_do_livro()} anos")

        
