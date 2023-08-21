import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor? '

    
    def Iniciar(self):
        resposta = input(self.mensagem).upper()
        if resposta == "SIM" or resposta == 'S':
            self.GerarValorDoDado()
        elif resposta == "NÃO" or resposta == "N":
            print("Ok,Obrigado")
        else:
            print("Por favor,Digite Sim ou Não")


    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))
    

simulador = SimuladorDeDado()
simulador.Iniciar()