# classe ABC do módulo abc para criar a classe abstrata
from abc import ABC, abstractmethod

class Computador(ABC):
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
    
    # retorna uma string formatada com os valores dos atributos
    def getInformacoes(self):
        return f"Modelo: {self.modelo}\nCor: {self.cor}\nPreço: R${self.preco:.2f}"
    
    # é definido como um método abstrato usando o decorator @abstractmethod
    # as classes derivadas devem implementar esse método
    @abstractmethod
    def cadastrar(self):
        pass