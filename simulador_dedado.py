import random
import PySimpleGUI
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor?'
        # Layout n ta sendo lido
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'),sg.Button('Não')]
        ]
        
    def Iniciar(self):
        # Create a Windows
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.read()
        
        try:
            if self.eventos == "Sim" or self.eventos == 'S':
                self.GerarValorDoDado()
            elif self.eventos == "Não" or self.eventos == "N":
                print("Ok,Obrigado")
            else:
                print("Por favor,Digite Sim ou Não")
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))
    

simulador = SimuladorDeDado()
simulador.Iniciar()