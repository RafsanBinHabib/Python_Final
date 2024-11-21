class Bank:
    def __init__(self):
        self.accounts = {}
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_on = True

    def add_account(self, account):
        if account.account_number in self.accounts:
            print(f"Account with number {account.account_number} already exists!")
        else:
            self.accounts[account.account_number] = account
            print(f"Account '{account.account_number}' added successfully.")

    def delete_account(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            self.total_balance -= account.balance
            self.total_loan_amount -= sum(txn["amount"] for txn in account.transaction_history if txn["type"] == "loan")
            del self.accounts[account_number]
            print(f"Account '{account_number}' deleted successfully.")
        else:
            print(f"Account '{account_number}' does not exist!")

    def view_all_accounts(self):
        if not self.accounts:
            print("No accounts available.")
        else:
            print("All Accounts:")
            for account_number, account in self.accounts.items():
                print(
                    f"Account Number: {account_number}, Name: {account.name}, Balance: {account.balance}"
                )

    def view_total_balance(self):
        self.total_balance = sum(account.balance for account in self.accounts.values())
        print(f"Total Balance: {self.total_balance}")

    def view_total_loan_amount(self):
        self.total_loan_amount = sum(
            sum(txn["amount"] for txn in account.transaction_history if txn["type"] == "loan")
            for account in self.accounts.values()
        )
        print(f"Total Loan Amount: {self.total_loan_amount}")

    def enable_loans(self):
        if self.loan_feature_on:
            print("Loan feature is already enabled.")
        else:
            self.loan_feature_on = True
            print("Loan feature enabled.")

    def disable_loans(self):
        if not self.loan_feature_on:
            print("Loan feature is already disabled.")
        else:
            self.loan_feature_on = False
            print("Loan feature disabled.")