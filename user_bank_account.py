class BankAccount:
    
    all_accounts = []
    
    def __init__(self, int_rate = 0.05, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance += amount
        else:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
        # return f"Balance {self.balance}"

    def yield_interest(self):
        if(self.balance) > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def display_all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum
        

customer_account1 = BankAccount(0.04, 700)
customer_account2 = BankAccount(0.07, 2000)

customer_account1.deposit(800).deposit(500).deposit(150).withdraw(950).yield_interest().display_account_info()
customer_account2.deposit(2000).deposit(2000).withdraw(300).withdraw(150).withdraw(75).withdraw(950).yield_interest().display_account_info()

print(BankAccount.display_all_balances())

class User:
    # class attributes - defined in the class
    bank_name = "First National Dojo"

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = {
            'checking' : BankAccount(0.09, 0),
            'savings' : BankAccount(0.01, 0),
        }
        # self.checking_account = BankAccount()
        # self.savings_account = BankAccount()
    # deposit method
    def make_deposit(self, amount, account_type):
        self.account[account_type].deposit(amount)
    # withdrawal method
    def make_withdrawal(self, amount, account_type):
        self.account[account_type].withdraw(amount)
    # display user balance method
    def display_user_balance(self, account_type):
        print(f"User: {self.name}")
        self.account[account_type].display_account_info()
    def tranfer_money(self, other_user, amount, account_type):
        self.make_withdrawal(amount, account_type)
        other_user.make_deposit(amount, account_type)

santana = User("Carlos Santana", "santan@python.com")
jacob = User("Jacob Collier", "jacob@python.com")
bowie = User("David Bowie", "d.bowie@python.com")

santana.make_deposit(4000, "checking")
santana.make_deposit(2300, "savings")
santana.make_deposit(3700, "savings")
santana.display_user_balance("savings")

jacob.make_deposit(15000, "checking")
jacob.make_deposit(2000, "savings")
jacob.make_withdrawal(500, "checking")
jacob.make_withdrawal(1200, "savings")
jacob.display_user_balance("checking")
jacob.display_user_balance("savings")

bowie.make_deposit(18000, "checking")
bowie.make_deposit(8000, "savings")
bowie.make_withdrawal(2500, "checking")
bowie.make_withdrawal(350, "checking")
bowie.display_user_balance("checking")

# BONUS - Transfer of money. 
santana.tranfer_money(bowie, 2350, "checking")
jacob.display_user_balance("checking")
jacob.display_user_balance("savings")
santana.display_user_balance("checking")
santana.display_user_balance("savings")
bowie.display_user_balance("checking")
bowie.display_user_balance("savings")   