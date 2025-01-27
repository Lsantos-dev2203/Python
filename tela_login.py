import tkinter as tk
from tkinter import messagebox

# Função para verificar o login
def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    
    if usuario == "admin" and senha == "1234":
        janela_login.destroy()  # Fecha a janela de login
        abrir_menu_inicial()   # Abre o menu inicial
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

# Função para o menu inicial
def abrir_menu_inicial():
    menu = tk.Tk()
    menu.title("Menu Inicial")
    menu.geometry("300x200")

    # Opções do menu
    tk.Label(menu, text="Bem-vindo ao Menu Inicial!", font=("Arial", 14)).pack(pady=10)

    tk.Button(menu, text="Opção 1", command=lambda: messagebox.showinfo("Opção 1", "Você selecionou a Opção 1")).pack(pady=5)
    tk.Button(menu, text="Opção 2", command=lambda: messagebox.showinfo("Opção 2", "Você selecionou a Opção 2")).pack(pady=5)
    tk.Button(menu, text="Sair", command=menu.destroy).pack(pady=20)

    menu.mainloop()

# Criando a janela de login
janela_login = tk.Tk()
janela_login.title("Tela de Login")
janela_login.geometry("300x200")

# Rótulos e entradas para o login
tk.Label(janela_login, text="Usuário:").pack(pady=5)
entrada_usuario = tk.Entry(janela_login)
entrada_usuario.pack()

tk.Label(janela_login, text="Senha:").pack(pady=5)
entrada_senha = tk.Entry(janela_login, show="*")
entrada_senha.pack()

# Botões para login e sair
tk.Button(janela_login, text="Login", command=verificar_login).pack(pady=10)
tk.Button(janela_login, text="Sair", command=janela_login.destroy).pack()

# Iniciando o loop da janela de login
janela_login.mainloop()
