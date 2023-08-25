from BankAccount import BankAc
class SavingAc(BankAc):
    __Ac = None

    def __init__(self, no, initialAmount):
        super().__init__(no, initialAmount)
        print("Congratulation for opening of saving bank account" + " " + str(self._AcNo))

    def savingAcDeposit(self, amount):
        interest = amount * 3 / 100
        amount += interest

        print(str(interest) + " interest added " + " ")
        self.depositBalance(amount)