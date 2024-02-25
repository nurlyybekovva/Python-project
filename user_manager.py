import csv

class UserManager:
    def __init__(self, filename):
        self.filename = filename

    def check_credentials(self, username, password):
        with open(self.filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == username and row[1] == password:
                    return True
        return False

    def register_user(self, username, password):
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([username, password])
        print("User registered successfully.")

    def is_user_registered(self, username):
        with open(self.filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == username:
                    return True
        return False
