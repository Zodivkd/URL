card = input("insert your card.\n")
pin_number =123
atm_balance = 1000
if card == "inserted":
    pin = input("Please Enter your pin.\n")
    if pin_number == 123:
        print("Access Granted. Please select an option.")
        option = "withdrawal\nDeposit\ncheck balance"
        print(option)
        selection = input("Select an option.\n")
        if selection == "withdrawal":
            if atm_balance<=1000:
                print("please take your cash")
            else:
                print("insufficient funds.")
        elif selection == "Deposit":
                print("your deposit has been accepted")
        elif selection == "check balance":
            print(f"your current balance is {atm_balance}.")
        else:
            print("Invalid selection. please try again")
    else:
        print("incorrect pin")
else:
    print("No card dedected. Please insert your card.")
    
            
                