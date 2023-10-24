import tkinter as tk



# def change_label_text():

#     label.config(text="Texto alterado!")



# root = tk.Tk()

# root.title("Janela de Exemplo")



# label = tk.Label(root, text="Olá!", font=("Arial", 16))

# label.pack()



# button = tk.Button(root, text="Alterar Texto", command=change_label_text)

# button.pack()



# root.mainloop()


root = tk.Tk()

root.title("Janela de Exemplo")

root.geometry("400x300")



label = tk.Label(root, text="Bem-vindo!", font=("Arial", 16))

label.pack()



button = tk.Button(root, text="Clique Aqui", padx=10, pady=5, bg="blue", fg="white")

button.pack()


root.mainloop()