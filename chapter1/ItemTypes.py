import abc

from chapter1.LibraryItem import LibraryItem


class CD(LibraryItem):

    def __init__(self, title=None, UPC=None, subject=None, contributors=[]):
        super(title, UPC, subject, contributors)
        self.artists = contributors

    def locate(self):
        pass


class Magazine(LibraryItem):

    def __init__(self, title=None, UPC=None, subject=None, contributors=[], volume=None, issue=None):
        super(title, UPC, subject, contributors)
        self.volume = volume
        self.issue = issue
        self.editors = contributors

    def locate(self):
        pass

class DVD(LibraryItem):

    def __init__(self, title=None, UPC=None, subject=None, genre=None, actors=[], directors=[]):

        contributors = [i for i in actors.extend(directors)]

        super(title, UPC, subject, contributors)
        self.genre = genre
        self.actors = actors
        self.directors = directors

    def locate(self):
        pass
