import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from tkinter import ttk

class PDVApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema PDV")
        self.style = Style(theme="flatly")

        # Lista de produtos disponíveis
        self.products = {
            "Café": 5.00,
            "Chá": 3.50,
            "Sanduíche": 8.00,
            "Suco": 4.50,
        }

        # Carrinho de compras
        self.cart = []

        # Interface gráfica
        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=BOTH, expand=True)

        # Título
        title_label = ttk.Label(main_frame, text="Ponto de Venda", font=("Helvetica", 24), bootstyle="primary")
        title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Lista de produtos disponíveis
        product_label = ttk.Label(main_frame, text="Selecione o Produto:", font=("Helvetica", 14))
        product_label.grid(row=1, column=0, padx=5, pady=5)

        self.product_var = tk.StringVar()
        self.product_combobox = ttk.Combobox(main_frame, textvariable=self.product_var, values=list(self.products.keys()), state="readonly")
        self.product_combobox.grid(row=1, column=1, padx=5, pady=5)
        self.product_combobox.set("Café")

        # Quantidade
        qty_label = ttk.Label(main_frame, text="Quantidade:", font=("Helvetica", 14))
        qty_label.grid(row=2, column=0, padx=5, pady=5)

        self.qty_spinbox = ttk.Spinbox(main_frame, from_=1, to=100, width=5)
        self.qty_spinbox.grid(row=2, column=1, padx=5, pady=5)

        # Botão de adicionar ao carrinho
        add_button = ttk.Button(main_frame, text="Adicionar ao Carrinho", bootstyle="success", command=self.add_to_cart)
        add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Lista do carrinho
        self.cart_listbox = tk.Listbox(main_frame, height=10, width=50)
        self.cart_listbox.grid(row=4, column=0, columnspan=3, pady=10)

        # Total
        self.total_label = ttk.Label(main_frame, text="Total: R$ 0.00", font=("Helvetica", 16))
        self.total_label.grid(row=5, column=0, columnspan=3, pady=10)

        # Botão de finalizar compra
        checkout_button = ttk.Button(main_frame, text="Finalizar Compra", bootstyle="primary", command=self.checkout)
        checkout_button.grid(row=6, column=0, columnspan=3, pady=10)

    def add_to_cart(self):
        product = self.product_var.get()
        qty = int(self.qty_spinbox.get())
        price = self.products[product]
        total_price = price * qty

        cart_entry = f"{product} - {qty} x R$ {price:.2f} = R$ {total_price:.2f}"
        self.cart.append(total_price)
        self.cart_listbox.insert(tk.END, cart_entry)

        self.update_total()

    def update_total(self):
        total = sum(self.cart)
        self.total_label.config(text=f"Total: R$ {total:.2f}")

    def checkout(self):
        total = sum(self.cart)
        messagebox.showinfo("Compra Finalizada", f"Total da compra: R$ {total:.2f}\nObrigado pela preferência!")
        self.cart_listbox.delete(0, tk.END)
        self.cart.clear()
        self.update_total()

if __name__ == "__main__":
    root = tk.Tk()
    app = PDVApp(root)
    root.mainloop()
