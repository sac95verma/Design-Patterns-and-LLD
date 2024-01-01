from abc import ABC, abstractmethod

class IBasePizza(ABC):
    
    @abstractmethod
    def getPrice():
        pass