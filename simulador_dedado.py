import random
import PySimpleGUI
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor?'
        # Layout n ta sendo lido
        layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'),sg.Button('Não')]
        ]
        
    def Iniciar(self):
        # Create a Windows
        janela = sg.Window('Simulador de Dado', layout=layout)
        # Ler os valores da tela
        self.eventos, self.valores = janela.Read()
        resposta = input(self.mensagem).upper()
        try:
            if resposta == "SIM" or resposta == 'S':
                self.GerarValorDoDado()
            elif resposta == "NÃO" or resposta == "N":
                print("Ok,Obrigado")
            else:
                print("Por favor,Digite Sim ou Não")
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))
    

simulador = SimuladorDeDado()
simulador.Iniciar()