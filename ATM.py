"""
    ATM.py
"""

class ATM:
    serial_number = 0
    transaction = []
    
    def __init__(self, serial_number=None):
        if serial_number is None:
            ATM.serial_number ++ 1
            self.serial_number = ATM.serial_number + 1
        else:
            self.serial_number = serial_number
            ATM.serial_number = self.serial_number

    def deposit(self, account, amount):
        account.current_balance += amount
        self.transaction.append(f"Deposit: {amount} to Account {account.account_number}")
        print("Deposit Complete")

    def withdraw(self, account, amount):
        if account.current_balance >= amount:
            account.current_balance -= amount
            self.transaction.append(f"Withdraw: {amount} from Account {account.account_number}")
            print("Withdraw Complete")
        else:
            print ("Insufficient Balance")

    def check_current_balance(self, account):
      print(f"Current Balance: {account.current_balance}")

    def view_transaction_summary(self):
        print("\nTransaction Summary:")
        for transaction in self.transaction:
            print(transaction)