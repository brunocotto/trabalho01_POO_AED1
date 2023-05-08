from Computer import Computer

class Notebook(Computer):
    def __init__(self, model, color, price, batteryTime):
        super().__init__(model, color, price)
        self.__batteryTime = batteryTime
    
    def getInformations(self):
        informations = super().getInformations()
        return f"{informations}\nTempo de Bateria: {self.__batteryTime} horas"
    
    def register(self):
        print("Cadastro de Notebook realizado com sucesso.")
        print(self.getInformations())