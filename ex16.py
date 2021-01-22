def get_info():
    """ Get user information in a dict that represents a banck account"""
    print("Wlecome to the Pythonf first National Bank.")
    name = input("Hello, what's you name: ").title().strip()
    savings = int(input("Welcome " +  name + " How much money would you like to set up on your savings account with :"))
    checking = int(input("How much money would you like to set up on your checking account with :"))
    bank_account = {
        "Name" :name,
        "Savings":savings,
        "Checking":checking,
        }
    return bank_account
def make_deposit(bank_account, account, money):
    """Add money"""
    bank_account[account] += money
    print("Desposited DHS" + str(money) + "into " + bank_account["Name"] + "'s" +account.lower() +  "account.")
def make_withdrawal(back_account, account, money):
    """withdraw money"""
    if bank_account[account] - money >= 0:
        bank_account[account] -= money
        print("Withdrew DHS" + str(money) + "from" +bank_account["Name"] + "'s" + account.lower() +"account.")
    else:
        print("Sorry, by withdrawing Dhs" + str(money) + "You will have a negative")
#dictionnaries are mutable we can its value directly on nak_account(account) +=money
def display_info(bank_account):
   print("current Account Information")
   for key,value in bank_account.items():
       if key == 'Name':
          print(key + ": " +str(value))
       else:
          print(key + ": Dhs" +str(value))
my_account = get_info()
display_info(my_account)
