class Account:
    
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account Owner : {self.owner} and Account Balance :${self.balance}'
        
    def deposit(self,deposit_amount):
        self.balance += deposit_amount
        print("Deposit Accepted")
    
    def withdraw(self,withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print("Withdrawal Accepted")
        else:
            print("Insufficient Funds")

acct1 = Account('John',500)

print(acct1)

print(acct1.owner)

print(acct1.balance)

acct1.deposit(50)

acct1.withdraw(75)

acct1.withdraw(500)
    
    
    
