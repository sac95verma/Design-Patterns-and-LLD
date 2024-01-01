from .fileSystemInterface import IFileSystem
from icecream import ic

class File(IFileSystem):

    def __init__(self, name):
        self.name = name

    def ls(self):
        ic(self.name)
