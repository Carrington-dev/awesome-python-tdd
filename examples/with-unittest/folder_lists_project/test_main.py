import os
import unittest
from main import Folder, File

class TestFolder(unittest.TestCase):
    def setUp(self):
        self.folder = Folder()
    
    def tearDown(self):
        self.folder = None

    
    def test_folder_path_not_none(self):
        self.assertIsNotNone(self.folder.path)

    def test_default_folder_path(self):
        current_path = "."
        self.assertEqual(current_path, self.folder.path)

    def test_getting_current_folder_files(self):
        current_folder_files = [
            "test_main.py",  "practice.py","main.py",
        ][::-1]
        self.assertListEqual(current_folder_files, self.folder.get_files("."))

    def test_getting_all_files_in_a_path(self):
        # path = "tests"
        # self.assertListEqual([], self.folder.get_all_sub_folders(path))
        self.assertEqual(8, len(self.folder.list_files_walk()))

    def test_getting_current_folder_sub_folders(self):
        current_folder_files = ['.vscode', 'tests', '__pycache__']
        self.assertEqual(current_folder_files, self.folder.get_sub_folders("."))

    def test_given_path_is_not_a_file(self):
        self.assertEqual(self.folder.is_folder("tests"), True)

    def test_given_path_is_a_file(self):
        self.assertEqual(self.folder.is_file("main.py"), True)

    def test_getting_files_in_all_child_folders(self):
        current_folder_and_sub_folders_files = ['main.py', 'practice.py', 'test_main.py']
        self.assertEqual(current_folder_and_sub_folders_files, self.folder.get_all_files("."))

    def test_get_all_files(self):
        self.assertEqual([], self.folder.all_files)

    def test_get_all_sub_folders(self):
        self.assertEqual([], self.folder.all_sub_folders)

    def test_if_path_exists(self):
        file_path = "main.py"
        self.assertEqual(True, os.path.exists(file_path))


class TestFile(unittest.TestCase):
    def setUp(self):
        self.file = File("main.py")

    def tearDown(self):
        self.file = None

    def test_file_name(self):
        self.assertIsNotNone(self.file.name)

    def test_path_name_is_a_file(self):
        self.assertEqual(self.file.is_file("main.py"), True)

    def test_path_name_not_a_file(self):
        self.assertEqual(self.file.is_file("tests"), False)

if __name__ == "__main__":
    unittest.main()
    
