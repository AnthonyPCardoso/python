class info:
    def __init__(self, modelo, fabricante, processador, ram, tam_hd, espa_hd, ligado):
        self.modelo = modelo
        self.fabricante = fabricante
        self.processador  = processador
        self.ram = ram
        self.tam_hd = tam_hd
        self.espa_hd = espa_hd
        self.ligado = ligado
    
    def liga(self):
        self.ligado = True
        print("Ligado.")
    
    def desliga(self):
        self.ligado = False
        print("Desligando")

    
    def limparHD(self):
        self.usu = float(input("Deseja limpar quanto de HD? "))
        if self.usu <= self.espa_hd:
            self.tam_hd = self.espa_hd - self.usu
            print("Limpeza concluída")
            print(f"Seu HD agora tem {self.tam_hd}GB ")
        else:
            print("ERROR")
    
    def ocuparHD(self):
        self.usu2 = float(input("Deseja ocupar quanto do HD? "))
        self.conta = self.espa_hd + self.usu2
        if self.conta < self.tam_hd:
            self.tam_hd = self.conta
            print(f"Espaço ocupado: {self.tam_hd}")
        else:
            print("Você não tem armazenamento para isso.")


pc = info("Samsung", "550XBE/350XBE", "Intel Celeron", 4, 450, 318, False)
pc.liga()
p1 = input("Deseja fazer uma limpeza no HD?[S/N] ").upper()
if p1 == "S":
    pc.limparHD()
else:
    print("Ok")

p2 = input("Deseja ocupar o HD? [S/N]").upper()
if p2 == "S":
    pc.ocuparHD()
else:
    print("Ok")

pc.desliga()