class InvalidWithdrawalException(Exception):
    def __init__(self, amount=None, balance=None):
        super(InvalidWithdrawalException, self).__init__("account does not have ${}".format(amount))
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance