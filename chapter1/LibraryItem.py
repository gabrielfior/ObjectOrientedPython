import abc


class LibraryItem:
    def __init__(self, title=None, UPC=None, subject=None, contributors=[]):
        self.title = title
        self.UPC = UPC
        self.subject = subject
        self.contributors = contributors

    @abc.abstractmethod
    def locate(self):
        print("Implement me!")
        pass

    @abc.abstractmethod
    def get_contributors(self):
        pass