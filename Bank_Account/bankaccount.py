class BankAccount:
    def __init__(self  , name , account_no , balance=0):
        print("Your bank account has been created.")
        self.name = name
        self.account_no = account_no
        self.balance = balance

    
    def deposit(self , amount):
        self.balance = self.balance + amount
        

    def withdrawal(self , amount_withdrawal):
        if amount_withdrawal <= self.balance:
            self.balance = self.balance - amount_withdrawal
        else:
            print("Please check your balance")

    def __str__(self):
        return f"Bank Account Details :\n{self.name}\n{self.account_no}\n{self.balance}"