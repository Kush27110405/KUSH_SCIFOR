# you have a class bank. It is able to withdraw money and deposit money after verifying PIN.
class Bank:
  def __init__(self,pin,balance):
    self.__pin = pin
    self.__balance = balance

  def verify_pin(self,pin):
    if not(isinstance(pin,int)):
      return False
    elif pin == self.__pin:
      return True
    else:
      return False

  def display_balance(self):
    pin = int(input("Enter PIN: "))
    if self.verify_pin(pin):
      print("PIN Verified!")
      print(f"Balance: {self.__balance}")
    else:
      print("Invalid PIN")
  
  def withdraw(self):
    pin = int(input("Enter PIN: "))
    
    if self.verify_pin(pin):
      print("PIN Verified!")
      print(f"Current balance: {self.__balance}")
      amount = float(input("Enter amount to withdraw: "))
      if amount <= self.__balance:
        self.__balance -= amount
        print(f"Amount withdrawn: {amount}")
        check_balance = input("Do you want to check the balance? (yes/no): ")
        if check_balance.lower() == "yes":
          print(f"Updated Balance : {self.__balance}")
      else:
        print("Insufficient balance")
    else:
      print("Invalid PIN")

  def deposit(self):
    pin = int(input("Enter PIN: "))
   
    if self.verify_pin(pin):
      print("PIN Verified!")
      print(f"Current balance: {self.__balance}")
      amount = float(input("Enter amount to deposit: "))
      self.__balance += amount
      print(f"Amount deposited: {amount}")
      check_balance = input("Do you want to check the balance? (yes/no): ")
      if check_balance.lower() == "yes":
        print(f"Updated Balance : {self.__balance}")
    else:
      print("Invalid PIN")

bank = Bank(1234,1000)
bank.withdraw()
bank.deposit()
bank.display_balance()

"""
Sample output:- 
Enter PIN: 1234
PIN Verified!
Current balance: 1000
Enter amount to withdraw: 500
Amount withdrawn: 500.0
Do you want to check the balance? (yes/no): yes
Updated Balance : 500.0
Enter PIN: 1234
PIN Verified!
Current balance: 500.0
Enter amount to deposit: 200
Amount deposited: 200.0
Do you want to check the balance? (yes/no): yes
Updated Balance : 700.0
Enter PIN: 1234
PIN Verified!
Balance: 700.0
"""
