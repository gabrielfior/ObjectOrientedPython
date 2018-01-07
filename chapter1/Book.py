class Book:
    def __init__(self, ISBN=None, authors=[], title=None, subject=None, DOS=None):
        self.ISBN = ISBN
        self.authors = authors
        self.title = title
        self.subject = subject
        self.DOS = DOS