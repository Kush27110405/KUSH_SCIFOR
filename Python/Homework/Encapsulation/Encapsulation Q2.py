"""
Encapsulation Q2 :- creating a class "BankAccount" to encapsulate the balance of the account.
"""
class BankAccount:
  def __init__(self,account_number,balance = 0):
    self.__account_number = account_number
    self.__balance = balance

  @property
  def account_number(self):
    return self.__account_number
  
  @property
  def balance(self):
    return self.__balance

  def deposit(self,amount):
    self.__balance += amount

  def withdraw(self,amount):
    if self.__balance >= amount:
      self.__balance -= amount
    else:
      print("Insufficient balance!")

my_BankAccount = BankAccount("123456")
print(my_BankAccount.account_number)
print(my_BankAccount.balance)

my_BankAccount.deposit(50000)
print(my_BankAccount.balance)

my_BankAccount.withdraw(20000)
print(my_BankAccount.balance)
