import tkinter as tk
from tkinter import messagebox

# Função para verificar as credenciais de login
def verificar_login():
    email = email_entry.get()
    senha = senha_entry.get()
    
    if len(senha) < 6:
        messagebox.showerror("Erro", "A senha deve ter 6 dígitos ou mais")
    elif "@" not in email:
        messagebox.showerror("Erro", "O email deve conter o caractere '@'")
    else:
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")

# Criar a janela principal
janela = tk.Tk()
janela.title("Tela de Login")

# rótulo de email
email_label = tk.Label(janela, text="E-mail:")
email_label.pack()

# campo de entrada de email
email_entry = tk.Entry(janela)
email_entry.pack()

# rótulo de senha
senha_label = tk.Label(janela, text="Senha:")
senha_label.pack()

# campo de entrada de senha
senha_entry = tk.Entry(janela, show="*")  # a senha será exibida como asteriscos
senha_entry.pack()

# botão de login
login_button = tk.Button(janela, text="Login", command=verificar_login)
login_button.pack()

# Executar a janela principal
janela.mainloop()
