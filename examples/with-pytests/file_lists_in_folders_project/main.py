class FolderLists:
    def __init__(self):
        self.folders: list[Folder] = []
        self.files: list[str] = []

    def add_folder(self, folder: Folder):
        self.folders.append(folder)

class Folder:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.subfolders = []
    
    
    
