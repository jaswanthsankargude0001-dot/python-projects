PIN = '1430'
balance = 10000

def credit(amount):
    global balance
    balance += amount
    print('''
Congratulations!
Your amount has been successfully credited to your account.
''')
    print(f"Your account balance after credit is: ₹ {balance}")

def debit(amount):
    global balance
    if balance < amount:
        print("Insufficient funds.")
    else:
        balance -= amount
        print('''
Congratulations!
Your amount has been successfully debited from your account.
''')
        print(f"Your account balance after debit is: ₹ {balance}")

def bal():
    print(f"Your current balance is: ₹ {balance}")

# Start of the program
bankbook = input("Insert your Passbook/Enter Bank Name: ")

# PIN check with retry loop
while True:
    pin = input("Enter your PIN: ")
    if pin == PIN:
        break
    else:
        print("❌ Invalid PIN! Please try again.\n")

# Main menu loop
while True:
    print('''
1. Credit Amount
2. Debit Amount
3. Balance
4. Mini Statement
5. Exit
''')

    try:
        option = int(input("Enter Your Option: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if option == 1:
        try:
            cred_amount = float(input("Enter Your Credit Amount: ₹ "))
            credit(cred_amount)
        except ValueError:
            print("Invalid amount entered.")
    elif option == 2:
        try:
            debit_amount = float(input("Enter Your Debit Amount: ₹ "))
            debit(debit_amount)
        except ValueError:
            print("Invalid amount entered.")
    elif option == 3:
        bal()
    elif option == 4:
        print("*** Mini Statement ***")
        print(f"Bank: {bankbook}")
        print(f"Balance: ₹ {balance}")
    elif option == 5:
        print("Thank you for banking with us. Goodbye!")
        break
    else:
        print("Invalid Option. Please try again.")