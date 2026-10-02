# Bank Management System

accounts = {}


# Create Account
def create_account():
    print("\n========== CREATE ACCOUNT ==========")

    account_number = input("Enter account number: ")

    if account_number in accounts:
        print("Account already exists!")
        return

    name = input("Enter account holder name: ")
    age = int(input("Enter age: "))
    phone = input("Enter phone number: ")
    initial_deposit = float(input("Enter initial deposit: "))

    if initial_deposit < 0:
        print("Deposit amount cannot be negative.")
        return

    accounts[account_number] = {
        "name": name,
        "age": age,
        "phone": phone,
        "balance": initial_deposit,
        "transactions": [
            f"Account created with deposit: ₹{initial_deposit:.2f}"
        ]
    }

    print("\nAccount created successfully!")
    print("Account Number:", account_number)


# Deposit Money
def deposit_money():
    print("\n========== DEPOSIT MONEY ==========")

    account_number = input("Enter account number: ")

    if account_number not in accounts:
        print("Account not found!")
        return

    amount = float(input("Enter deposit amount: "))

    if amount <= 0:
        print("Enter a valid amount.")
        return

    accounts[account_number]["balance"] += amount

    accounts[account_number]["transactions"].append(
        f"Deposited: ₹{amount:.2f}"
    )

    print("Money deposited successfully!")
    print("Current Balance: ₹{:.2f}".format(
        accounts[account_number]["balance"]
    ))


# Withdraw Money
def withdraw_money():
    print("\n========== WITHDRAW MONEY ==========")

    account_number = input("Enter account number: ")

    if account_number not in accounts:
        print("Account not found!")
        return

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Enter a valid amount.")
        return

    balance = accounts[account_number]["balance"]

    if amount > balance:
        print("Insufficient balance!")
        return

    accounts[account_number]["balance"] -= amount

    accounts[account_number]["transactions"].append(
        f"Withdrawn: ₹{amount:.2f}"
    )

    print("Money withdrawn successfully!")
    print("Current Balance: ₹{:.2f}".format(
        accounts[account_number]["balance"]
    ))


# Check Balance
def check_balance():
    print("\n========== CHECK BALANCE ==========")

    account_number = input("Enter account number: ")

    if account_number not in accounts:
        print("Account not found!")
        return

    print("Account Holder:", accounts[account_number]["name"])
    print("Balance: ₹{:.2f}".format(
        accounts[account_number]["balance"]
    ))


# View Account Details
def account_details():
    print("\n========== ACCOUNT DETAILS ==========")

    account_number = input("Enter account number: ")

    if account_number not in accounts:
        print("Account not found!")
        return

    account = accounts[account_number]

    print("-----------------------------------")
    print("Account Number :", account_number)
    print("Account Holder :", account["name"])
    print("Age            :", account["age"])
    print("Phone Number   :", account["phone"])
    print("Balance        : ₹{:.2f}".format(account["balance"]))
    print("-----------------------------------")


# Transaction History
def transaction_history():
    print("\n========== TRANSACTION HISTORY ==========")

    account_number = input("Enter account number: ")

    if account_number not in accounts:
        print("Account not found!")
        return

    transactions = accounts[account_number]["transactions"]

    print("Account Holder:", accounts[account_number]["name"])
    print("-----------------------------------")

    for transaction in transactions:
        print(transaction)

    print("-----------------------------------")


# Main Menu
while True:

    print("\n==========================================")
    print("          BANK MANAGEMENT SYSTEM")
    print("==========================================")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Account Details")
    print("6. Transaction History")
    print("7. Exit")
    print("==========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        deposit_money()

    elif choice == "3":
        withdraw_money()

    elif choice == "4":
        check_balance()

    elif choice == "5":
        account_details()

    elif choice == "6":
        transaction_history()

    elif choice == "7":
        print("\nThank you for using Bank Management System!")
        break

    else:
        print("\nInvalid choice! Please enter 1 to 7.")