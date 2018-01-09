class OddContainer:
    def __contains__(self, item):
        if not isinstance(item, int) or not x % 2:
            return False
        return True
