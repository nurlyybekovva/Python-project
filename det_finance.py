from finance import Finance
class DetailedFinanceManager(Finance):
    def show_detailed_transactions(self):
        for transaction in self.transactions:
            print(f"ID: {transaction['id']}")
            print(f"Type: {transaction['type']}")
            print(f"Amount: {transaction['amount']}")
            print(f"Category: {transaction['category']}")
            print(f"Date: {transaction['date']}")
            print()
