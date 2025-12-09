import os


class File:
    def __init__(self, name = None):
        self.name = name

    def is_file(self, path):
        return os.path.isfile(path)

class Folder:
    def __init__(self, path = "."):
        self.path = path
        self.all_files = []
        self.all_sub_folders = []

    def is_path_existing(self, path):
        return  os.path.exists(path)
    
    def is_folder(self, path):
        return os.path.isdir(path)
    
    def is_file(self, path):
        return os.path.isfile(path)
    
    def get_sub_folders(self, path):
        if os.path.exists(path):
            all_files = [ entry for entry in os.listdir(path) if os.path.isdir(entry)]
        return all_files
    
    def get_files(self, path):
        if os.path.exists(path):
            all_files = [ entry for entry in os.listdir(path) if os.path.isfile(entry)]
        return all_files
    
    def get_all_files(self, path):
        all_files =  []
        if os.path.exists(path):
            for entry in os.listdir(path):
                if os.path.isfile(entry):
                    all_files.append(entry)
                else:
                    self.get_all_files(entry)
        return all_files
    
    
    def list_files_walk(self):
        start_path = self.path

        for root, dirs, files in os.walk(start_path):
            for file in files:
                self.all_files.append(os.path.join(root, file))

        return self.all_files
    
    def get_all_sub_folders(self, path):
        all_folders =  []
        if os.path.exists(path):
            for entry in os.listdir(path):
                if os.path.isdir(entry):
                    all_folders.append(entry)
                else:
                    self.get_all_sub_folders(entry)
        return all_folders
    
    def get_all_sub_folders(self, path):
        all_folders =  []
        if os.path.exists(path):
            for entry in os.listdir(path):
                if os.path.isfile(entry):
                    all_folders.append(entry)
                else:
                    self.get_all_sub_folders(entry)
        return all_folders


"""
folder -> folder or file
"""