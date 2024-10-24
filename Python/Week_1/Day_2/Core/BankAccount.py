class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance:.2f}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self 

account1 = BankAccount(int_rate=0.01 , balance=100)
account2 = BankAccount(int_rate=0.01 , balance=1000)
account1.deposit(500).deposit(150).deposit(200).withdraw(300).yield_interest().display_account_info()
account2.deposit(800).deposit(1600).withdraw(80).withdraw(100).withdraw(800).withdraw(300).yield_interest().display_account_info()