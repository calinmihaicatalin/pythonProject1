def show_balance(balance):
    print(f"Your balance is {balance:.2f} E")

def deposit():
    while True:
        amount_input = input("Enter an amount to be deposited: ")
        try:
            amount = float(amount_input)
            if amount < 0:
                print("This isn't a valid amount!")
            else:
                print(f"You deposited the following amount: {amount:.2f}")
                return amount
        except ValueError:
            print("Please enter a valid input!")

def withdraw(balance):
    while True:
        amount_input = input("Enter the amount to withdraw: ")
        try:
            amount = float(amount_input)
            if amount > balance:
                print("Insufficient funds!")
                return False
            elif amount < 0:
                print("Please enter a valid input!")
            else:
                print(f"The following amount has been withdrawn: {amount:.2f}")
                return amount
        except ValueError:
            print("Please enter a valid input!")

def main():
    balance = 0
    is_running = True

    while is_running:
        print("***********************")
        print("    Banking Program    ")
        print("***********************")
        print()
        print("Press 1 to show balance")
        print("Press 2 to deposit money")
        print("Press 3 to withdraw money")
        print("Press 4 to exit")
        user_input = input("Please enter your option: ")
        match user_input:
            case '1':
                show_balance(balance)
            case '2':
                balance += deposit()
            case '3':
                balance -= withdraw(balance)
            case '4':
                is_running = False
            case _:
                print("This is not a valid option")
    print("Thank you~ Have a nice day!")
if __name__ == '__main__':
    main()