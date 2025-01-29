"""
    main.py
"""
import Accounts
import ATM

Account1 = Accounts.Accounts(account_number=191105,account_firstname="Justin Rhey",
                             account_lastname="Monoy", current_balance = 1500,
                             address = "Caloocan City",
                             email ="rheymonoy@gmail.com")

print("Account1")
print(Account1.account_firstname)
print(Account1.account_lastname)
print(Account1.current_balance)
print(Account1.address)
print(Account1.email)

ATM1 = ATM.ATM(serial_number=1)
ATM1.withdraw(Account1, 750)
ATM1.check_current_balance(Account1)

print(f"\nATM Serial Number: {ATM1.serial_number}")

Account2 = Accounts.Accounts(account_number=132497, account_firstname="Mina",
                             account_lastname="Myoui", current_balance=5000,
                             address="Seoul, South Korea",
                             email="minaimnida37@gmail.com")

print("\nAccount2")
print(Account2.account_firstname)
print(Account2.account_lastname)
print(Account2.current_balance)
print(Account2.address)
print(Account2.email)

ATM2 = ATM.ATM(serial_number=2)
ATM2.deposit(Account2, 2345)
ATM2.check_current_balance(Account2)

print(f"\nATM Serial Number: {ATM2.serial_number}")

ATM1.view_transaction_summary()




