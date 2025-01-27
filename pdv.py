import tkinter as tk
from tkinter import messagebox

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class PDV:
    def __init__(self, root):
        self.root = root
        self.root.title("PDV LUIZ SANTOS")
        self.produtos_no_carrinho = []
        
        # Definindo interface gráfica
        self.lista_produtos = [
            Produto("Produto 1", 10.00),
            Produto("Produto 2", 25.50),
            Produto("Produto 3", 15.30)
        ]
        
        self.total_label = tk.Label(self.root, text="Total: R$0.00", font=("Arial", 14))
        self.total_label.grid(row=0, column=0, columnspan=2)
        
        self.carrinho_listbox = tk.Listbox(self.root, width=30, height=10)
        self.carrinho_listbox.grid(row=1, column=0, padx=10, pady=10)
        
        self.desconto_label = tk.Label(self.root, text="Desconto: R$", font=("Arial", 12))
        self.desconto_label.grid(row=2, column=0, padx=10, pady=5)
        
        self.desconto_entry = tk.Entry(self.root)
        self.desconto_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.adicionar_button = tk.Button(self.root, text="Adicionar Produto", command=self.adicionar_produto)
        self.adicionar_button.grid(row=3, column=0, padx=10, pady=5)
        
        self.finalizar_button = tk.Button(self.root, text="Finalizar Compra", command=self.finalizar_compra)
        self.finalizar_button.grid(row=3, column=1, padx=10, pady=5)
        
        self.produto_buttons()
        
    def produto_buttons(self):
        for i, produto in enumerate(self.lista_produtos):
            button = tk.Button(self.root, text=f"{produto.nome} - R${produto.preco:.2f}", command=lambda p=produto: self.adicionar_produto(p))
            button.grid(row=i + 4, column=0, columnspan=2, padx=10, pady=5)
    
    def adicionar_produto(self, produto=None):
        if produto is None:
            produto = self.lista_produtos[0]  # Adiciona Produto 1 se não especificado
        self.produtos_no_carrinho.append(produto)
        self.atualizar_carrinho()

    def atualizar_carrinho(self):
        self.carrinho_listbox.delete(0, tk.END)
        for produto in self.produtos_no_carrinho:
            self.carrinho_listbox.insert(tk.END, f"{produto.nome} - R${produto.preco:.2f}")
        self.atualizar_total()

    def atualizar_total(self):
        total = sum(p.preco for p in self.produtos_no_carrinho)
        self.total_label.config(text=f"Total: R${total:.2f}")

    def finalizar_compra(self):
        try:
            desconto = float(self.desconto_entry.get())
        except ValueError:
            desconto = 0
        
        total = sum(p.preco for p in self.produtos_no_carrinho)
        total_com_desconto = total - desconto

        if total_com_desconto < 0:
            total_com_desconto = 0
        
        mensagem = f"Total: R${total:.2f}\nDesconto: R${desconto:.2f}\nTotal com desconto: R${total_com_desconto:.2f}"
        
        messagebox.showinfo("Compra Finalizada", mensagem)
        self.produtos_no_carrinho.clear()
        self.carrinho_listbox.delete(0, tk.END)
        self.total_label.config(text="Total: R$0.00")
        self.desconto_entry.delete(0, tk.END)

# Configurando a janela principal
if __name__ == "__main__":
    root = tk.Tk()
    pdv = PDV(root)
    root.mainloop()
