from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self.__potenciaDaFonte = potenciaDaFonte
    
    def getInformacoes(self):
        informacoes = super().getInformacoes()
        return f"{informacoes}\nPotência da Fonte: {self.__potenciaDaFonte}W"
    
    def cadastrar(self):
        print("Cadastro de Desktop realizado com sucesso!")
        print(self.getInformacoes())