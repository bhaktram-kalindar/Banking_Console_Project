from BankAccount import BankAc


class CurrentAc(BankAc):

    def __init__(self, no, initialAmount):
        super().__init__(no, initialAmount)
        print("Congratulation your current account is created" + " " + str(self._AcNo))

    def CurrentAcWithdraw (self, amount):
        amount += 200
        print(" " + "200 Rs charge for every withdraw" + " ")
        self.withdraw(amount)