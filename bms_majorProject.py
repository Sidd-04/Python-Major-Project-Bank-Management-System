class Account:
 def __init__(self, acc_no, acc_name, ph_no, add, cr_amt):
     self.acc_no = acc_no
     self.acc_name = acc_name
     self.ph_no = ph_no
     self.add = add
     self.cr_amt = cr_amt
     self.transactions = []

 def deposit(self,amount):
     self.cr_amt+= amount
     self.transactions.append(amount)

 def withdraw(self,amount):
    if self.cr_amt >= amount:
      self.cr_amt -= amount
      self.transactions.append(amount)
    else:
      print("Insufficient balance.")

 def display_details(self):
    print("Account Number:", self.acc_no)
    print("Account Name:", self.acc_name)
    print("Phone Number:", self.ph_no)
    print("Address:", self.add)
    print("Account Balance:", self.cr_amt)

 def display_transactions(self):
    print("Transaction History:")
    for transaction in self.transactions:
     print(transaction)

class Bank:
 def __init__(self):
     self.accounts = {}

 def create_account(self, acc_no, acc_name, ph_no, add, cr_amt):
     account = Account(acc_no, acc_name, ph_no, add, cr_amt)
     self.accounts[acc_no] = account
     print("Your account has been created successfully.")

 def login(self, acc_no, acc_name):
     if acc_no in self.accounts:
         account = self.accounts[acc_no]
         if account.acc_name == acc_name:
             return account
     else:
        print("Invalid account details.")

 def delete_account(self, acc_no):
     if acc_no in self.accounts:
         del self.accounts[acc_no]
         print("Account deleted successfully.")
     else:
         print("Account not found.")

 def change_account_details(self, acc_no):
    if acc_no in self.accounts:
         account = self.accounts[acc_no]
         print("Select the detail you want to change:")
         print("1. Account Name")
         print("2. Phone Number")
         print("3. Address")
         choice = int(input("Enter your choice: "))
         if choice == 1:
             new_name = input("Enter new account name: ")
             account.acc_name = new_name
             print("Account name updated successfully.")
         elif choice == 2:
             new_phone = int(input("Enter new phone number: "))
             account.ph_no = new_phone
             print("Phone number updated successfully.")
         elif choice == 3:
             new_address = input("Enter new address: ")
             account.add = new_address
             print("Address updated successfully.")
         else:
             print("Invalid choice.")
    else:
        print("Account not found.")

bank = Bank()

while True:
    print("\nWELCOME TO BANK PORTAL\n")
    print("1.CREATE ACCOUNT")
    print("2.LOGIN TO AN EXISTING ACCOUNT")
    print("3.EXIT")
    try:
        choice = int(input("CHOOSE ANY OPTION = "))
        if choice == 1:
            acc_no = int(input('\nEnter your ACCOUNT NUMBER='))
            acc_name = input('Enter your ACCOUNT NAME=')
            ph_no = int(input('Enter your PHONE NUMBER='))
            add = input('Enter your place=')
            cr_amt = int(input('Enter your credit  amount='))
            bank.create_account(acc_no, acc_name, ph_no, add, cr_amt)

        elif choice == 2:
            acc_no = int(input("\nENTER YOUR ACCOUNT NO= "))
            acc_name = input("ENTER YOUR NAME= ")
            account = bank.login(acc_no, acc_name)
            while True:
                print('1.TRANSACTION')
                print('2.CUSTOMER DETAILS')
                print('3.TRANSACTION DETAILS')
                print('4.CHANGE ACCOUNT DETAILS')
                print('5.DELETE ACCOUNT')
                print('6.EXIT')
                option = int(input("Enter your CHOICE = "))
                if option == 1:
                    print('\n1.WITHDRAW AMOUNT')
                    print('2.ADD AMOUNT\n')
                    trans_choice = int(input("Enter your CHOICE = "))
                    if trans_choice == 1:
                        amount = int(input('\nEnter Withdrawl Amount = '))
                        account.withdraw(amount)
                    elif trans_choice == 2:
                        amount = int(input('\nEnter Amount to be Deposited = '))
                        account.deposit(amount)
                    else:
                        raise ValueError("Invalid choice.")
                elif option == 2:
                    account.display_details()
                elif option == 3:
                    account.display_transactions()
                elif option == 4:
                    bank.change_account_details(acc_no)
                elif option == 5:
                    bank.delete_account(acc_no)
                    break
                elif option == 6:
                    break
                else:
                    print("Invalid option selected.")

        elif choice == 3:
            print("Thank you for using our service.")
            break
        else:
           print("Invalid choice.")

    except ValueError as ve:
        print("Error:", ve)