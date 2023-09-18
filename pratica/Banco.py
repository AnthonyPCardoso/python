class Banco:
    def __init__(self, cpf, nome, saldo):
        self.cpf = cpf
        self.nome = nome
        self.saldo = saldo
    

class conta_corrente(Banco):
    def __init__(self, cpf, nome, saldo, sacar=0):
        super().__init__(cpf, nome, saldo)
        self.sacar = sacar

    def abrir_c(self):
        self.sac = str(input("Conta corrente aberta,Deseja sacar?[S/N] ")).upper()
        while True:
            if self.sac == 'S':
                self.valor = float(input("Quando deseja sacar? R$"))
                self.total = self.saldo - self.valor
                if self.valor > self.saldo:
                    print("Você não tem essa quantia no banco.Tente outro valor")
                    continue
                print(f"Foi feito um saque de R${self.valor},o seu saldo atual é R${self.total}")
                break
            elif self.sac == 'N':
                print(f"Ok, {self.nome} Até a próxima")
                break
            else:
                print("ERRO,Algo foi digitado errado! ")
                continue


class conta_poupanca(Banco):
    def __init__(self, cpf, nome, saldo, juros=0):
        super().__init__(cpf, nome, saldo)
        self.juros = juros
    
    def abrir_p(self):
        print('Conta Poupança aberta!')
        self.juros = self.saldo + (self.saldo *  6/100)
        print(f"Com o juros de 6% ao ano, mantendo esse valor seu novo saldo será R${self.juros}")



nome = str(input("Qual o seu nome? "))
cpf = str(input("Seu CPF: "))
saldo = float(input("Deposito: "))

confi =str(input("Conta corrente ou Poupança?  [C/P] ")).upper()
if confi == "C":
    usuario = conta_corrente(cpf, nome, saldo)
    usuario.abrir_c()
elif confi == "P":
    usuario = conta_poupanca(cpf, nome, saldo)
    usuario.abrir_p()