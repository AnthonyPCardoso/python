import tkinter as tk

def converter():
    try:
        centimetros = float(entrada_cm.get())
        metros = centimetros / 100
        resultado.set(f"{centimetros} cm é igual a {metros} m")
    except ValueError:
        resultado.set("Entrada inválida")


janela = tk.Tk()
janela.title("Conversor de Centímetros para Metros")


entrada_cm = tk.Entry(janela)
resultado = tk.StringVar()
resultado.set("Resultado aparecerá aqui")


rotulo_cm = tk.Label(janela, text="Centímetros:")
rotulo_resultado = tk.Label(janela, textvariable=resultado)
botao_converter = tk.Button(janela, text="Converter", command=converter)


rotulo_cm.pack()
entrada_cm.pack()
botao_converter.pack()
rotulo_resultado.pack()


janela.mainloop()
