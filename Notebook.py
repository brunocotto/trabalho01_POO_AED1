from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria
    
    def getInformacoes(self):
        informacoes = super().getInformacoes()
        return f"{informacoes}\nTempo de Bateria: {self.__tempoDeBateria} horas"
    
    def cadastrar(self):
        print("Cadastro de Notebook realizado com sucesso!")
        print(self.getInformacoes())