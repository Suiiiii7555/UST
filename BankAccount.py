class BankAccount:
    def __init__(self , account_no , name , balance=0):
        print("Your bank account has been created.")
        self.account_no = account_no
        self.name = name
        self.balance = balance

    
    def deposit(self , amount):
        self.balance = self.balance + amount
        

    def withdrawal(self , amount_withdrawal):
        if amount_withdrawal <= self.balance:
            self.balance = self.balance - amount_withdrawal
        else:
            print("Please check your balance")