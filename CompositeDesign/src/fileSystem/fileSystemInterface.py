from abc import ABC, abstractmethod

class IFileSystem(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def ls(self):
        pass

    def add(self):
        pass