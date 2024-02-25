from det_finance import DetailedFinanceManager
from user_manager import UserManager
def start_menu(user_manager):
    print("\n⋆｡‧˚ʚ♡ɞ˚‧｡⋆ MENU ⋆｡‧˚ʚ♡ɞ˚‧｡⋆")
    print("1. Login")
    print("2. Sign up")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        while True:
            login = input("Enter your login: ")
            password = input("Enter your password: ")
            if user_manager.check_credentials(login, password):
                print("Login successful!")
                break
            else:
                print("Invalid username or password.")

    elif choice == 2:
        login = input("Enter your login: ")
        password = input("Enter your password: ")
        if user_manager.is_user_registered(login):
            print("User already exists.")
        else:
            user_manager.register_user(login, password)
    elif choice == 3:
        print("Exiting...")
    else:
        print("Invalid choice. Try again.")


def main_menu():
    print("\n⋆｡‧˚ʚ♡ɞ˚‧｡⋆ MENU ⋆｡‧˚ʚ♡ɞ˚‧｡⋆")
    print("1. View all financial transactions")
    print("2. Income and expense report for the selected period")
    print("3. Bank account balance")
    print("4. Edit financial transactions")
    print("5. Exit")


if __name__ == "__main__":
    user_manager = UserManager("users.csv")
    start_menu(user_manager)

    while True:
        main_menu()
        ch= int(input("Enter your choice: "))
        if ch == 1:
            finance = DetailedFinanceManager()
            finance.show_detailed_transactions()
        elif ch == 2:
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            finance = DetailedFinanceManager()
            finance.generate_report(start_date, end_date)
        elif ch == 3:
            finance = DetailedFinanceManager()
            finance.current_balance()
        elif ch == 4:
            print("1. Add a new transaction")
            print("2. Delete an existing transaction")
            ch1 = input("Enter your choice(add/delete): ")

            if ch1 == "add":
                transaction_type = input("Enter transaction type (income or expense): ")
                amount = float(input("Enter transaction amount: "))
                category = input("Enter transaction category: ")
                date = input("Enter transaction date (YYYY-MM-DD): ")
                finance = DetailedFinanceManager()
                transaction = {'id': len(finance.transactions) + 1, 'type': transaction_type, 'amount': amount, 'category': category, 'date': date}
                finance.add_transaction(transaction)
                print("Transaction added successfully.")
            elif ch1 == "delete":
                transaction_id = int(input("Enter ID of the transaction to delete: "))
                if finance.delete_transaction(transaction_id):
                    print("Transaction deleted successfully.")
                else:
                    print("Transaction not found.")

        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")