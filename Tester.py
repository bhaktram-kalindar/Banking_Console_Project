from BankAccount import BankAc
from SavingAc import SavingAc
from CurrentAc import CurrentAc


b1 = BankAc(1112, 500)
b1.displayAcBalance()
b1.withdraw(200)
b1.depositBalance(700)
b1.displayAcBalance()

print("*************")


s1 = SavingAc(1111, 1000)
s1.displayAcBalance()
s1.savingAcDeposit(200)
s1.displayAcBalance()
s1.withdraw(400)

print("**************")

c1 = CurrentAc(1113, 100000)
c1.displayAcBalance()
c1.CurrentAcWithdraw(99800)
c1.displayAcBalance()

print("***************")

b2 = BankAc(1114, 3000)
b2.displayAcBalance()
b2.transfer(500, b1)
b1.displayAcBalance()
b2.displayAcBalance()