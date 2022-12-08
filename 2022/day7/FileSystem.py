class Folder:
    def __init__(self, parent, name: str):
        self.subfolders: list[Folder] = []
        self.size = 0
        self.parent = parent
        self.name = name
    
    def addFolder(self, name: str):
        newFolder = Folder(self, name)
        self.subfolders.append(newFolder)
    
    def addFile(self, size: int):
        self.size += size

        f = self
        while(f.parent):
            f.parent.size += size
            f = f.parent
    
    def findFolder(self, name: str):
        return next((f for f in self.subfolders if f.name == name) , None)
    
    def __repr__(self) -> str:
        return f'{self.name} (size: {self.size})'

class FileSystem:
    def __init__(self):
        self.curFolder: Folder = None
        self.rootFolder = Folder(None, '/')
        self.command = ''
    
    def interpretLine(self, line: str):
        if line.startswith('$'):
            self.__executeCommand(line[2:])
        elif self.command == 'ls':
            self.__parseLsResult(line)
    
    def changeDir(self, dir: str):
        if dir == "/":
            self.curFolder = self.rootFolder
        elif dir == '..':
            self.curFolder = self.curFolder.parent
        else:
            self.curFolder = self.curFolder.findFolder(dir)

    def traverseFolders(self, parentFolder: Folder = None):
        if parentFolder == None:
            parentFolder = self.rootFolder

        yield parentFolder

        for child in parentFolder.subfolders:
            yield from self.traverseFolders(child)
    
    def __executeCommand(self, cmd: str):
        (cmd, *params) = cmd.split(' ')
        self.command = cmd
        
        if cmd == "cd":
            self.changeDir(params[0])
    
    def __parseLsResult(self, line: str):
        (sizeOrDir, name) = line.split(' ')
        if sizeOrDir == 'dir':
            self.curFolder.addFolder(name)
        else:
            self.curFolder.addFile(int(sizeOrDir))