import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


# Função para salvar os dados em um arquivo
def salvar_contato():
    nome = nome_entry.get()
    telefone = telefone_entry.get()

    # Verifica se um arquivo já foi criado
    if 'contatos.txt' not in contatos_criados:
        arquivo = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])
        if arquivo:
            contatos_criados.add('contatos.txt')
    else:
        arquivo = open('contatos.txt', 'a')

    if arquivo:
        arquivo.write(f"Nome: {nome}, Telefone: {telefone}\n")
        arquivo.close()
        nome_entry.delete(0, tk.END)
        telefone_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Não foi possível criar o arquivo.")

# Configuração da janela principal
root = tk.Tk()
root.title("Cadastro de Contatos")
root.geometry("230x300")

# Variável de controle para verificar se um arquivo já foi criado
contatos_criados = set()

# Widgets da interface
nome_label = tk.Label(root, text="Nome:")
nome_label.pack()

nome_entry = tk.Entry(root, width=30)
nome_entry.pack()

telefone_label = tk.Label(root, text="Telefone:")
telefone_label.pack()

telefone_entry = tk.Entry(root, width=30)
telefone_entry.pack()

cadastrar_button = tk.Button(root, text="Cadastrar", command=salvar_contato)
cadastrar_button.pack()

root.mainloop()
