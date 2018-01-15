class Inventory:
    def lock(self):
        """
        Select the type of item that is going to be manipulated. This method will lock the item so nobody else
        can manipulate the inventory until it is returned. This prevents selling the same item
        to two different customers
        :return:
        """
        pass

    def unlock(self):
        """
        Release the given type so that other customers can access it
        :return:
        """
        pass

    def purchase(self, item_type):
        """
        If the item is not locked, raise an exception. If the item type does not exist, raise an exception.
        If the item is currently out of stock, raise an exception.
        If the item is available, subtract one item and return the number of items left
        :param item_type:
        :return:
        """
        pass