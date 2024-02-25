from data import Data
class Finance:
    def __init__(self):

        self.transactions = Data.load_to_json("transactions.json")

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        Data.save_to_json("transactions.json",self.transactions)  # Save transactions to JSON file

    def delete_transaction(self, transaction):
        for i, transaction in enumerate(self.transactions):
            if transaction['id'] == id:
                del self.transactions[i]
                Data.save_to_json("transactions.json",self.transactions)   # Save transactions to JSON file
                return True
        return False

    def get_transactions(self):
        for transaction in self.transactions:
            print(transaction)

    def generate_report(self, start_date, end_date):
        total_income = 0
        total_expense = 0
        Data.load_to_json("transactions.json")
        for transaction in self.transactions:
            if start_date <= transaction['date'] <= end_date:
                if transaction['type'] == "income":
                    total_income += transaction['amount']
                else:
                    total_expense += transaction['amount']
        print(f"Total income for period {start_date} to {end_date}: {total_income} tenge.")
        print(f"Total expense for period {start_date} to {end_date}: {total_expense} tenge.")

    def current_balance(self):

        total = 0
        for transaction in self.transactions:
            if transaction['type'] == "income":
                total += transaction['amount']
            if transaction['type'] == "expense":
                total -= transaction['amount']
        print(f"Bank account balance: {total} tenge.")


    def show_detailed_transactions(self):
        return 0
