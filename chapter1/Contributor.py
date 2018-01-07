class Contributor:
    def __init__(self, name=None):
        self.name = name

class ContributorWithType(Contributor):
    def __init__(self, name=None, type = None):
        super(name)
        self.type = type