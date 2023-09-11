import tkinter as tk

def press(key):
    entry.insert(tk.END, key)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")

def clear():
    entry.delete(0, tk.END)

# Configurar a janela principal
root = tk.Tk()
root.title("Calculadora")

# Entrada de texto
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Botões
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 1, 0
for button_text in buttons:
    tk.Button(root, text=button_text, width=5, command=lambda key=button_text: press(key) if key != '=' else calculate()).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Botão de limpar
tk.Button(root, text='C', width=5, command=clear).grid(row=row, column=col)

# Iniciar a interface gráfica
root.mainloop()