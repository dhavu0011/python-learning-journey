class BankAccount:
    def __init__(self,account_holder,account_number,account_type,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.account_type=account_type
        self.balance=balance
    
    def display(self):
        print("---------------")
        print("Account holder:", self.account_holder)
        print("Account number:", self.account_number)
        print("Account type  :", self.account_type)
        print("Balance       :", self.balance)
        
    def __str__(self):
            return f"{self.account_holder},{self.account_number},{self.account_type},{self.balance}"
    
    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            print("Deposit successful.")
            print("New balance:",self.balance)
        else:
            print("Invalid deposit amount")
    
    def withdraw(self,amount):
        if amount>0:
            if self.balance >= amount:
                self.balance-=amount
                print("Withdraw successful.")
                print("balance : ",self.balance)
                return True
            else:
                print("Insufficient funds")
                return False
        else:
            print("Enter valid amount")
            return False
            
    def transfer(self, other_account, amount):
        if self.withdraw(amount):
            other_account.deposit(amount)
            print("Transfer success.")
        else:
            print("Transfer failed.")
        
def save_accounts(accounts):
    with open("account.txt","w")as file:
        for account in accounts:
            file.write(str(account)+"\n")
    
def load_accounts():
    accounts=[]
    with open("account.txt","r")as file:
        for line in file:
            line=line.strip()
            parts=line.split(",")
            account=BankAccount(
                parts[0].strip(),
                int(parts[1]),
                parts[2].strip(),                                        float(parts[3])
                )
            accounts.append(account)
    return accounts
    
def find_account(accounts, account_number):
    for account in accounts:
        if account.account_number == account_number:
            return account

    return None

                
def menu():
    while True:
        try:
            print("1.Add Account\n2.Show Accounts")
            print("3.Deposit\n4.Withdraw")
            print("5.Tranfer\n6.Save Accounts")
            print("7.Load Accounts\n8.Exit")
            
            choice = int(input("Enter your choice: "))
                        
            if 1 <= choice <= 8:
                return choice
            else:
                print("Please choose between 1 and 8.")
            
        except ValueError:
            print("Invalid input. Please enter a number.")
            
        
            
accounts=[]

while True:
    choice=menu()
    
    if choice==1:
        name=input("Enter account holder name:")
        while True:
            try:
                
                acc_number=int(input("Enter account number:"))
            except ValueError:
                print("Enter numbers only")
            else:
                if acc_number<0:
                    print("Enter valid number.")
                else:
                    break
        acc_type=input("Enter account type:")
        while True:
            try:
                acc_bal=int(input("Enter account starting balance:"))
            except ValueError:
                print("Enter numbers only")
            else:
                break
        account=BankAccount(name,acc_number,acc_type,acc_bal)
        accounts.append(account)
                

    elif choice==2:
        for account in accounts:
            account.display()
            
    elif choice==3:
        acc_number=int(input("Enter account number:"))
        account = find_account(accounts, acc_number)

        if account:
            while True:
                try:
                    amount = int(input("Enter amount: "))
                except ValueError:
                    print("Enter valid input.")
                else:
                    break
            account.deposit(amount)
        else:
            print("Account not found.")

            
                    
                    
    elif choice==4:
        ac_number=int(input("Enter account number:"))
        account = find_account(accounts, ac_number)

        if account:
            while True:
                try:
                    amount = int(input("Enter amount: "))
                except ValueError:
                    print("Enter valid input.")
                else:
                    break
            account.withdraw(amount)
        else:
            print("Account not found.")
    
    elif choice==5:
        acc_number1=int(input("Enter sender account number:"))
        acc_number2=int(input("Enter receiver account number:"))
        account = find_account(accounts, acc_number1)
        account2 = find_account(accounts, acc_number2)
        if account and account2:
            while True:
                try:
                    amount = int(input("Enter amount: "))
                except ValueError:
                    print("Enter valid input.")
                else:
                    break
                
            account.transfer(account2,amount)
        else:
            print("Cannot find account")

    elif choice==6:
        save_accounts(accounts)
        print("Accounts saved.")
    elif choice==7:
        accounts = load_accounts()
        print("Accounts loaded.")
    else:
        print("Good bye")
        break