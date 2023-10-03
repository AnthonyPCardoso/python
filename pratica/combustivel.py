class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor_abastecido):
        litros_abastecidos = valor_abastecido / self.valorLitro
        if litros_abastecidos <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros_abastecidos
            return f"Abastecidos {litros_abastecidos:.2f} litros de {self.tipoCombustivel}."
        else:
            return "Quantidade insuficiente de combustível na bomba."

    def abastecerPorLitro(self, litros_abastecidos):
        valor_a_pagar = litros_abastecidos * self.valorLitro
        if litros_abastecidos <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros_abastecidos
            return f"Valor a pagar: R${valor_a_pagar:.2f}"
        else:
            return "Quantidade insuficiente de combustível na bomba."

    def alterarValor(self, novo_valor_litro):
        self.valorLitro = novo_valor_litro
        return f"Valor do litro de {self.tipoCombustivel} alterado para R${novo_valor_litro:.2f}."

    def alterarCombustivel(self, novo_tipo_combustivel):
        self.tipoCombustivel = novo_tipo_combustivel
        return f"Tipo de combustível alterado para {novo_tipo_combustivel}."

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade
        return f"Quantidade de combustível alterada para {nova_quantidade} litros."



bomba = BombaCombustivel("Gasolina", 4.50, 1000)

print(bomba.abastecerPorValor(50))  # Abastecer R$50.00 de gasolina
print(bomba.abastecerPorLitro(10))  # Abastecer 10.00 litros de gasolina
print(bomba.alterarValor(4.60))      # Alterar valor do litro para R$4.60
print(bomba.alterarCombustivel("Etanol"))  # Alterar tipo de combustível para Etanol
print(bomba.alterarQuantidadeCombustivel(800))  # Alterar quantidade de combustível para 800 litros
