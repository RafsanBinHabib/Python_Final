import uuid

class Account:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = str(uuid.uuid4())[:10]
        self.balance = 0
        self.transaction_history = []
        self.loan_count = 0

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        self.balance += amount
        self.transaction_history.append({"type": "deposit", "amount": amount})
        print(f"Deposited {amount}")
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        if amount > self.balance:
            print("Withdrawal amount exceeded!")
            return
        self.balance -= amount
        self.transaction_history.append({"type": "withdraw", "amount": amount})
        print(f"Withdrew {amount}")
        return self.balance

    def check_balance(self):
        print(f"Balance is {self.balance}")
        return self.balance

    def view_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self, amount, bank):
        if not bank.loan_feature_on:
            print("Loan feature is disabled.")
            return
        if self.loan_count >= 2:
            print("Maximum loan limit reached.")
            return
        if amount <= 0:
            print("Loan amount must be positive.")
        self.balance += amount
        self.loan_count += 1
        bank.total_loan_amount += amount
        self.transaction_history.append({"type": "loan", "amount": amount})
        print(f"Took loan of {amount}")
        return self.balance

    def transfer(self, amount, transfer_account, bank):
        if amount <= 0:
            print("Transfer amount must be positive.")
        if self.balance < amount:
            print("Insufficient balance for transfer!")
            return
        if transfer_account not in bank.accounts:
            print("Account does not exist.")
            return
        to_account = bank.accounts[transfer_account]
        self.balance -= amount
        to_account.balance += amount
        self.transaction_history.append({"type": "transfer_out", "amount": amount, "to": transfer_account})
        to_account.transaction_history.append({"type": "transfer_in", "amount": amount, "from": self.account_number})
        print(f"Transferred {amount} to {transfer_account}")
        return self.balance