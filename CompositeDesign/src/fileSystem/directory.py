from .fileSystemInterface import IFileSystem

class Directory(IFileSystem):

    def __init__(self, name):
        self.files = []
        self.name = name

    def add(self, filesList: list[IFileSystem]):
        self.files.extend(filesList)
        return

    def ls(self):
        for file in self.files:
            print(f'Dir Name : {self.name}')
            file.ls()

