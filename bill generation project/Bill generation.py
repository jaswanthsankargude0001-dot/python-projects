from datetime import datetime

# Welcome and user input
name = input("Enter Your Name: ")

# Item list display
items = {
    'Rice': 200, 'Sugar': 30, 'Salt': 15, 'Oil': 95, 'Paneer': 50,
    'Ice cr': 35, 'Vegata': 50, 'Fruits': 70, 'Curd': 25,
    'Plastic': 50, 'Chips': 10
}

item_list = '''
Available Items:
----------------
Rice    Rs 200/kg
Sugar   Rs 30/kg
Salt    Rs 15/kg
Oil     Rs 95/kg
Paneer  Rs 50/kg
Ice cr  Rs 35/kg
Vegata  Rs 50/kg
Fruits  Rs 70/kg
Curd    Rs 25/kg
Plastic Rs 50/kg
Chips   Rs 10/-
'''

# Show item list if requested
option = input("Press 1 to see the list of items: ")
if option == '1':
    print(item_list)

# Main shopping loop
while True:
    pricelist = []
    Totalprice = 0

    while True:
        choice = input("Press 1 to buy, Press 2 to finish shopping: ")
        if choice == '2':
            break
        elif choice == '1':
            item = input("Enter the name of the item: ").strip()
            if item in items:
                try:
                    quantity = int(input("Enter quantity: "))
                    price = quantity * items[item]
                    pricelist.append((item, quantity, price))
                    Totalprice += price
                except ValueError:
                    print("Invalid quantity. Please enter a number.")
            else:
                print("Sorry, the item is out of stock.")
        else:
            print("Invalid input. Please try again.")

    # Billing confirmation
    if pricelist:
        confirm = input("Would you like to generate the bill? (yes/no): ").lower()
        if confirm == 'yes':
            gst = Totalprice * 0.05
            final_amount = Totalprice + gst

            print("\n" + "="*40)
            print(f"Customer Name: {name}")
            print(f"Date & Time  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("="*40)
            print(f"{'S.No':<5}{'Item':<10}{'Qty':<5}{'Price':>10}")
            print("-"*40)
            for idx, (item, qty, price) in enumerate(pricelist, start=1):
                print(f"{idx:<5}{item:<10}{qty:<5}{price:>10}")
            print("-"*40)
            print(f"{'Total':<20}{Totalprice:>10}")
            print(f"{'GST (5%)':<20}{gst:>10.2f}")
            print(f"{'Final Amount':<20}{final_amount:>10.2f}")
            print("="*40)
            print("Thank you for shopping with us!")

    else:
        print("No items were purchased.")

    # Ask if user wants to shop again
    again = input("Do you want to shop again? (yes/no): ").lower()
    if again != 'yes':
        print("Visit again! Have a great day!")
        break