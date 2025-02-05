class accont:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"{self.owner} have: {self.balance}")
    def withdraw(self,amount):
        if self.balance<amount:
            print("{self.owner} cant take money, its too much")
        else:
            self.balance-=amount
            print(f"{self.owner} now ur balance is {self.balance}")
obj=accont("D",1000)
obj.deposit(1000)
obj.withdraw(300)
