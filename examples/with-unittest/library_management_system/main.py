class Library:
    """
    Docstring for Library

    The instance which represents the Library
    """
    def __init__(self, name):
        self.name = name
        self.reading_units = {}
        self.librarians = {}

class ReadingMaterialUnit:
    """
    Docstring for ReadingMaterialUnit
    
    """

    def __init__(self, title, author, year_published, isbn, typr_ = "book"):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.isbn = isbn
        self.type = typr_

    def __str__(self):
        return f"ReadingMaterialUnit({self.title=}, {self.author=}, {self.isbn=})"

reading_material_unit = ReadingMaterialUnit("New Maths", "author", "isbn", "year_published")
 
print(reading_material_unit)