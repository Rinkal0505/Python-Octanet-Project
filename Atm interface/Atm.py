class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. Current balance is ${self.balance}"
        else:
            return "Please enter a valid amount to deposit"

    def withdraw(self, amount):
        if self.balance >= amount > 0:
            self.balance -= amount
            return f"Withdrawn ${amount}. Current balance is ${self.balance}"
        elif amount <= 0:
            return "Please enter a valid amount to withdraw"
        else:
            return "Insufficient funds"

def main():
    atm = ATM(1000)  # Starting balance of $1000

    while True:
        print("\n**** Welcome to the ATM ****")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Please select an option: ")

        if choice == "1":
            print(f"Your current balance is ${atm.check_balance()}")
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: $"))
                print(atm.deposit(amount))
            except ValueError:
                print("Please enter a valid amount")
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: $"))
                print(atm.withdraw(amount))
            except ValueError:
                print("Please enter a valid amount")
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
