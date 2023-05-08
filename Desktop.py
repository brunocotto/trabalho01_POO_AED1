from Computer import Computer

class Desktop(Computer):
    def __init__(self, model, color, price, sourcePower):
        super().__init__(model, color, price)
        self.sourcePower = sourcePower
    
    def getInformations(self):
        informations = super().getInformations()
        return f"{informations}\nPotência da Fonte: {self.sourcePower}W"
    
    def register(self):
        print("Cadastro de Desktop realizado com sucesso.")
        print(self.getInformations())