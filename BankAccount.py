
class BankAc:

    _CurBalance = None
    _AcNo = None

    def __init__(self,no,initialAmount):
        self._CurBalance = initialAmount
        self._AcNo = no
        print("Congratulations your account is created")
    def displayAcBalance(self):
        print(str(self._AcNo) + " " + " Current balance is " + " " + str(self._CurBalance))

    def depositBalance(self, amount):
        self._CurBalance += amount
        print(str(amount) + " " + "deposited into the account " +" " + str(self._AcNo))

    def CheckAcBalance(self,amount):
        if self._CurBalance < amount:
            return False
        else:
            return True
    def withdraw(self, amount):
        if self.CheckAcBalance(amount):
            self._CurBalance -= amount
            print(str(amount) + " " + "Withdraw from account" + " " + str(self._AcNo))
        else:
            print(" " + "insufficient balance" + " " + str(self._AcNo))

    def transfer(self, amount,BankAc):
        self.withdraw(amount)
        BankAc.depositBalance(amount)