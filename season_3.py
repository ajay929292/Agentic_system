class Bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        
    def deposit(self,amount):
        self.balance+=amount
        print(f"You deposited {amount} and now your current balance is {self.balance}")
        
    def withdrawl(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"You withdrawl {amount} and now your current balance is {self.balance}")
        else:
            print("Insufficient funds")


bank=Bankaccount("Ajay",20000)
bank.deposit(200)
bank.withdrawl(2000000)