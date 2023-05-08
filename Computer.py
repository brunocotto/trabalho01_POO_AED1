# classe ABC do módulo abc para criar a classe abstrata
from abc import ABC, abstractmethod

class Computer(ABC):
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
    
    # retorna uma string formatada com os valores dos atributos
    def getInformations(self):
        return f"Modelo: {self.model}\nCor: {self.color}\nPreço: R${self.price:.2f}"
    
    # é definido como um método abstrato usando o decorator @abstractmethod
    # as classes derivadas devem implementar esse método
    @abstractmethod
    def register(self):
        pass