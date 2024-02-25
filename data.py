import json
class Data:
    def save_to_json(filename, transactions):
        with open(filename, 'w') as f:
            json.dump(transactions, f)

    def load_to_json(filename):
        with open(filename, 'r') as f:
            return json.load(f)