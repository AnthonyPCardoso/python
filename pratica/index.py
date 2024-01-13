class Hero:
    ELO_MAP = {
        (0, 1000): "Ferro",
        (1001, 2000): "Bronze",
        (2001, 5000): "Prata Ouro",
        (5001, 8000): "Platina Diamante",
        (8001, 9000): "Ascendente",
        (9001, 10000): "Imortal",
        (10001, float('inf')): "Radiante"
    }

    def __init__(self, heroname, xp, elo=0):
        self.heroname = heroname
        self.xp = xp
        self.elo = elo

    def avaliahero(self):
        for xp_range, elo in self.ELO_MAP.items():
            if xp_range[0] <= self.xp <= xp_range[1]:
                self.elo = elo
                break

    def mensagem(self):
        print(f'Olá herói {self.heroname}, seu elo é {self.elo}')


heroname = input("Qual seu nome de herói? ")
xp = float(input("Quanto de xp tem? "))
teste = Hero(heroname, xp)

teste.avaliahero()
teste.mensagem()


