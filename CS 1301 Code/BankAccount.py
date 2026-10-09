class BankAccount:
    def __init__ (self, account_number, balance):
        self.account_number=account_number
        self.balance=balance

    def calculate_interest():
        return 0
    
    def display_interest(self):
        return f"Account: {self.account_number} Interest: {self.calculate_interest()}"

class SavingAccount(BankAccount):
    def __init__ (self, account_number, balance,interest_rate):
        BankAccount.__init__(self, account_number,balance)
        self.interest_rate=interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

class CheckingAccount(BankAccount):
    def __init__ (self, account_number, balance,interest_rate):
        BankAccount.__init__(self, account_number,balance)
        self.interest_rate=interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

class FixedDeposit(BankAccount):
    def __init__ (self, account_number, balance,interest_rate,term_years):
        BankAccount.__init__(self, account_number,balance)
        self.interest_rate=interest_rate
        self.term_years=term_years
    
    def calculate_interest(self):
        return self.balance * self.interest_rate * self.term_years

result_list=[]

retry=True

while retry==True:
    saving_account_number=input("Please enter the account number for your savings account: ")
    saving_balance=float(input("Please enter the balance for your savings account: "))
    saving_interest_rate=float(input("Please enter the interest rate for your savings account: "))
    saving_interest_rate=saving_interest_rate/100
    saving=SavingAccount(saving_account_number,saving_balance,saving_interest_rate)
    result_list.append(saving)

    checking_account_number=input("Please enter the account number for your checking account: ")
    checking_balance=float(input("Please enter the balance for your checking account: "))
    checking_interest_rate=float(input("Please enter the interest rate for your checking account: "))
    checking_interest_rate=checking_interest_rate/100
    checking=CheckingAccount(checking_account_number,checking_balance,checking_interest_rate)
    result_list.append(checking)

    fixed_account_number=input("Please enter the account number for your fixed deposit account: ")
    fixed_balance=float(input("Please enter the balance for your fixed deposit account: "))
    deposit_interest_rate=float(input("Please enter the interest rate for your fixed deposit account: "))
    term_years=int(input("Please enter the length of the term in years for your fixed deposit account: "))
    deposit_interest_rate=deposit_interest_rate/100
    fixed=FixedDeposit(fixed_account_number,fixed_balance,deposit_interest_rate,term_years)
    result_list.append(fixed)
    
    retryPrompt=input("Would you like to enter information for more accounts (y/n): ")
    
    if retryPrompt=="y":
        retry=True
    else:
        retry=False

if retry==False:
    for item in result_list:
        print(item.display_interest())