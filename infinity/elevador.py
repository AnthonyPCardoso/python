class Elevador:
    def __init__(self, totalCapacidade, totalAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = 0
        self.totalAndar = totalAndar
        self.atualAndar = 0

    def Subir(self):
        if self.atualAndar < self.totalAndar:
            self.atualAndar += 1
            print("Subindo")
        else:
            print("VOCÊ ESTÁ NO ANDAR MAIS ALTO!")

    def Descer(self):
        if self.atualAndar > 0:
            self.atualAndar -= 1
            print("Descendo")
        else:
            print("VOCÊ JÁ ESTÁ NO TÉRREO!")

    def Entrar(self):
        if self.atualCapacidade < self.totalCapacidade:
            self.atualCapacidade += 1
            print("Entrando uma pessoa")
        else:
            print("O ELEVADOR ESTÁ CHEIO!")

    def Sair(self):
        if self.atualCapacidade > 0:
            self.atualCapacidade -= 1
            print("Saindo uma pessoa")
        else:
            print("NÃO TEM NINGUÉM")



elevador = Elevador(totalCapacidade=5, totalAndar=5)

while True:
    acao = input("Escolha ação (Subir, Descer, Entrar, Sair, fim): ").strip().lower()
    
    if acao == "subir":
        if elevador.atualAndar < elevador.totalAndar:
            elevador.Subir()
        else:
            print("VOCÊ ESTÁ NO ANDAR MAIS ALTO!")
    elif acao == "descer":
        if elevador.atualAndar > 0:
            elevador.Descer()
        else:
            print("VOCÊ JÁ ESTÁ NO TÉRREO!")
    elif acao == "entrar":
        elevador.Entrar()
    elif acao == "sair":
        elevador.Sair()
    elif acao == "fim":
        break
    else:
        print("Ação inválida. Escolha entre Subir, Descer, Entrar, Sair ou fim.")