from bankaccount import BankAccount

account_1 = BankAccount( account_no = 1234567890 , name="Sathvik", balance = 100000)

# print(f"Account details of user ({account_1.name}) is as  follows : \nName is {account_1.name} \nNumber is {account_1.account_no} \nInitial Balance is {account_1.balance}")

# account_2 = BankAccount(name="Nandeesha",account_no = 1357913579)

# print("<--------------------------------------------------------------------------->")

# print(f"Account details of user {account_2.name} is as follows : \nName is {account_2.name} \nNumber is {account_2.account_no} \nBalance is {account_2.balance}")

# print("Depositing amount to account 1")

# print(f"Initial balance of user  {account_1.name} is {account_1.balance}")

# account_1.deposit(100000)

# print(f"Balance of user {account_1.name} after depositng money is {account_1.balance}")
print(account_1)

