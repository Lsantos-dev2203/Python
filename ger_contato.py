class Contato:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def mostrar_informacoes(self):
        return f'Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}'


class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def listar_contatos(self):
        for contato in self.contatos:
            print(contato.mostrar_informacoes())


def main():
    minha_agenda = Agenda()

    while True:
        print("\n1 - Adicionar contato")
        print("2 - Listar contatos")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            nome = input("Digite o nome: ")
            email = input("Digite o email: ")
            telefone = input("Digite o telefone: ")
            contato = Contato(nome, email, telefone)
            minha_agenda.adicionar_contato(contato)
            print("Contato adicionado com sucesso!")
        elif opcao == 2:
            print("\nLista de contatos:")
            minha_agenda.listar_contatos()
        elif opcao == 0:
            print("SAINDO...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
