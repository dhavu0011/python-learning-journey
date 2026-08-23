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
            
            
accounts=[]