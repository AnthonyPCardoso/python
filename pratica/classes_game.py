class HeroiAventura:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == 'mago':
            ataque = 'Usou magia'
        elif self.tipo == 'guerreiro':
            ataque = 'Usou espada'
        elif self.tipo == 'monge':
            ataque = 'Usou artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'Usou shuriken'
        else:
            ataque = 'Ataque indefinido'

        mensagem_ataque = f"O {self.tipo} atacou usando {ataque}"
        print(mensagem_ataque)


tipo_heroi_escolhido = input("Escolha o tipo de herói (mago, guerreiro, monge, ninja): ").lower()

if tipo_heroi_escolhido not in ['mago', 'guerreiro', 'monge', 'ninja']:
    print("Tipo de herói inválido.")
else:

    nome_heroi = input("Digite o nome do herói: ")
    idade_heroi = int(input("Digite a idade do herói: "))
    heroi = HeroiAventura(nome=nome_heroi, idade=idade_heroi, tipo=tipo_heroi_escolhido)

    heroi.atacar()
