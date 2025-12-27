class BankAccount:

    interest_rate = 1.5

    def __init__(self,account_no,account_holder,account_balance):
        self.account_no = account_no
        self.account_holder = account_holder
        self.account_balance = account_balance

    def calculate_interest(self):
        interest = self.account_balance * BankAccount.interest_rate
        return interest

acc1 = BankAccount(123,"sathvik",10000)

print(BankAccount.interest_rate)

print(acc1.calculate_interest())
