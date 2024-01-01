from fileSystem.directory import Directory
from fileSystem.file import File

def printFileStructure(rootDirectory):
    return rootDir.ls()

def initiateAdditionOfFiles():
    directory = Directory('dir1')
    file1 = File('f1')
    file2 = File('f2')
    directory.add([file1, file2])

    dir2 = Directory('dir2')
    f3 = File('f3')
    dir2.add([f3])
    f4 = File('f4')
    directory.add([dir2])
    directory.add([f4])
    
    return directory

if __name__ == '__main__':
    rootDir = initiateAdditionOfFiles()
    printFileStructure(rootDir)