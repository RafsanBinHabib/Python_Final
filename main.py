from acc import Account
from admin import Admin
from bank import Bank

brac = Bank()

def user_menu():
    print("-----User Registration-----")
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    address = input("Enter Your Address: ")
    account_type = input("Enter Your Account Type: ")
    user = Account(name=name, email=email, address=address, account_type=account_type)
    brac.add_account(user)
    
    while True:
        print(f"\n-----Welcome {user.name}-----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Apply for Loan")
        print("6. Transfer")
        print("7. Exit")
        
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            amount = int(input("Enter Your Amount: "))
            user.deposit(amount)
        elif choice == 2:
            amount = int(input("Enter Your Amount: "))
            user.withdraw(amount)
        elif choice == 3:
            user.check_balance()
        elif choice == 4:
            user.view_transaction_history()
        elif choice == 5:
            amount = int(input("Enter Your Loan Amount: "))
            user.take_loan(amount, brac)
        elif choice == 6:
            amount = int(input("Enter Transfer Amount: "))
            transfer_account = input("Enter Recipient Account Number: ")
            user.transfer(amount, transfer_account, brac)
        elif choice == 7:
            print("Exiting User Menu.")
            break
        else:
            print("Invalid Input!")

def admin_menu():
    admin = Admin(bank=brac)
    
    while True:
        print(f"\n-----Welcome Admin-----")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. View User Accounts")
        print("4. Check Total Balance")
        print("5. Check Total Loan Amount")
        print("6. Toggle Loan Feature")
        print("7. Exit")
        
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            name = input("Enter Account Holder Name: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            account_type = input("Enter Account Type: ")
            admin.create_account(name, email, address, account_type)
        elif choice == 2:
            acc_num = input("Enter Account Number to Delete: ")
            admin.delete_account(acc_num)
        elif choice == 3:
            admin.list_all_accounts()
        elif choice == 4:
            admin.check_total_balance()
        elif choice == 5:
            admin.check_total_loan_amount()
        elif choice == 6:
            admin.toggle_loan_feature()
        elif choice == 7:
            print("Exiting Admin Menu.")
            break
        else:
            print("Invalid Input!")

def main_menu():
    while True:
        print("\n-----Welcome to the Bank-----")
        print("1. User")
        print("2. Admin")
        print("3. Exit")
        
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            user_menu()
        elif choice == 2:
            admin_menu()
        elif choice == 3:
            print("Thank You for Using the Bank System!")
            break
        else:
            print("Invalid Choice!")
          
            
main_menu()