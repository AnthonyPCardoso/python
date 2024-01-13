class JogadorRanqueado:
    def __init__(self, vitorias, derrotas):
        self.vitorias = vitorias
        self.derrotas = derrotas
        self.saldo_ranked = self.calcular_saldo_ranked()
        self.resultado_ranked = self.definir_resultado_ranked()

    def calcular_saldo_ranked(self):
        return self.vitorias - self.derrotas

    def definir_resultado_ranked(self):
        if self.vitorias < 10:
            return "Ferro"
        elif 11 <= self.vitorias <= 20:
            return "Bronze"
        elif 21 <= self.vitorias <= 50:
            return "Prata"
        elif 51 <= self.vitorias <= 80:
            return "Ouro"
        elif 81 <= self.vitorias <= 90:
            return "Diamante"
        elif 91 <= self.vitorias <= 100:
            return "Lendário"
        elif self.vitorias >= 101:
            return "Imortal"
        else:
            return "Resultado indefinido"


jogador = JogadorRanqueado(vitorias=70, derrotas=20)

print(f"Saldo de Ranqueadas: {jogador.saldo_ranked}")
print(f"Resultado Ranqueado: {jogador.resultado_ranked}")
