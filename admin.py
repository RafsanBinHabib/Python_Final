from acc import Account

class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        account = Account(name, email, address, account_type)
        self.bank.add_account(account)
        print(f"Account created successfully: {account.account_number}")
        return account

    def delete_account(self, account_number):
        try:
            self.bank.delete_account(account_number)
            print(f"Account '{account_number}' deleted successfully.")
        except KeyError:
            print(f"Error: Account '{account_number}' does not exist.")

    def list_all_accounts(self):
        print("Listing all accounts:")
        self.bank.view_all_accounts()

    def check_total_balance(self):
        print("Checking total bank balance:")
        self.bank.view_total_balance()  
    
    def check_total_loan_amount(self):
        print("Checking total loan amount:")
        self.bank.view_total_loan_amount() 

    def toggle_loan_feature(self):
        if self.bank.loan_feature_on:
            self.bank.disable_loans()
            print("Loan feature disabled.")
        else:
            self.bank.enable_loans()
            print("Loan feature enabled.")