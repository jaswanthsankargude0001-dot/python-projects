
while True:
    print("*" * 10, 'Welcome to union Bank', "*" * 10)
    print('''Which function do you want to use from below:
    1) Open new account
    2) Withdraw
    3) Deposit
    4) Check balance
    5) Exit''')

    try:
        option = int(input('Enter the number of the option you want to select: '))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if option == 1:
        try:
            noc = int(input('Number of customers to register: '))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if noc > 5:
            print("The number of registrations exceeded the maximum limit.")
        else:
            for i in range(noc):
                name = input('Enter your name: ')
                pin = input('Enter a 4-digit PIN: ')
                if len(pin) != 4 or not pin.isdigit():
                    print("Invalid PIN. Must be 4 digits.")
                    continue
                try:
                    deposit = float(input("Enter the amount you want to deposit: "))
                except ValueError:
                    print("Invalid amount.")
                    continue

                customername.append(name)
                customerpin.append(pin)
                customerbalance.append(deposit)

                print("\nAccount successfully created!")
                print("Name:", name)
                print("PIN:", pin)
                print("Balance:", deposit)
                print("&" * 10, 'New account successfully created', "&" * 10)
                print("Note! Please remember your Name and PIN.\n")

    elif option == 2:
        name = input('Enter your name: ')
        pin = input('Enter your PIN: ')
        if name in customername:
            index = customername.index(name)
            if pin == customerpin[index]:
                print("Your current balance is:", customerbalance[index])
                try:
                    amount = float(input('Enter the amount you want to withdraw: '))
                except ValueError:
                    print("Invalid amount.")
                    continue

                if amount > customerbalance[index]:
                    print("Insufficient balance.")
                else:
                    customerbalance[index] -= amount
                    print("Withdrawal successful.")
                    print("Your updated balance is:", customerbalance[index])
            else:
                print("Incorrect PIN.")
        else:
            print("Name not found.")

    elif option == 3:
        name = input('Enter your name: ')
        pin = input('Enter your PIN: ')
        if name in customername:
            index = customername.index(name)
            if pin == customerpin[index]:
                print("Your current balance is:", customerbalance[index])
                try:
                    deposit = float(input('Enter the amount you want to deposit: '))
                except ValueError:
                    print("Invalid amount.")
                    continue
                customerbalance[index] += deposit
                print("Deposit successful.")
                print("Your updated balance is:", customerbalance[index])
            else:
                print("Incorrect PIN.")
        else:
            print("Name not found.")

    elif option == 4:
        name = input('Enter your name: ')
        pin = input('Enter your PIN: ')
        if name in customername:
            index = customername.index(name)
            if pin == customerpin[index]:
                print("Your current balance is:", customerbalance[index])
            else:
                print("Incorrect PIN.")
        else:
            print("Name not found.")

    elif option == 5:
        print("Thank you for visiting Naresh Bank.")
        print("Goodbye!")
        break

    else:
        print("Invalid option selected. Please try again.")