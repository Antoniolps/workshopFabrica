from abc import ABC, abstractmethod

class IAnimal(ABC):

    @abstractmethod
    def falar(self):
        """Defina na classe filha"""

    @abstractmethod
    def andar(self):
        """Defina na classe filha"""

class Cachorro(IAnimal):
    def falar(self):    
        print("Au Au Au")
    
    def andar(self):
        print("Andando")


class Pessoa:

    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self.idade = idade
        self.__humano = True

    def fala_pessoa(self):
        print("Falando")

    def mostra_nome(self):
        print(self._nome)

pingo = Cachorro()
pingo.falar()
pingo.andar()

humano = Pessoa("Antonio", 23)
humano.fala_pessoa()
humano.mostra_nome()

