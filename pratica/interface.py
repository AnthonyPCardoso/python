import tkinter as tk
from tkinter import *
from tkinter import filedialog

#cores
cor1 = "#060807" # black
cor2 = "#feffff" # white
cor3 = "#38576b" # BLue
cor4 = "#ECEFF1" # Gray
cor5 = "#FFAB40" # Orange



janela = Tk()
janela.title("Lista Telefônica")
janela.geometry("310x300")
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)

#Dividindo as janela..
frame_top = Frame(janela, width=310, height=50, bg=cor3, relief='flat')
frame_top.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_bottom = Frame(janela, width=310, height=250, bg=cor2, relief='flat')
frame_bottom.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#Configurando os frame acima.....

l_nome = Label(frame_top, text="Lista Telefônica", anchor=NE, font=('Ivy 25'), bg=cor3, fg=cor1)
l_nome.place(x=5, y=5)

l_linha = Label(frame_top, text='', width=275, anchor=NW, font='Ivy 1', bg=cor1, fg=cor1)
l_linha.place(x=10, y=45)

#configurando os frames de baixo.....
l_nome = Label(frame_bottom, text="Nome *", anchor=NW, font=('Ivy 13'), bg=cor2, fg=cor1)
l_nome.place(x=10,y=20)
e_nome = Entry(frame_bottom, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_nome.place(x=14, y=50)

l_pass = Label(frame_bottom, text="Telefone *", anchor=NW, font=('Ivy 13'), bg=cor2, fg=cor1)
l_pass.place(x=10,y=95)
e_pass = Entry(frame_bottom, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_pass.place(x=14, y=130)

b_confirmar = Button(frame_bottom, text="Cadastrar", width=39, height=3,  font=('Ivy 8 bold'), bg=cor5, fg=cor1, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=15,y=180)


# parte do FileDialog

class Tela:
    def __init__(self, master):

        self.mhtela = master
        self.barra_menu = tk.Menu(self.mhtela)
        self.mhtela.config(menu = self.barra_menu)

        self.barra_menu.add_command(Label="Salvar", command=self.salvar)
        self.barra_menu.add_command(label="Salvar no diretório...")
    
    def salvar(self):
        self.arquivo = filedialog.asksaveasfile(mode= "w")



Tela(janela)
janela.mainloop() #Mantém janela aberta